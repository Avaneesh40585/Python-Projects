# Motivational Quote Automated-Mail
A simple Python script that sends a random motivational quote to your email every Monday morning!

## How it works
- Reads all quotes from `quotes.txt`
- Selects a random quote
- Checks if today is Monday
- Sends the quote to your email via Gmail SMTP

## Setup Instructions
1. **Add your email credentials**  
   Replace `sender_email`, `app_password`, and `receiver_email` in the script with your information.  
   *Tip: For security, use environment variables instead of hardcoding credentials.*

2. **Prepare your quotes file**
   - Create a `quotes.txt` file in the same directory.
   - Add one quote per line.
---

Never miss your weekly dose of motivation!
