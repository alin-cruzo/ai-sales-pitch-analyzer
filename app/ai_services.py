import os
import uuid
from dotenv import load_dotenv
from groq import Groq
from gtts import gTTS

# Load the secret API keys from your .env file
load_dotenv()

# Initialize our Groq client
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def transcribe_audio(file_path: str) -> str:
    """Takes an audio file and returns the text transcript using Groq's Whisper model."""
    with open(file_path, "rb") as audio_file:
        transcription = groq_client.audio.transcriptions.create(
            file=(file_path, audio_file.read()),
            model="whisper-large-v3",
        )
    return transcription.text

def analyze_pitch(transcript: str) -> str:
    """Analyzes the text transcript using Groq's Llama-3 model."""
    response = groq_client.chat.completions.create(
       model="llama-3.1-8b-instant", # The upgraded model!, # Super fast, open-source model, # Super fast, open-source model
        messages=[
            {
                "role": "system", 
                "content": "You are an expert sales manager and closing coach. Analyze the following sales pitch. Provide actionable feedback on their closing strategy, psychology, and tone. Keep the feedback concise, conversational, and under 3 paragraphs so it sounds natural when spoken aloud."
            },
            {"role": "user", "content": transcript}
        ]
    )
    return response.choices[0].message.content

def generate_audio_feedback(text: str) -> str:
    """Converts the AI feedback text into speech using Google TTS."""
    os.makedirs("saved_audio", exist_ok=True)
    
    file_name = f"feedback_{uuid.uuid4().hex}.mp3"
    file_path = os.path.join("saved_audio", file_name)

    # Generate the audio using gTTS (100% free, runs locally)
    tts = gTTS(text=text, lang='en', tld='com')
    tts.save(file_path)
            
    return file_path