import pandas as pd
import requests

# Replace these with your actual values
vapi_base_url = "https://api.vapi.ai/call/phone" # Base URL for VAPI
phone_number_id = "ADD YOUR VAPI PHONE NUMBER ID HERE"  # Phone number ID from VAPI
assistant_id = "ADD YOUR VAPI ASSISTANT ID HERE"    # Assistant ID from VAPI
api_key = "ADD YOUR VAPI API KEY HERE" # API Key from VAPI
server_url = "ENTER YOUR SERVER URL HERE FOR FUNCTIONS" # Server URL for functions Make.com or zapier

# Load the leads from a CSV file
leads_csv_path = "numbers.csv"  # Path to your CSV file
leads_df = pd.read_csv(leads_csv_path)


# Function to place a call
def place_call(lead_name, lead_number):
    url = vapi_base_url
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "assistantId": assistant_id,
        "customer": {
            "name": lead_name,
            "number": lead_number
        },
        "phoneNumberId": phone_number_id,
        "type": "outboundPhoneCall",
        "assistant": {
            "voice": {
                "provider": "deepgram", # Voice provider
                "voiceId": "athena" # Voice ID
            },
            "transcriber": {
            "provider": "deepgram", # Transcriber provider
            "keywords": ["Nova:1", "Phonecall:1"] # Keywords for transcriber
            },
            "model": {
                "provider": "openai", # Model provider
                "model": "gpt-4", # Model ID
                "functions": [
                    {
                        "name": "bookAppointment",
                        "description": "Books an appointment with client details.",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "Name": {"type": "string"},
                                "PhoneNumber": {"type": "string"},
                                "EmailAddress": {"type": "string"},
                                "PreferredDateTime": {"type": "string"}
                            },
                            "required": ["Name", "PhoneNumber", "EmailAddress", "PreferredDateTime"]
                        },
                        "serverUrl": server_url
                    }
                ],
                "messages": [
                    {
                        "role": "system",
                        "content": "You're a sales agent for Bicky Realty. You're calling a list of leads to schedule appointments to show them houses..."
                    }
                ]
            },
            "firstMessage": "Hi, this is Jennifer from Bicky Realty. We're calling to schedule an appointment to show you a house. When would be a good time for you?",
            "endCallMessage": "Thanks for your time.",
            "endCallFunctionEnabled": True,
            "recordingEnabled": False
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print(f"Call initiated to {lead_name} at {lead_number}.")
    else:
        print(f"Failed to initiate call to {lead_name}. Status code: {response.status_code}, Response: {response.text}")

# Place calls to all leads
for index, row in leads_df.iterrows():
    place_call(row['Name'], row['Number'])

