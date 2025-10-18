#!/bin/bash
# Render startup script

# Copy template to cred.py if it doesn't exist
if [ ! -f cred.py ]; then
    echo "Creating cred.py from template..."
    cp cred_template.py cred.py
fi

# Start the application
gunicorn mainn:app
