"""
Audio Mixer and Soundscape Engine
Controls atmospheric ambient layers, audio pacing,
and Web Audio soundscape parameters.
"""

from typing import Dict, Any, List
from app.config import settings

class AudioMixerEngine:
    def __init__(self):
        self.soundscapes = {
            "temple_drone": {
                "name": "Sacred Temple Bells & Tanpura",
                "frequencies": [432.0, 648.0, 216.0],
                "bell_intervals_sec": [0.0, 4.0, 9.0],
                "reverb_decay": 3.5,
                "recommended_for": ["Ancient Inscriptions", "Brahmi Edicts", "Chola Epigraphs"]
            },
            "royal_court": {
                "name": "Maratha Darbar & Sitar Chords",
                "frequencies": [293.66, 440.0, 587.33],
                "drone_type": "sitar_buzz",
                "reverb_decay": 2.2,
                "recommended_for": ["Royal Decrees", "Modi Script", "Court Chronicles"]
            },
            "monsoon_library": {
                "name": "Monsoon Rain on Palm Leaves",
                "white_noise_filter": "lowpass_800hz",
                "drop_cadence": "gentle",
                "reverb_decay": 1.5,
                "recommended_for": ["Oral Ballads", "Baul Songs", "Archival Reading"]
            },
            "ancient_caravan": {
                "name": "Desert Caravan & Night Wind",
                "frequencies": [196.0, 293.66],
                "wind_noise": True,
                "reverb_decay": 4.0,
                "recommended_for": ["Trade Routes", "Silk Road Records", "Border Edicts"]
            },
            "battlefield_echoes": {
                "name": "Distant War Drums & Campfire",
                "drum_bpm": 60,
                "fire_crackle": True,
                "reverb_decay": 2.8,
                "recommended_for": ["1857 Uprising", "Siege Letters", "Hero Stones"]
            }
        }

    def get_soundscape_presets(self) -> List[Dict[str, Any]]:
        return settings.SOUNDSCAPES

    def get_soundscape_meta(self, soundscape_id: str) -> Dict[str, Any]:
        return self.soundscapes.get(soundscape_id, {})

audio_mixer = AudioMixerEngine()
