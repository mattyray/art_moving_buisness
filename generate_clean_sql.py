import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
import decimal

# Connect to your local recovery DB
conn = psycopg2.connect(dbname="workorders_recovery")
cursor = conn.cursor(cursor_factory=RealDictCursor)

# Get client name → id mapping
cursor.execute("SELECT id, name FROM clients_client;")
clients = {row["name"]: row["id"] for row in cursor.fetchall()}

# Get workorders (must include client_name!)
cursor.execute("SELECT * FROM workorders_workorder;")
rows = cursor.fetchall()

output = []

for row in rows:
    client_name = row.get("client_name")
    client_id = clients.get(client_name)

    if not client_id:
        print(f"⚠️ Skipping: No client_id found for {client_name}")
        continue

    cols = []
    vals = []

    for k, v in row.items():
        if k == "client_name":
            continue  # Skip this field
        elif k == "client_id":
            cols.append("client_id")
            vals.append(str(client_id))
        else:
            cols.append(k)
            if isinstance(v, str):
                safe_str = v.replace("'", "''")
                vals.append(f"'{safe_str}'")
            elif isinstance(v, bool):
                vals.append('TRUE' if v else 'FALSE')
            elif isinstance(v, datetime):
                vals.append(f"'{v.isoformat()}'")
            elif isinstance(v, decimal.Decimal):
                vals.append(str(v))
            elif v is None:
                vals.append("NULL")
            else:
                vals.append(str(v))

    line = f"INSERT INTO workorders_workorder ({', '.join(cols)}) VALUES ({', '.join(vals)});"
    output.append(line)

cursor.close()
conn.close()

with open("clean_insert.sql", "w") as f:
    f.write("\n".join(output))

print("✅ Done! Saved to clean_insert.sql")
