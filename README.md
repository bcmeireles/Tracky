# Tracky

Tracky is allows users to track shipments from multiple courier services in one place. Users can create accounts, add tracking numbers, and receive updates on their shipments conveniently.

## Features

- **Multi-Courier Support:** Track shipments from various courier services, including UPS, DHL, YunExpress, CTT, Paack, etc.
- **User Accounts:** Users can sign up, log in, and manage their shipments through personalized accounts.
- **Responsive Design:** The website is designed to be accessible and functional across different devices and screen sizes.

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