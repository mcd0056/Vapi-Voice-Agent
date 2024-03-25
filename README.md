## FastAPI Server for Handling VAPI Messages
This FastAPI server is designed to receive messages from the VAPI (Voice API) platform and save them as JSON files. It's a simple webhook endpoint that can be used for logging or further processing of incoming calls and messages.

# Setup
Setup Enviroment

- python -m venv venv
- venv\Scripts\Activate

# Install Requirements:
- pip install -r requirements.txt

# Start the Server:
- uvicorn main:app --reload
This command starts the FastAPI server on port 8000, accessible from any machine.

# Expose with Ngrok:
First, download and install ngrok.
Run ngrok to expose port 8000:
- ngrok http 8000

Ngrok will provide a URL (e.g., https://abc123.ngrok.io) that forwards to your local server. Use this URL as the endpoint for VAPI or other services to send requests.

# Endpoint
POST /vapi/: Receives and logs messages from VAPI.
Ensure your VAPI configuration or external service is set to POST messages to https://<ngrok_url>/vapi/.

## VAPI Outbound Call Script
This script utilizes the VAPI platform to make outbound sales calls using leads from a CSV file. It sets up calls with a custom assistant configured to handle various tasks, such as booking appointments.

## Add leads to CSV file
- Add Name and Number to numbers.csv
- Call each lead

# Variables Required 
phone_number_id: Your VAPI phone number ID.
assistant_id: Your VAPI assistant ID.
api_key: Your VAPI API key.
server_url: Your server URL for handling function calls with the agent

# Run the Script
- python outbound.py
