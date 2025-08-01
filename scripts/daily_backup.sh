#!/bin/bash
export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

# Set environment
DATE=$(date +%Y-%m-%d)
BACKUP_DIR="backups"
JSON_FILE="$BACKUP_DIR/full_backup_${DATE}.json"
B64_FILE="$BACKUP_DIR/full_backup_${DATE}.b64"
DUMP_FILE="$BACKUP_DIR/full_backup_${DATE}.dump"
EMAIL="mnraynor90@gmail.com"
APP_NAME="art-moving-buisness"

mkdir -p "$BACKUP_DIR"

echo "📦 Dumping Heroku production database as JSON..."
heroku run --app "$APP_NAME" python manage.py dumpdata > "$JSON_FILE"

if [ ! -s "$JSON_FILE" ]; then
  echo "❌ JSON dump failed or file is empty."
  exit 1
fi

echo "🔐 Encoding JSON to base64..."
base64 -i "$JSON_FILE" -o "$B64_FILE"

echo "📦 Capturing and downloading raw .dump of production database..."
heroku pg:backups:capture --app "$APP_NAME"
heroku pg:backups:download --app "$APP_NAME" --output "$DUMP_FILE"

if [ ! -s "$DUMP_FILE" ]; then
  echo "❌ .dump file generation failed."
  exit 1
fi

echo "✅ Backup complete:"
echo "- JSON: $JSON_FILE"
echo "- Base64: $B64_FILE"
echo "- .dump: $DUMP_FILE"

# Email confirmation
echo -e "✅ Daily backup completed successfully on $DATE.\n\nFiles created:\n- $JSON_FILE\n- $B64_FILE\n- $DUMP_FILE" | msmtp "$EMAIL"
