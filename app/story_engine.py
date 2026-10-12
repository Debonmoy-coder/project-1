"""
Heritage Story Engine: Transforms historical content into:
1. Interactive Branching Stories
2. Immersive Dual-Host Audio Podcasts
3. Step-by-Step Guided Virtual Tours
4. Interactive Q&A with the Historical Chronicler
"""

from typing import Dict, Any, List, Optional

class StoryEngine:
    def __init__(self):
        pass

    def generate_interactive_story(
        self,
        title: str,
        transcription: str,
        era: str = "Historic Era",
        location: str = "Ancient Citadel",
        protagonist_role: str = "Court Chronicler"
    ) -> Dict[str, Any]:
        """Generates a branching interactive narrative from manuscript content."""
        clean_text = transcription[:300]

        return {
            "title": f"The Chronicles of {title}",
            "era": era,
            "setting": location,
            "protagonist": protagonist_role,
            "prologue": f"You stand at the crossroads of history. The dust of {era} settles around your sandals. You carry the newly inscribed parchment: '{clean_text}...'",
            "chapters": [
                {
                    "chapter_number": 1,
                    "title": "The Whispers of the Council",
                    "content": f"The royal chamber is lit by sesame oil lamps. Elders and generals debate the momentous declaration written upon the scroll. Every decision made tonight will echo through centuries.",
                    "choices": [
                        {
                            "id": "c1_a",
                            "text": "Present the royal scroll directly to the sovereign assembly, advocating for immediate peace.",
                            "consequence": "The elders are moved by the noble words. Scribes hurry to dispatch copies to frontier garrisons.",
                            "next_chapter": 2
                        },
                        {
                            "id": "c1_b",
                            "text": "Secretly consult the master artisan to engrave the decree upon the mountain bedrock before sunrise.",
                            "consequence": "The words are etched into granite, making them unalterable by changing court factions.",
                            "next_chapter": 2
                        }
                    ]
                },
                {
                    "chapter_number": 2,
                    "title": "The Test of Time",
                    "content": "Decades turn into centuries. Armies march and empires fade into dust, but travelers on the ancient highway still pause to read the inscription. The message has endured.",
                    "choices": [
                        {
                            "id": "c2_a",
                            "text": "Plant a banyan grove beside the monument to shelter future generations of seekers.",
                            "consequence": "The sanctuary flourishes into a renowned retreat for philosophers and travelers.",
                            "next_chapter": 3
                        },
                        {
                            "id": "c2_b",
                            "text": "Entrust a family of hereditary bards to sing the decree as a folk ballad.",
                            "consequence": "The song enters the oral memory of the land, sung across rivers and campfires.",
                            "next_chapter": 3
                        }
                    ]
                },
                {
                    "chapter_number": 3,
                    "title": "The Living Heritage",
                    "content": "Today, as modern historians decipher the ancient script, your legacy shines undimmed. The courage to preserve human dignity remains the truest monument.",
                    "choices": []
                }
            ]
        }

    def generate_podcast_script(
        self,
        title: str,
        transcription: str,
        era: str = "Ancient Period",
        host_names: List[str] = None
    ) -> Dict[str, Any]:
        """Generates a dynamic 2-host audio drama / podcast script."""
        hosts = host_names or ["The Chronicler", "The Explorer"]
        return {
            "title": f"Echoes in Stone: The Tale of {title}",
            "series": "The Heritage Chronicles Podcast",
            "duration_est": "3.5 mins",
            "hosts": hosts,
            "dialogue": [
                {
                    "speaker": hosts[0],
                    "cue": "[Sound of wind blowing across ancient stones, warm drone melody swells]",
                    "line": f"Welcome, travelers. Tonight we open an archival window into {era}. What you are about to hear is not legend—it is carved into history."
                },
                {
                    "speaker": hosts[1],
                    "cue": "[Sound of rustling archival parchment]",
                    "line": f"Look at this transcription before us: '{transcription[:180]}...' It carries the genuine voice of someone speaking to us across hundreds of years."
                },
                {
                    "speaker": hosts[0],
                    "cue": "[Bronze temple bell tolls gently in background]",
                    "line": "Notice how the words don't speak of cruelty or destruction. Instead, they command compassion, justice, and the dignity of the common human being."
                },
                {
                    "speaker": hosts[1],
                    "cue": "[Atmospheric flute notes rising]",
                    "line": "That is the miracle of Indian heritage. While dynasties collapsed, the core ethos—protecting nature, caring for the living, seeking truth—remained unbreakable."
                },
                {
                    "speaker": hosts[0],
                    "cue": "[Warm musical outro rises, fade out]",
                    "line": "Join us next time as we unearth more lost voices from the archives of the subcontinent. Until then, keep listening to the whispers of history."
                }
            ]
        }

    def generate_guided_tour(
        self,
        title: str,
        transcription: str,
        monument_name: str = "Historic Heritage Site",
        stops_count: int = 4
    ) -> Dict[str, Any]:
        """Generates an immersive audio walking tour."""
        return {
            "title": f"The Virtual Pilgrim: Guided Audio Walk through {monument_name}",
            "monument": monument_name,
            "stops_count": stops_count,
            "total_duration": "15 mins",
            "stops": [
                {
                    "stop_number": 1,
                    "name": "The Threshold of Time: Main Gateway",
                    "orientation": "Facing the weathered stone entrance lintel",
                    "narrative": f"Pause here at the stone threshold. Notice the monumental scale of the architecture designed to instill reverence in every approaching traveler.",
                    "audio_cue": "[Sound of temple birds and morning breeze]"
                },
                {
                    "stop_number": 2,
                    "name": "The Epigraphical Gallery: Words in Granite",
                    "orientation": "Along the sunlit southern wall",
                    "narrative": f"Here, engraved into the bedrock, lies the central inscription: '{transcription[:140]}...' Run your imagination over the curves of the ancient script.",
                    "audio_cue": "[Rhythmic chipping of a distant bronze chisel]"
                },
                {
                    "stop_number": 3,
                    "name": "The Pillar of Reflection: Inner Courtyard",
                    "orientation": "Center of the open pavilion under the sky",
                    "narrative": "Stand at the geographic heart of the monument. In ancient times, community meetings, theatrical performances, and philosophical debates took place right where you stand.",
                    "audio_cue": "[Murmur of a gentle crowd and acoustic tanpura]"
                },
                {
                    "stop_number": 4,
                    "name": "The Horizon Viewpoint: Sunset Bastion",
                    "orientation": "Looking westward toward the river and mountains",
                    "narrative": "As dusk gilds the stone with amber light, look across the landscape. The people who built this world are gone, but their spirit lives whenever we remember.",
                    "audio_cue": "[Deep evening bell chime slowly fading]"
                }
            ]
        }

    def answer_historical_query(
        self,
        query: str,
        context_title: str,
        transcription: str
    ) -> Dict[str, Any]:
        """Answers user queries in the persona of an erudite Heritage Chronicler."""
        q_lower = query.lower()
        
        # Determine focus of inquiry
        if any(w in q_lower for w in ["who", "king", "queen", "ruler", "person", "emperor"]):
            response = f"Regarding the leadership connected with '{context_title}': Historical records show this edict was commanded during a pivotal epoch of sovereign responsibility. Leaders of this period placed immense value on moral authority (Dharma/Neeti) over sheer coercive force."
        elif any(w in q_lower for w in ["script", "language", "alphabet", "write", "modi", "brahmi"]):
            response = f"The palaeographical style observed here reflects the linguistic evolution of the subcontinent. Ancient scribes mastered cursive flourishes to write swiftly upon palm leaves (Talapatra) or chiselled deep, uniform grooves on basalt to endure centuries of tropical monsoons."
        elif any(w in q_lower for w in ["why", "significance", "important", "purpose"]):
            response = f"The core purpose was public perpetuity. Unlike private court diaries, these proclamations were placed at busy crossroads, pilgrimage passes, and temple plinths so that soldiers, merchants, pilgrims, and foreign emissaries alike would know the ethical laws of the land."
        else:
            response = f"As chroniclers of this heritage, we observe that '{context_title}' represents a rare balance between political authority and profound humanism. The passage: '{transcription[:100]}...' reminds us that Indian history is not merely a record of battles, but of civilizational dialogue."

        return {
            "query": query,
            "chronicler_response": response,
            "persona": "Acharya Vidyadhar, Heritage Chronicler",
            "source_referenced": context_title
        }

story_engine = StoryEngine()
