# Tracky

Tracky is allows users to track shipments from multiple courier services in one place. Users can create accounts, add tracking numbers, and receive updates on their shipments conveniently.

## Features

- **Multi-Courier Support:** Track shipments from various courier services, including UPS, DHL, YunExpress, CTT, Paack, etc.
- **User Accounts:** Users can sign up, log in, and manage their shipments through personalized accounts.
- **Responsive Design:** The website is designed to be accessible and functional across different devices and screen sizes.
- **Email Verification:** Only mail verified users can get past the website's login, these verifications are handled by firebase.
- **Real Tracking Hyperlinks:** Each parcel being tracked has a button to be redirected to a courier's official tracking page, already on the page for the specific parcel selected

## Requirements
- Python
- Node
- MongoDB

There is a Docker container for easy setup but to manually do it:

```bash
cd backend
pip install -r requirements.txt
python app.py

cd ../frontend
npm install
npm start
```

Make sure to update `frontend/src/firebase.js` with your own credentials

## Screenshots
### Parcel Cards
Light Mode
![Light Mode](screenshots/light.png)
Dark Mode
![Dark Mode](screenshots/dark.png)