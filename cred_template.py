import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
# On Render, environment variables are set directly in dashboard
load_dotenv()

#Twilio Details
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilionumber = os.getenv('TWILIO_PHONE_NUMBER')
twiliosmsnumber = os.getenv('TWILIO_SMS_NUMBER')

#FC Bot
API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

#Host URL (Use Render URL in production, ngrok URL for local testing)
callurl = os.getenv('SERVER_URL')
twiliosmsurl = os.getenv('SERVER_SMS_URL')

# Validate that all required environment variables are set
required_vars = [
    'TWILIO_ACCOUNT_SID',
    'TWILIO_AUTH_TOKEN', 
    'TWILIO_PHONE_NUMBER',
    'TWILIO_SMS_NUMBER',
    'TELEGRAM_BOT_TOKEN',
    'SERVER_URL',
    'SERVER_SMS_URL'
]

missing_vars = [var for var in required_vars if not os.getenv(var)]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
