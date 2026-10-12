import base64
from typing import Dict, Any, Optional, List
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from pydantic import BaseModel

from app.config import settings
from app.sarvam_client import sarvam_client
from app.manuscript_ocr import manuscript_engine
from app.story_engine import story_engine
from app.audio_mixer import audio_mixer
from app.vault_data import HERITAGE_VAULT

router = APIRouter(prefix="/api")

# Pydantic Schemas
class TranslateRequest(BaseModel):
    text: str
    source_language: str = "auto"
    target_language: str = "hi-IN"
    mode: str = "formal"

class NarrationRequest(BaseModel):
    text: str
    language_code: str = "hi-IN"
    speaker: str = "shubh"
    pace: float = 1.0
    model: str = "bulbul:v3"
    soundscape: str = "temple_drone"

class StoryTransformRequest(BaseModel):
    title: str
    transcription: str
    era: Optional[str] = "Ancient Period"
    mode: str = "interactive_story"  # interactive_story | podcast | guided_tour
    extra_context: Optional[str] = None

class ChatRequest(BaseModel):
    query: str
    context_title: str
    transcription: str

class KeyUpdateRequest(BaseModel):
    api_key: str

# -------------------------------------------------------------
# Endpoints
# -------------------------------------------------------------

@router.get("/status")
def get_system_status():
    """Returns system status, active Sarvam API key quota check, and catalogs."""
    health = sarvam_client.check_health_and_quota()
    return {
        "status": "online",
        "sarvam_status": health,
        "supported_languages": settings.SUPPORTED_LANGUAGES,
        "voice_catalog": settings.VOICE_CATALOG,
        "soundscapes": settings.SOUNDSCAPES,
        "current_key_preview": f"{sarvam_client.api_key[:6]}...{sarvam_client.api_key[-4:]}" if sarvam_client.api_key else "None"
    }

@router.post("/settings/key")
def update_api_key(req: KeyUpdateRequest):
    """Updates the in-memory Sarvam API key and verifies it."""
    sarvam_client.update_key(req.api_key)
    health = sarvam_client.check_health_and_quota()
    return {
        "status": "updated",
        "health": health
    }

@router.get("/vault")
def get_vault_catalog():
    """Returns curated historical manuscripts and oral archives in the Heritage Vault."""
    catalog = []
    for item in HERITAGE_VAULT:
        catalog.append({
            "id": item["id"],
            "title": item["title"],
            "origin": item["origin"],
            "era": item["era"],
            "script": item["script"],
            "original_language": item["original_language"],
            "category": item["category"],
            "image_url": item["image_url"],
            "summary": item["summary"]
        })
    return {"vault": catalog}

@router.get("/vault/{archive_id}")
def get_vault_item(archive_id: str):
    """Returns full details, authentic scripts, and pre-generated stories for a specific archive."""
    for item in HERITAGE_VAULT:
        if item["id"] == archive_id:
            return item
    raise HTTPException(status_code=404, detail="Archive item not found in Heritage Vault")

@router.post("/transcribe/manuscript")
async def transcribe_manuscript(
    file: Optional[UploadFile] = File(None),
    raw_text: Optional[str] = Form(None),
    title: Optional[str] = Form(None)
):
    """Transcribes an uploaded manuscript image or archival text."""
    if file:
        content = await file.read()
        res = manuscript_engine.process_image(content, filename=file.filename or "manuscript.png")
        return {"status": "success", "result": res}
    elif raw_text:
        res = manuscript_engine.process_raw_text(raw_text, title=title)
        return {"status": "success", "result": res}
    else:
        raise HTTPException(status_code=400, detail="Provide an image file or raw text to transcribe")

@router.post("/transcribe/audio")
async def transcribe_oral_archive(
    file: UploadFile = File(...),
    prompt: Optional[str] = Form("Historical oral archive recording")
):
    """Transcribes oral archive audio using Sarvam Saaras STT."""
    audio_bytes = await file.read()
    res = sarvam_client.speech_to_text(audio_bytes, filename=file.filename or "oral_recording.wav", prompt=prompt)
    return res

@router.post("/translate")
def translate_content(req: TranslateRequest):
    """Translates text across Indic languages using Sarvam Mayura Translation API."""
    res = sarvam_client.translate(
        text=req.text,
        source_lang=req.source_language,
        target_lang=req.target_language,
        mode=req.mode
    )
    return res

@router.post("/story/transform")
def transform_to_story(req: StoryTransformRequest):
    """Transforms raw historical content into an Interactive Story, Podcast, or Tour."""
    if req.mode == "interactive_story":
        res = story_engine.generate_interactive_story(
            title=req.title,
            transcription=req.transcription,
            era=req.era or "Ancient Period",
            location=req.extra_context or "Historic Citadel"
        )
    elif req.mode == "podcast":
        res = story_engine.generate_podcast_script(
            title=req.title,
            transcription=req.transcription,
            era=req.era or "Ancient Period"
        )
    elif req.mode == "guided_tour":
        res = story_engine.generate_guided_tour(
            title=req.title,
            transcription=req.transcription,
            monument_name=req.title
        )
    else:
        raise HTTPException(status_code=400, detail="Invalid mode. Choose interactive_story, podcast, or guided_tour")
    
    return {"status": "success", "mode": req.mode, "content": res}

@router.post("/narration/generate")
def generate_narration(req: NarrationRequest):
    """Generates natural multilingual voice narration using Sarvam Bulbul TTS + soundscape mixer."""
    # Call Sarvam TTS
    tts_result = sarvam_client.text_to_speech(
        text=req.text,
        language_code=req.language_code,
        speaker=req.speaker,
        pace=req.pace,
        model=req.model
    )

    # Attach ambient soundscape metadata
    soundscape_meta = audio_mixer.get_soundscape_meta(req.soundscape)
    tts_result["soundscape"] = req.soundscape
    tts_result["soundscape_meta"] = soundscape_meta

    return tts_result

@router.post("/chat")
def chat_heritage_scholar(req: ChatRequest):
    """Interactive dialogue with the Heritage Chronicler persona."""
    return story_engine.answer_historical_query(
        query=req.query,
        context_title=req.context_title,
        transcription=req.transcription
    )
