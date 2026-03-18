import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Tell Render exactly where to find your AI logic file
from app import ai_services

app = FastAPI(title="AI Sales Pitch Coach API")

# ==========================================
# 1. SECURITY (CORS FIX)
# Allows your GitHub Pages site to talk to this Render server
# ==========================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# 2. STATIC FILES (AUDIO FOLDER)
# Allows the frontend to access and play the saved feedback audio
# ==========================================
AUDIO_DIR = "saved_audio"
os.makedirs(AUDIO_DIR, exist_ok=True)
app.mount("/saved_audio", StaticFiles(directory=AUDIO_DIR), name="saved_audio")

# ==========================================
# 3. API ENDPOINTS
# ==========================================

@app.get("/")
def read_root():
    return {"status": "Live", "message": "AI Sales Pitch Analyzer Backend is running!"}

@app.post("/analyze-pitch")
async def analyze_pitch_endpoint(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded.")

    temp_file_path = f"temp_{file.filename}"
    
    try:
        # Step A: Save the user's uploaded audio file temporarily
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Step B: AI Processing (Fully synced with ai_services.py)
        
        # 1. Transcribe audio to text (Groq Whisper)
        transcript = ai_services.transcribe_audio(temp_file_path)
        
        # 2. Get coaching feedback (Groq Llama 3)
        feedback = ai_services.analyze_pitch(transcript)
        
        # 3. Turn feedback into speech (Google TTS)
        # Your function saves the file and returns the path (e.g., "saved_audio/feedback_123.mp3")
        saved_audio_path = ai_services.generate_audio_feedback(feedback)
        
        # Extract just the filename so we can send the correct URL to the frontend
        audio_filename = os.path.basename(saved_audio_path)

        # Step C: Send the results back to the website
        return {
            "transcript": transcript,
            "feedback": feedback,
            "audio_path": f"/saved_audio/{audio_filename}"
        }

    except Exception as e:
        print