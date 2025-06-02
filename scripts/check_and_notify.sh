#!/bin/bash

TODAY=$(date +%F)
YESTERDAY=$(date -v-1d +%F)  # For Mac. Use GNU date on Linux: date -d yesterday +%F
HASH_DIR="$HOME/db_hashes"
EMAIL="you@example.com"

mkdir -p "$HASH_DIR"

# Create a DB hash from Heroku prod DB (example: workorders_workorder)
heroku pg:psql --app art-moving-buisness \
  --command="SELECT md5(string_agg(t::text, '')) FROM (SELECT * FROM workorders_workorder ORDER BY id) t;" \
  | tail -n 1 | awk '{print $1}' > "$HASH_DIR/hash_$TODAY.txt"

# Compare with yesterday’s hash
if [ -f "$HASH_DIR/hash_$YESTERDAY.txt" ]; then
  if ! cmp -s "$HASH_DIR/hash_$YESTERDAY.txt" "$HASH_DIR/hash_$TODAY.txt"; then
    echo "🚨 The production database has changed on $TODAY." | mail -s "Art Mover DB Changed" $EMAIL
  fi
fi
