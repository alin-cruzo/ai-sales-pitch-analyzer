from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import shutil
from app.ai_services import transcribe_audio, analyze_pitch, generate_audio_feedback

app = FastAPI(title="AI Sales Pitch Analyzer")

# 1. ALLOW WEB BROWSERS TO TALK TO YOUR API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows any frontend to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. ALLOW THE BROWSER TO PLAY YOUR SAVED AUDIO FILES
os.makedirs("saved_audio", exist_ok=True)
app.mount("/saved_audio", StaticFiles(directory="saved_audio"), name="saved_audio")

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Sales Pitch Analyzer API"}

@app.post("/api/v1/analyze-pitch")
async def analyze_sales_pitch(file: UploadFile = File(...)):
    try:
        # 1. Save the uploaded file temporarily
        temp_file_path = f"temp_{file.filename}"
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 2. Transcribe the audio
        transcript = transcribe_audio(temp_file_path)

        # 3. Analyze the pitch
        feedback = analyze_pitch(transcript)

        # 4. Generate audio feedback
        audio_file_path = generate_audio_feedback(feedback)

        # Clean up temp file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

        return {
            "message": "Pitch analyzed successfully!",
            "transcript": transcript,
            "feedback_text": feedback,
            "feedback_audio_url": f"/{audio_file_path}"
        }

    except Exception as e:
        # Clean up temp file even if there is an error
        if 'temp_file_path' in locals() and os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        raise HTTPException(status_code=500, detail=str(e))