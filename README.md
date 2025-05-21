Zoho CRM Excel Uploader (Flask App)
====================================

This is a Python Flask web app to upload Excel files containing lead data 
and automatically push them to Zoho CRM's Leads module.

Features:
---------
- Upload `.xlsx` file via web browser
- Automatically fetch Zoho access token using refresh token
- Pushes each row to Zoho CRM
- Displays success/failure for each row after upload

Setup Instructions:
-------------------
1. Clone the repo
2. Create a `.env` file with the following:
   ZOHO_REFRESH_TOKEN=your_refresh_token
   ZOHO_CLIENT_ID=your_client_id
   ZOHO_CLIENT_SECRET=your_client_secret
3. Install requirements:
   pip install -r requirements.txt
4. Run the app:
   python app.py
5. Visit `http://localhost:5000` and upload your Excel file.

Excel Format:
-------------
- First_Name
- Last_Name
- Email
- Phone
- Description

Enjoy automating your lead uploads! 🚀
