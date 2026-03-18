# 🎙️ AI Sales Pitch Analyzer

A full-stack AI application designed to evaluate and elevate sales pitches. This tool allows users to upload audio recordings of their sales calls and receive instant, actionable coaching on their closing strategy, tone, and the underlying psychology of the conversation.

## ✨ Features

* **Lightning-Fast Transcription:** Uses Groq's Whisper model to convert raw audio pitches (including filler words and pauses) into highly accurate text transcripts.
* **Strategic AI Coaching:** Leverages the Groq Llama 3.1 model to act as an expert sales manager, analyzing the transcript and providing targeted feedback on negotiation tactics and tone.
* **Interactive Audio Feedback:** Converts the AI's coaching advice into spoken audio using Google TTS (at an optimized 1.25x playback speed) for a natural, conversational review experience.
* **Modern Web Interface:** A clean, responsive frontend built with Tailwind CSS and vanilla JavaScript for seamless audio uploading and result visualization.

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI
* **AI & LLMs:** Groq API (Whisper-large-v3, Llama-3.1-8b-instant)
* **Audio Processing:** gTTS (Google Text-to-Speech), `python-multipart`
* **Frontend:** HTML5, JavaScript, Tailwind CSS

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/alincruzo9122-max/ai-sales-pitch-analyzer.git](https://github.com/alincruzo9122-max/ai-sales-pitch-analyzer.git)
cd ai-sales-pitch-analyzer