from fastapi import FastAPI, Request
import uvicorn
import json
from datetime import datetime

app = FastAPI()

@app.post("/vapi/")
async def receive_message(request: Request):
    raw_body = await request.body()
    message = json.loads(raw_body)
    messages = message.get("message", {}).get("messages", [])
    
    if messages:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"messages_{timestamp}.json"
        with open(filename, "w") as file:
            json.dump(messages, file, indent=4)
        return {"message": "Messages received and saved."}
    else:
        return {"message": "No messages found in the request."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
