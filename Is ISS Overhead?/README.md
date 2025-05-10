# ISS Overhead Notifier
This project sends you an email notification when the International Space Station (ISS) is flying over your location at night. It uses real-time ISS position data and sunrise/sunset times to determine visibility.

## How it works:
- **Fetches ISS position** from the [Open Notify API](http://open-notify.org/).
- **Checks nighttime visibility** using the [Sunrise-Sunset API](https://sunrise-sunset.org/api).
- **Sends an email alert** via Gmail if:
  - The ISS is within **5 degrees** of your coordinates.
  - It’s dark outside (after sunset and before sunrise).
- **Runs continuously**, checking conditions every 60 seconds.

## Key Features:
- Real-time API integration for ISS tracking.
- Automated email notifications via SMTP.
- Customizable location coordinates.

---

**Note:**  
- Replace `MY_LAT` and `MY_LONG` with your latitude and longitude.
- Use environment variables for `sender_email` and `app_password` to secure your Gmail credentials.

## Dependencies:  
- `requests` (for API calls) & to be installed seperately / through requirements.txt.
- `smtplib` (for email notifications)  
- `datetime` and `time` (for scheduling and time checks)  
