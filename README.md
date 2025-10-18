# Techie OTP Bot 🤖

A Telegram bot for automated OTP/PIN calling with Twilio integration and Hindi voice support.

## Features ✨

- 📞 Automated OTP/PIN calls via Twilio
- 💬 SMS mode support
- 🇮🇳 Natural Hindi voice (Polly.Aditi)
- 🔙 Back button navigation
- 🏦 Multiple service templates (Bank, PhonePe, etc.)
- 🎯 Admin & User modes
- 📊 SQLite database for user management

## Setup Instructions 🚀

### 1. Clone Repository
```bash
git clone https://github.com/Gobinda988888/otpbot.git
cd otpbot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy `.env.example` to `.env` and fill in your credentials:
```bash
cp .env.example .env
```

Edit `.env` with your actual values:
```env
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=+1234567890
TELEGRAM_BOT_TOKEN=your_bot_token
NGROK_URL=your_server_url
```

### 4. Setup Database
```bash
python dbase.py
```

### 5. Create Admin User
Edit `createadmin.py` with your Telegram user ID and run:
```bash
python createadmin.py
```

### 6. Run Locally (Development)
```bash
# Start ngrok
ngrok http 5000

# Update NGROK_URL in .env with the ngrok URL

# Run the bot
python mainn.py
```

## Deploy to Render 🌐

### Option 1: Automatic Deploy
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

### Option 2: Manual Deploy

1. **Create Render Account**: https://render.com
2. **New Web Service**: Connect your GitHub repository
3. **Configure**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn mainn:app`
   - **Environment Variables**: Add all variables from `.env`

4. **Deploy**: Click "Create Web Service"

5. **Update Bot Webhook**:
   - Copy your Render URL: `https://your-app.onrender.com`
   - Update `NGROK_URL` environment variable in Render

## Environment Variables 🔐

| Variable | Description | Example |
|----------|-------------|---------|
| `TWILIO_ACCOUNT_SID` | Twilio Account SID | `ACxxxxxxxxxxxxx` |
| `TWILIO_AUTH_TOKEN` | Twilio Auth Token | `xxxxxxxxxxxxxxx` |
| `TWILIO_PHONE_NUMBER` | Twilio Phone Number | `+1234567890` |
| `TWILIO_SMS_NUMBER` | Twilio SMS Number | `+1234567890` |
| `TELEGRAM_BOT_TOKEN` | Telegram Bot Token | `123456:ABCdefg...` |
| `NGROK_URL` | Server URL | `https://your-app.com` |
| `NGROK_SMS_URL` | SMS Webhook URL | `https://your-app.com/sms` |

## Usage 📱

1. Start bot: `/start`
2. Choose mode (User/Admin)
3. Enter target phone number
4. Select call type (OTP/PIN/Card)
5. Enter service name
6. Bot makes automated call

## Important Notes ⚠️

- **Free Twilio Account**: Can only call verified numbers
- **Paid Twilio**: Can call any number
- **Render Free Tier**: App sleeps after 15 mins of inactivity
- **ngrok Free**: URL changes on restart (for local testing)

## Security 🔒

- Never commit `.env` file
- Keep credentials secure
- Use for educational/ethical purposes only

## Tech Stack 💻

- **Backend**: Flask (Python)
- **Bot**: pyTelegramBotAPI
- **Voice**: Twilio
- **Database**: SQLite
- **Hosting**: Render
- **Tunneling**: ngrok (development)

## License 📄

Educational purposes only.

## Support 💬

For issues or questions, contact @TechieGamer on Telegram.

---

Made with ❤️ by Techie Team
