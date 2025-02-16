from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
import base64
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Ensure you have a "templates" folder

decoded_message = "Hi all"

@app.post("/")
async def home(request: Request):
    global decoded_message
    try:
        envelope = await request.json()
        if not envelope:
            raise HTTPException(status_code=400, detail="Bad Request: No JSON body received")

        if "message" not in envelope:
            raise HTTPException(status_code=400, detail="Bad Request: No message field in JSON")

        pubsub_message = envelope["message"]

        if "data" in pubsub_message:
            message_data = pubsub_message["data"]
            decoded_message = base64.b64decode(message_data).decode("utf-8")

        return {"detail": "Message received and processed."}
    except Exception as e:
        print(f"Error processing the message: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/")
async def redirect_to_about():
    return RedirectResponse(url="/about")

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    global decoded_message
    return templates.TemplateResponse("message.html", {"request": request, "message": decoded_message})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
