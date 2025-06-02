#!/bin/bash

# Set timestamp
TIMESTAMP=$(date +%F)

# Set output paths
BACKUP_DIR="backups"
JSON_FILE="$BACKUP_DIR/full_backup_${TIMESTAMP}.json"
B64_FILE="$BACKUP_DIR/full_backup_${TIMESTAMP}.b64"

# Dump production database using Heroku (with quoted command)
echo "Dumping Heroku production database..."
heroku run --app art-moving-buisness "python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.permission --indent 2" > "$JSON_FILE"

# Encode JSON to base64 (macOS syntax)
echo "Encoding JSON to base64..."
base64 -i "$JSON_FILE" -o "$B64_FILE"

echo "✅ Backup complete:"
echo "- JSON: $JSON_FILE"
echo "- Base64: $B64_FILE"

echo "Backup for $DATE completed successfully." | mail -s "Database Backup Complete - $DATE" mnraynor90@gmail.com
