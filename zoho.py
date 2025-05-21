import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_access_token():
    url = "https://accounts.zoho.in/oauth/v2/token"
    params = {
        "refresh_token": os.getenv("ZOHO_REFRESH_TOKEN"),
        "client_id": os.getenv("ZOHO_CLIENT_ID"),
        "client_secret": os.getenv("ZOHO_CLIENT_SECRET"),
        "grant_type": "refresh_token"
    }

    resp = requests.post(url, params=params)
    resp.raise_for_status()
    return resp.json().get("access_token")

def push_to_zoho_crm(token, row):
    url = "https://www.zohoapis.in/crm/v2/Leads"
    headers = {
        "Authorization": f"Zoho-oauthtoken {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "data": [{
            "Last_Name": row.get("Last_Name", "Unknown"),
            "First_Name": row.get("First_Name", ""),
            "Email": row.get("Email", ""),
            "Phone": row.get("Phone", ""),
            "Description": row.get("Description", "")
        }]
    }

    resp = requests.post(url, json=payload, headers=headers)
    return resp.status_code == 201
