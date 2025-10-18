#!/bin/bash
# Render startup script

# Copy template to cred.py if it doesn't exist
if [ ! -f cred.py ]; then
    echo "Creating cred.py from template..."
    cp cred_template.py cred.py
fi

# Initialize database if it doesn't exist
if [ ! -f UserDetails.db ]; then
    echo "Initializing database..."
    python dbase.py
    python createadmin.py
fi

# Start the application with correct binding
exec gunicorn app:app --bind 0.0.0.0:$PORT
