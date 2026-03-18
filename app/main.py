import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Import your custom AI logic from your ai_services.py file
import ai_services

app = FastAPI(title="AI Sales Pitch Coach API")

# ==========================================
# 1. SECURITY (CORS FIX)
# This allows your GitHub Pages site to talk to this Render server
# ==========================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all websites (like your GitHub Pages) to connect
    allow_credentials=True,
    allow_methods=["*"],  # Allows POST, GET, etc.
    allow_headers=["*"],  # Allows all headers
)

# ==========================================
# 2. STATIC FILES (AUDIO FOLDER)
# This allows the frontend to access and play the saved feedback audio
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
async def analyze_pitch(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded.")

    temp_file_path = f"temp_{file.filename}"
    
    try:
        # Step A: Save the user's uploaded audio file temporarily
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Step B: AI Processing
        # (Note: Ensure these function names match exactly what you wrote in ai_services.py!)
        
        # 1. Transcribe audio to text (Groq Whisper)
        transcript = ai_services.transcribe_audio(temp_file_path)
        
        # 2. Get coaching feedback (Groq Llama 3)
        feedback = ai_services.analyze_pitch_text(transcript)
        
        # 3. Turn feedback into speech (ElevenLabs/gTTS)
        audio_filename = f"feedback_{file.filename}.mp3"
        audio_file_path = os.path.join(AUDIO_DIR, audio_filename)
        ai_services.generate_audio(feedback, audio_file_path)

        # Step C: Send the results back to the website
        return {
            "transcript": transcript,
            "feedback": feedback,
            "audio_path": f"/saved_audio/{audio_filename}"
        }

    except Exception as e:
        print(f"Server Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
        
    finally:
        # Step D: Delete the temporary uploaded file to keep the server clean
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)