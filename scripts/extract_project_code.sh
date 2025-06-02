#!/bin/bash

# Move to the project root directory
cd "$(dirname "$0")/.."

# Extract all key project code into a flat text file
(
  echo "===== Dockerfile ====="
  cat Dockerfile

  echo "===== docker-compose.yml ====="
  cat docker-compose.yml

  echo "===== docker-compose-prod.yml ====="
  cat docker-compose-prod.yml

  echo "===== heroku.yml ====="
  cat heroku.yml

  echo "===== requirements.txt ====="
  cat requirements.txt

  echo "===== manage.py ====="
  cat manage.py

  # Loop through all main apps and their common files
  for app in accounts pages workorders clients invoices; do
    for file in models.py views.py forms.py urls.py admin.py; do
      if [ -f $app/$file ]; then
        echo -e "\n\n===== $app/$file ====="
        cat $app/$file
      fi
    done
  done

  # Include core project config files
  for file in settings.py urls.py asgi.py wsgi.py; do
    echo -e "\n\n===== django_project/$file ====="
    cat django_project/$file
  done

  # Include all HTML templates
  find templates -type f -name "*.html" | while read tmpl; do
    echo -e "\n\n===== $tmpl ====="
    cat "$tmpl"
  done
) > project_code_output.txt
