import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(BASE_DIR / ".env")

class Settings:
    SARVAM_API_KEY: str = os.getenv("SARVAM_API_KEY", "")
    SARVAM_DEFAULT_VOICE: str = os.getenv("SARVAM_DEFAULT_VOICE", "shubh")
    SARVAM_TTS_MODEL: str = os.getenv("SARVAM_TTS_MODEL", "bulbul:v3")
    PORT: int = int(os.getenv("PORT", 8000))
    HOST: str = os.getenv("HOST", "127.0.0.1")

    # Sarvam Endpoints
    SARVAM_BASE_URL: str = "https://api.sarvam.ai"
    SARVAM_TRANSLATE_URL: str = "https://api.sarvam.ai/translate"
    SARVAM_TTS_URL: str = "https://api.sarvam.ai/text-to-speech"
    SARVAM_STT_URL: str = "https://api.sarvam.ai/speech-to-text"

    # Supported Indic & International Languages
    SUPPORTED_LANGUAGES = [
        {"code": "hi-IN", "name": "Hindi", "native": "हिन्दी"},
        {"code": "bn-IN", "name": "Bengali", "native": "বাংলা"},
        {"code": "ta-IN", "name": "Tamil", "native": "தமிழ்"},
        {"code": "te-IN", "name": "Telugu", "native": "తెలుగు"},
        {"code": "mr-IN", "name": "Marathi", "native": "मराठी"},
        {"code": "gu-IN", "name": "Gujarati", "native": "ગુજરાતી"},
        {"code": "kn-IN", "name": "Kannada", "native": "ಕನ್ನಡ"},
        {"code": "ml-IN", "name": "Malayalam", "native": "മലയാളം"},
        {"code": "pa-IN", "name": "Punjabi", "native": "ਪੰਜਾਬੀ"},
        {"code": "od-IN", "name": "Odia", "native": "ଓଡ଼ିଆ"},
        {"code": "en-IN", "name": "English (India)", "native": "English (India)"},
    ]

    # Voice Catalog for Sarvam Bulbul TTS
    VOICE_CATALOG = [
        {"id": "shubh", "name": "Shubh", "gender": "Male", "accent": "Hindi / North Indian", "description": "Solemn, resonant, royal chronicler tone"},
        {"id": "ratan", "name": "Ratan", "gender": "Male", "accent": "Elder Sage", "description": "Deep, weathered, ancient oral storyteller"},
        {"id": "kavitha", "name": "Kavitha", "gender": "Female", "accent": "South Indian / Tamil", "description": "Melodic, graceful, temple bard tone"},
        {"id": "priya", "name": "Priya", "gender": "Female", "accent": "Modern Indian", "description": "Engaging, crisp podcast host voice"},
        {"id": "arvind", "name": "Arvind", "gender": "Male", "accent": "Classical", "description": "Commanding, epic narration style"},
        {"id": "aditya", "name": "Aditya", "gender": "Male", "accent": "Youthful Historian", "description": "Lively, curious, expedition guide"},
        {"id": "roopa", "name": "Roopa", "gender": "Female", "accent": "Warm Matriarch", "description": "Intimate, folklore transmitter voice"},
        {"id": "shreya", "name": "Shreya", "gender": "Female", "accent": "Poetic", "description": "Lyrical, emotive storytelling style"},
    ]

    # Ambient Soundscapes
    SOUNDSCAPES = [
        {"id": "none", "name": "Silence (Voice Only)", "icon": "volume-x"},
        {"id": "temple_drone", "name": "Sacred Temple Bells & Tanpura", "icon": "bell"},
        {"id": "royal_court", "name": "Maratha Darbar & Sitar Chords", "icon": "crown"},
        {"id": "monsoon_library", "name": "Monsoon Rain on Palm Leaves", "icon": "cloud-rain"},
        {"id": "ancient_caravan", "name": "Desert Caravan & Night Wind", "icon": "compass"},
        {"id": "battlefield_echoes", "name": "Distant War Drums & Campfire", "icon": "flame"},
    ]

settings = Settings()
