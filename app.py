# Wrapper file for Render deployment
# This allows using 'gunicorn app:app' command
from mainn import app

if __name__ == "__main__":
    app.run()
