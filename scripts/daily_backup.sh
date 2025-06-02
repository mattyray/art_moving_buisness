#!/bin/bash

# Set variables
DATE=$(date +%F)
BACKUP_DIR="backups"
JSON_FILE="$BACKUP_DIR/full_backup_$DATE.json"
B64_FILE="$BACKUP_DIR/full_backup_$DATE.b64"

# Export the full database to JSON
docker compose exec web python manage.py dumpdata --natural-primary --natural-foreign --indent 2 > "$JSON_FILE"

# Encode the JSON file to Base64
base64 "$JSON_FILE" > "$B64_FILE"
