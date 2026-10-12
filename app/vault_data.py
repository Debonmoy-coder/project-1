"""
Heritage Vault: Curated Historical Archives & Oral Traditions
Contains authentic transcriptions, paleographical context, multi-lingual translations,
and pre-designed interactive stories, podcasts, and guided tours.
"""

HERITAGE_VAULT = [
    {
        "id": "ashoka_girnar",
        "title": "Major Rock Edict of Emperor Ashoka",
        "origin": "Girnar Rock, Junagadh, Gujarat",
        "era": "c. 257 BCE (Maurya Empire)",
        "script": "Brahmi Script",
        "original_language": "Prakrit (Girnar Dialect)",
        "category": "Imperial Inscription",
        "image_url": "https://images.unsplash.com/photo-1599837565318-67429bde7162?auto=format&fit=crop&w=800&q=80",
        "summary": "King Devanampriya Priyadarsin (Ashoka) decrees that all living beings deserve non-injury, compassion, and medicinal care across all borders, even in kingdoms beyond.",
        "original_script_text": "𑀤𑁂𑀯𑀸𑀦𑀁𑀧𑀺𑀬𑁂𑀦 𑀧𑀺𑀬𑀤𑀲𑀺𑀦𑀸 𑀭𑀸𑨓𑀸 𑀤𑁂𑀲𑁂𑀲𑀼 𑀲𑀯𑀢𑀸 𑀥𑀁𑀫𑀮𑀺𑀧𑀺 𑀮𑀺𑀔𑀸𑀧𑀺𑀢𑀸 ... 𑀲𑀭𑁆𑀯𑀢𑁆𑀭 𑀯𑀺𑀚𑀺𑀢𑁂𑀱𑀼 𑀤𑁂𑀯𑀸𑀦𑀸𑀫𑁆𑀧𑁆𑀭𑀺𑀬𑀲𑁆𑀬 𑀫𑀦𑀼𑀱𑁆𑀬-𑀘𑀺𑀓𑀺𑀢𑁆𑀲𑀸 𑀘 𑀧𑀰𑀼-𑀘𑀺𑀓𑀺𑀢𑁆𑀲𑀸 𑀘 𑀓𑀢𑀸।",
        "transliteration": "Devanampiyena Piyadasina ranya desesu savata dhammalipi likhapita... Sarvatra vijiteshu Devanampriyasya manushya-chikitsa cha pashu-chikitsa cha kata.",
        "archaic_glossary": [
            {"term": "Devanampriya", "meaning": "Beloved of the Gods - royal honorific title assumed by Ashoka"},
            {"term": "Dhamma", "meaning": "Cosmic and moral law; ethical righteousness and compassion towards all beings"},
            {"term": "Chikitsa", "meaning": "Medicinal and herbal botanical gardens established for humans and beasts"}
        ],
        "default_translations": {
            "en-IN": "King Devanampriya Priyadarsin caused this sacred edict to be inscribed upon the stone. Everywhere within his dominions, two kinds of medical treatment have been established: medical treatment for men and medical treatment for animals. Medicinal herbs suitable for men and beasts, wherever they are not found, have been imported and planted.",
            "hi-IN": "देवानांप्रिय प्रियदर्शी राजा ने अपने संपूर्ण साम्राज्य में इस धम्मलिपि को उत्कीर्ण कराया। उनके समस्त राज्य में दो प्रकार की चिकित्सा व्यवस्थाएं स्थापित की गईं—मनुष्यों के लिए चिकित्सा और पशुओं के लिए चिकित्सा। जहां औषधीय वनस्पतियां उपलब्ध नहीं थीं, वहां उन्हें दूर-दूर से मंगाकर रोपित कराया गया।",
            "bn-IN": "দেবনামপ্রিয় প্রিয়দর্শী রাজা তাঁর সমগ্র সাম্রাজ্যে এই ধর্মলিপি খোদাই করালেন। তাঁর সমস্ত রাজ্যে দুই ধরণের চিকিৎসা ব্যবস্থা প্রতিষ্ঠিত হয়েছে—মানুষের চিকিৎসা এবং পশুদের চিকিৎসা। যেখানে ঔষধি ভেষজ পাওয়া যেত না, সেখানে দূরদেশ থেকে এনে রোপণ করা হয়েছে।",
            "ta-IN": "தேவானாம்பிரிய பிரியதர்சி மன்னர் தமது பேரரசு முழுவதும் இந்த தர்ம சாசனத்தை கல்லில் செதுக்கச் செய்தார். மனிதர்களுக்கான மருத்துவம் மற்றும் விலங்குகளுக்கான மருத்துவம் என இருவகை மருத்துவ வசதிகள் உருவாக்கப்பட்டுள்ளன.",
            "mr-IN": "देवानांप्रिय प्रियदर्शी राजाने आपल्या संपूर्ण साम्राज्यात ही धम्मलिपी पाषाणावर कोरून घेतली. मनुष्यांसाठी आणि पशूंसाठी औषधोपचारांची व्यवस्था करण्यात आली आहे."
        },
        "interactive_story": {
            "title": "The Stonecutter of Girnar",
            "prologue": "It is the monsoon of 257 BCE. You are Vishva, a master lapidary summoned to the sacred granite mountain of Girnar by the royal emissary of Pataliputra.",
            "chapters": [
                {
                    "chapter_number": 1,
                    "title": "The Imperial Seal",
                    "content": "The imperial scroll arrives bound with purple silk and the seal of the Mauryan Peacock. The emissary unrolls the parchment: 'His Majesty renounces the slaughter of war. You must carve his words into the enduring granite so that our grandchildren shall see peace.' You gaze at the jagged cliff face.",
                    "choices": [
                        {
                            "text": "Begin chiseling on the eastern face where the morning sun strikes the cliff.",
                            "next_hint": "The eastern cliff catches the pilgrimage route from Saurashtra."
                        },
                        {
                            "text": "Carve deep grooves near the ancient water reservoir of Sudarshana Lake.",
                            "next_hint": "Travelers and farmers watering their herds will read the message daily."
                        }
                    ]
                },
                {
                    "chapter_number": 2,
                    "title": "Words that Outlive Empires",
                    "content": "For eighteen months, your bronze hammers ring against the porphyry granite. As dust coats your skin, the Brahmi glyphs appear like sacred constellations: 'Everywhere, compassion for animals; medicinal roots planted for all travelers.' An envoy from the southern kingdoms arrives, bowing before the rock.",
                    "choices": [
                        {
                            "text": "Offer herbal roots from the newly planted royal nursery to the travelers.",
                            "next_hint": "A living demonstration of the edict in action."
                        },
                        {
                            "text": "Seal the stone with natural lacquer to withstand two thousand monsoons.",
                            "next_hint": "Ensuring the edict survives into the twenty-first century."
                        }
                    ]
                }
            ]
        },
        "podcast_script": {
            "title": "Echoes of Girnar: When an Emperor Laid Down His Sword",
            "duration": "4 mins",
            "speakers": ["Chronicler", "Historian"],
            "dialogue": [
                {"speaker": "Chronicler", "cue": "[Sound of chisel striking ancient granite, wind howling over hills]", "line": "High above the plains of Gujarat, upon a massive dark boulder of Girnar, lies a message written more than twenty-two hundred years ago."},
                {"speaker": "Historian", "cue": "[Subtle drone of ancient flute]", "line": "It was carved not to boast of bloody conquests or sacked cities, but to announce something radical: that a sovereign emperor was commanding free medicine for all animals and humans."},
                {"speaker": "Chronicler", "cue": "[Sound of rustling palm leaves]", "line": "Look closely at the Brahmi letters. The script seems simple, but its courage was monumental. Ashoka had seen the carnage of Kalinga and decided that true conquest is Dhamma-Vijaya—the victory of righteousness."},
                {"speaker": "Historian", "cue": "[Temple bell chimes gently]", "line": "Even today, standing before the Girnar rock, you can touch the indentations where the chisel fell in 257 BCE. History is not distant; it breathes beneath your fingertips."}
            ]
        },
        "guided_tour": {
            "title": "Walking with Ashoka: The Girnar Rock Sanctuary",
            "total_stops": 4,
            "stops": [
                {
                    "stop_number": 1,
                    "name": "The Foothills of Mount Girnar",
                    "orientation": "Facing East towards the rising Saurashtra ridge",
                    "narrative": "Welcome to the base of Junagadh's ancient mountain. Here, travelers on ancient trade routes paused to drink water before beginning the grueling ascent.",
                    "audio_hook": "Listen closely to the gentle rustle of deciduous teak forest."
                },
                {
                    "stop_number": 2,
                    "name": "The Great Basalt Boulder",
                    "orientation": "Inside the stone sanctuary pavilion",
                    "narrative": "Before you stands a massive granite-basalt outcrop, 12 feet high and 75 feet in circumference. On this single rock, three great dynasties left their voices: Ashoka, Rudradaman, and Skandagupta.",
                    "audio_hook": "Notice how the stone was smoothed with river sand before the Brahmi scribes applied ink guides."
                },
                {
                    "stop_number": 3,
                    "name": "The Edict of Compassion (Rock Edict II)",
                    "orientation": "Upper-left quadrant of the boulder face",
                    "narrative": "Trace your eyes along the second sector. Here Ashoka proclaims botanical expeditions: sending physicians to gather medicinal barks and roots for both humans and beasts across kingdoms.",
                    "audio_hook": "This marks the world's earliest recorded state-sponsored veterinary health system."
                },
                {
                    "stop_number": 4,
                    "name": "Sudarshana Lake Overlook",
                    "orientation": "Looking westward toward the ancient earthen dam site",
                    "narrative": "Just below this rock lay Lake Sudarshana, commissioned by Chandragupta Maurya and repaired across five centuries. An oasis of water engineered for dry Saurashtra.",
                    "audio_hook": "Gaze across the valley where Mauryan engineers harnessed the mountain torrents."
                }
            ]
        }
    },
    {
        "id": "shivaji_farman_1674",
        "title": "Royal Edict of Chhatrapati Shivaji Maharaj",
        "origin": "Raigad Fort, Western Ghats, Maharashtra",
        "era": "c. 1674 CE (Coronation Period)",
        "script": "Modi Script (मोडी लिपी)",
        "original_language": "Marathi",
        "category": "Royal Decree & Administrative Farman",
        "image_url": "https://images.unsplash.com/photo-1590076215667-875d4ef2d7ee?auto=format&fit=crop&w=800&q=80",
        "summary": "Chhatrapati Shivaji Maharaj writes to his military commanders commanding absolute discipline: no soldier shall seize grain, wood, or vegetables from the peasant farmers without fair payment.",
        "original_script_text": "श्री राजा शिवछत्रपती यांच्या आज्ञेवरून... लष्करातील सैनिकांनी रयतेच्या भाजीच्या देठासही हात लावू नये. रयतेवर कसलाही जुलूम-जबरदस्ती न होता त्यांना अभय दिले पाहिजे. शेतकऱ्यांच्या धान्याची नासाडी झाल्यास कठोर शासन केले जाईल.",
        "transliteration": "Shri Raja Shivachhatrapati yanchya aagnyene... Lashkaratil sainikani rayatechya bhajichya dethasahi haat laavu naye. Rayatevar kaslahi julum-jabardasti na hota tyanna abhay dile pahije.",
        "archaic_glossary": [
            {"term": "Rayat", "meaning": "The peasantry, farmers, and common people of the land"},
            {"term": "Bhajichya Detha", "meaning": "Even the stalk of a vegetable; metaphor for zero extortion from civilians"},
            {"term": "Abhay", "meaning": "Absolute sanctuary, protection from fear and oppression"}
        ],
        "default_translations": {
            "en-IN": "By the royal command of Shri Raja Shivachhatrapati: Soldiers of the army must not touch even a stalk of vegetable belonging to the ryot (common people). No oppression or coercion shall be inflicted upon the peasantry; they must be granted fearless protection. If the farmers' harvest is ruined, severe punishment shall follow.",
            "hi-IN": "श्री राजा शिवछत्रपति की आज्ञा से: सेना के किसी भी सिपाही को रैयत (किसानों) की भाजी के डंठल को भी हाथ नहीं लगाना चाहिए। प्रजा पर किसी भी प्रकार का अत्याचार न हो, उन्हें निर्भय संरक्षण प्रदान किया जाए। यदि अन्न और फसल को नुकसान पहुंचाया गया, तो कठोर दंड दिया जाएगा।",
            "bn-IN": "শ্রী রাজা শিবছত্রপতির আদেশে: সেনাবাহিনীর কোনো সৈন্য যেন প্রজাদের শাকসবজির ডাঁটাতেও হাত না দেয়। কৃষকদের ওপর কোনো প্রকার অত্যাচার না করে তাদের অভয় দিতে হবে। কৃষকদের শস্য নষ্ট হলে কঠোর শাস্তি দেওয়া হবে।",
            "ta-IN": "ஸ்ரீ ராஜா சிவ சத்ரபதியின் ஆணைப்படி: இராணுவ வீரர்கள் எளிய மக்களின் ஒரு காய்கறித் தண்டைக்கூட அத்துமீறி தொடக்கூடாது. மக்களுக்கு முழுமையான பாதுகாப்பு வழங்கப்பட வேண்டும்.",
            "mr-IN": "श्री राजा शिवछत्रपती यांच्या आज्ञेवरून: लष्करातील सैनिकांनी रयतेच्या भाजीच्या देठासही हात लावू नये. रयतेवर कसलाही जुलूम न होता त्यांना अभय दिले पाहिजे."
        },
        "interactive_story": {
            "title": "The Seal of the Swarajya",
            "prologue": "The year is 1674. Clouds roll over the cliffs of Raigad. You are Subhedar Malhar, leading a cavalry outpost in the lush Konkan valleys.",
            "chapters": [
                {
                    "chapter_number": 1,
                    "title": "The Monsoon Encampment",
                    "content": "Torrential rain pounds the Sahyadri ranges. Your horses need fodder, and wet wood is scarce. A troop of young cavalrymen approaches you, suggesting they harvest firewood and grain from the nearby village of farmers.",
                    "choices": [
                        {
                            "text": "Forbid them instantly and read aloud the Maharaja's Farman bearing the Royal Seal.",
                            "next_hint": "Honor the Swarajya pledge of protecting the peasantry at all costs."
                        },
                        {
                            "text": "Send a treasury officer with silver coins to buy provisions openly from the village elders.",
                            "next_hint": "Fair market trade wins the enduring loyalty of the local population."
                        }
                    ]
                },
                {
                    "chapter_number": 2,
                    "title": "The Inspection at Dawn",
                    "content": "At dawn, the Maharaja himself arrives on horseback accompanied by swift scouts. He inspects the perimeter of your camp. Seeing that the peasants' haystacks and orchards remain untouched, a rare smile graces his face.",
                    "choices": [
                        {
                            "text": "Present the village patil (headman) to the Maharaja to testify to the peace.",
                            "next_hint": "The Patil blesses the king, shouting 'Jai Bhavani, Jai Shivaji!'"
                        },
                        {
                            "text": "Request orders for building coastal watchtowers near the Janjira frontier.",
                            "next_hint": "Expanding the naval defense of the realm."
                        }
                    ]
                }
            ]
        },
        "podcast_script": {
            "title": "Not Even a Stalk of Green: The Ethics of Shivaji's Swarajya",
            "duration": "3.5 mins",
            "speakers": ["Narrator", "Archivist"],
            "dialogue": [
                {"speaker": "Narrator", "cue": "[Sound of galloping horses stopping abruptly, rustling Modi script parchment]", "line": "In seventeenth-century warfare, invading armies stripped villages bare. But in the mountain fortresses of Maharashtra, a handwritten letter changed military history."},
                {"speaker": "Archivist", "cue": "[Sitar melody blending into warm acoustic strings]", "line": "It was written in the rapid, cursive loops of Modi script. Chhatrapati Shivaji Maharaj warned his commanders: 'If you take wood from the farmer, or seize their grain, what difference remains between you and the looters?'"},
                {"speaker": "Narrator", "cue": "[Sound of rain pouring over Sahyadri rocks]", "line": "He wrote that if a poor farmer cannot plant their seed, the kingdom itself starves. Sovereignty, in his eyes, was measured by the safety of the weakest citizen."},
                {"speaker": "Archivist", "cue": "[Resonant temple bell]", "line": "This edict remains preserved today in the archives of Pune. A timeless testament to compassionate leadership."}
            ]
        },
        "guided_tour": {
            "title": "Summit of Sovereignty: Raigad Fort Audio Walk",
            "total_stops": 4,
            "stops": [
                {
                    "stop_number": 1,
                    "name": "Maha Darwaza (The Great Gate)",
                    "orientation": "Flanked by two towering bastions at 2,800 feet",
                    "narrative": "Look up at the sheer stone arches of Maha Darwaza. Ingeniously angled so enemy cannons could never sight it straight.",
                    "audio_hook": "Feel the brisk mountain breeze that swept past royal messengers carrying urgent edicts."
                },
                {
                    "stop_number": 2,
                    "name": "The Royal Secretariat (Daftarkhana)",
                    "orientation": "Plaza east of the main palace complex",
                    "narrative": "Here sat the royal scribes wielding reed pens and iron-gall ink, translating royal decrees into Modi script, Persian diplomatic missives, and Sanskrit treatises.",
                    "audio_hook": "Listen for the rhythmic scraping of reeds upon handmade paper."
                },
                {
                    "stop_number": 3,
                    "name": "Holi Cha Mal & Royal Market (Bazar Peth)",
                    "orientation": "Dual rows of 44 stone shops raised on high plinths",
                    "narrative": "Notice how each shop was elevated so riders on horseback could buy goods without dismounting. Here spices, swords, and silks were fairly traded.",
                    "audio_hook": "Imagine merchants from Surat, Goa, and Venice bargaining in the afternoon mist."
                },
                {
                    "stop_number": 4,
                    "name": "Takmak Tok (Execution Point & Echo Cliff)",
                    "orientation": "Extreme northern edge overlooking a 1,200-foot precipice",
                    "narrative": "Standing atop this sheer drop, look out across the emerald valleys of the Konkan. Discipline was unyielding: those who broke the trust of the people faced justice here.",
                    "audio_hook": "The silence here is profound, broken only by falcon cries."
                }
            ]
        }
    },
    {
        "id": "brihadeeswara_inscription_1010",
        "title": "Great Temple Dedication of Rajaraja Chola",
        "origin": "Brihadeeswarar Temple, Thanjavur, Tamil Nadu",
        "era": "c. 1010 CE (Chola Empire)",
        "script": "Tamil-Grantha Script (கல்வெட்டு)",
        "original_language": "Old Tamil",
        "category": "Architectural Epigraph",
        "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=800&q=80",
        "summary": "Emperor Rajaraja Chola I carves into the stone plinth of the great temple: an accounting of every gold gift, bronze artisan, temple dancer, and community custodian who built the towering Vimana.",
        "original_script_text": "ஸ்வஸ்தி ஸ்ரீ... கொப்பரகேசரிவன்மரான உடையார் ஸ்ரீராஜராஜ தேவர்க்கு யாண்டு இருபத்தைந்தாவது... நாம் குடுத்தனவும், நம் அக்கன் குடுத்தனவும், நம் பெண்டுகள் குடுத்தனவும் மற்றும் குடுத்தார் குடுத்தனவும் இக்கல்லிலே வெட்டுக என்று திருவாய்மொழிந்தருள...",
        "transliteration": "Svasti Shri... Kopparakesarivanmarana Udaiyar Shri Rajaraja Devarkku yaandu irubaththainthavathu... Naam kuduthanavum, nam akkan kuduthanavum, nam pendugal kuduthanavum...",
        "archaic_glossary": [
            {"term": "Vimana", "meaning": "The towering 216-foot pyramidal sanctum tower crowned by an 80-tonne granite dome"},
            {"term": "Udaiyar", "meaning": "Honored sovereign ruler and protector"},
            {"term": "Kalvettu", "meaning": "Stone epigraph chiselled into temple granite to endure eternity"}
        ],
        "default_translations": {
            "en-IN": "Hail Prosperity! In the 25th regnal year of King Rajaraja Deva: The King commanded that all gifts given by himself, all gifts bestowed by his elder sister Kundavai, by his royal consorts, and by every humble citizen and artisan, shall be engraved permanently upon this stone.",
            "hi-IN": "कल्याण हो! राजा राजराज देव के शासन के 25वें वर्ष में: महाराजा ने आदेश दिया कि उनके स्वयं के द्वारा, उनकी ज्येष्ठ बहन कुंदवई द्वारा, उनकी रानियों द्वारा और राज्य के प्रत्येक नागरिक एवं शिल्पकार द्वारा दिए गए समस्त दान को इस मंदिर के पत्थरों पर सदा के लिए उत्कीर्ण किया जाए।",
            "bn-IN": "শুভ হোক! রাজা রাজরাজ দেবের রাজত্বের ২৫তম বর্ষে: রাজা আদেশ দিলেন যে তাঁর নিজের দেওয়া সমস্ত উপহার, তাঁর জ্যেষ্ঠা ভগিনী কুন্দবইয়ের দান, এবং প্রতিটি কারিগর ও সাধারণ মানুষের অবদান এই শিলায় চিরতরে উৎকীর্ণ করা হোক।",
            "ta-IN": "சுவஸ்தி ஸ்ரீ! ராஜராஜ சோழனின் 25-வது ஆட்சியாண்டில்: நாம் கொடுத்ததும், நம் தமக்கை குந்தவை கொடுத்ததும், நம் தேவிமார்கள் கொடுத்ததும், பிறர் கொடுத்ததும் இக்கல்லில் வெட்டப்பட வேண்டும் என்று ஆணையிட்டார்.",
            "mr-IN": "कल्याण असो! राजा राजराज चोल यांच्या २५व्या राज्यवर्षामध्ये: राजांनी आदेश दिला की त्यांनी दिलेली सर्व दाने, त्यांच्या भगिनी कुंदवई आणि प्रत्येक कारागिराचे योगदान या पाषाणावर कायमचे कोरले जावे."
        },
        "interactive_story": {
            "title": "The Granite Spire of the Cholas",
            "prologue": "The year is 1010 CE. The Kaveri delta glows golden with ripening paddy. You are Arul, a master bronze caster preparing to gild the crowning Kalasam atop the Vimana.",
            "chapters": [
                {
                    "chapter_number": 1,
                    "title": "The Eighty-Tonne Capstone",
                    "content": "A six-kilometer earthen ramp has brought the titanic monolithic granite block to the pinnacle, 216 feet into the tropical sky. Princess Kundavai has sent gold ornaments melted from royal heirlooms to cast the finial.",
                    "choices": [
                        {
                            "text": "Inspect the copper-gold alloy ratio before the pouring ritual starts.",
                            "next_hint": "Ensuring the Kalasam glows radiant across the delta for a thousand years."
                        },
                        {
                            "text": "Etch the names of your sixteen apprentice smelters onto the inner rim of the bronze.",
                            "next_hint": "Immortality for the humble hands that built the monument."
                        }
                    ]
                },
                {
                    "chapter_number": 2,
                    "title": "Consecration of the Big Temple",
                    "content": "Trumpets carved from conch shells echo across Thanjavur. Priests chant Vedic verses while bronze bells toll in unison. King Rajaraja approaches the stone base where epigraphers are chivvying letters into the granite.",
                    "choices": [
                        {
                            "text": "Bow before the King and present the consecrated bronze lamp.",
                            "next_hint": "The lamp is lit, casting dancing shadows upon the frescoes."
                        },
                        {
                            "text": "Join the celebration in the natya mandapam with 400 temple bards.",
                            "next_hint": "Music and rhythmic footwork reverberate through the granite pillars."
                        }
                    ]
                }
            ]
        },
        "podcast_script": {
            "title": "Stone That Defied Gravity: The Secrets of Thanjavur",
            "duration": "4 mins",
            "speakers": ["Host", "Epigraphist"],
            "dialogue": [
                {"speaker": "Host", "cue": "[Sound of deep bronze temple bell resonating, chanting of Om Namah Shivaya]", "line": "Imagine standing before a temple tower that rises 216 feet into the Tamil Nadu sky, built entirely of interlocking granite without a single drop of mortar."},
                {"speaker": "Epigraphist", "cue": "[Soft sounds of Kaveri river flowing]", "line": "What makes Brihadeeswarar truly modern is not just engineering—it is its radical transparency. Rajaraja didn't just carve his own name; he carved the names of over 400 dancers, the cooks, the accountants, and the goldsmiths."},
                {"speaker": "Host", "cue": "[Sound of chisel cutting stone]", "line": "Every fraction of a gram of gold donated by his sister Kundavai was audited and engraved on the basement walls. It is perhaps the world's most beautiful public ledger."},
                {"speaker": "Epigraphist", "cue": "[Temple bell fade]", "line": "More than a millennium later, earthquakes and monsoons have passed, but the shadows of Thanjavur continue to mesmerize the world."}
            ]
        },
        "guided_tour": {
            "title": "The Granite Wonder: Inside Thanjavur's Royal Temple",
            "total_stops": 4,
            "stops": [
                {
                    "stop_number": 1,
                    "name": "Keralantakan Gopuram (The Outer Gate)",
                    "orientation": "Facing East along the grand entry axis",
                    "narrative": "Pass through the five-tiered eastern gateway. Notice how the entrance gateway is deliberately shorter than the sanctum tower inside—a triumph of spiritual humility.",
                    "audio_hook": "Listen for the temple elephants trumpeting at dawn."
                },
                {
                    "stop_number": 2,
                    "name": "The Monolithic Nandi Pavilion",
                    "orientation": "Courtyard center facing the sanctum",
                    "narrative": "Behold the massive sacred bull Nandi, carved from a single colossal block of stone weighing over 20 tonnes. It faces Lord Shiva's sanctum with serene poise.",
                    "audio_hook": "Feel the coolness of the granite under your feet."
                },
                {
                    "stop_number": 3,
                    "name": "The Epigraphical Plinth (South Wall)",
                    "orientation": "Along the southern basement course of the Vimana",
                    "narrative": "Run your fingers near the base course. Here runs the continuous Tamil-Grantha inscription, detailing the salaries, daily rice allocations, and lands granted to temple caretakers.",
                    "audio_hook": "This inscription is over 100 meters long—an open book carved into stone."
                },
                {
                    "stop_number": 4,
                    "name": "The 80-Tonne Kumbam Finial",
                    "orientation": "Looking directly upward at the apex of the Vimana",
                    "narrative": "At the summit sits the single granite octagonal dome, crowned by the golden kalasam. For centuries, folklore claimed it cast no shadow at noon.",
                    "audio_hook": "A masterwork of Chola mathematical precision."
                }
            ]
        }
    },
    {
        "id": "baul_oral_archive",
        "title": "Oral Archive: Mystic Ballads of Lalon Fakir",
        "origin": "Kushtia / Nadia, Bengal Delta",
        "era": "c. 19th Century Oral Tradition",
        "script": "Bengali Oral Transmission (বাউল গান)",
        "original_language": "Bengali",
        "category": "Oral Archive & Folk Tradition",
        "image_url": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=800&q=80",
        "summary": "Recorded oral testimony of a wandering Baul minstrel singing Lalon Fakir's eternal verse on 'Moner Manush'—seeking the divine person within every human soul beyond caste, dogma, and religion.",
        "original_script_text": "খাঁচার ভিতর অচিন পাখি কেমনে আসে যায়। তারে ধরতে পারলে মন-বেড়ি দিতাম পাখির পায়... সব লোকে কয় লালন কি জাত সংসারে? লালন বলে জাতের কি রূপ দেখলাম না এই নজরে।",
        "transliteration": "Khanchar bhitor ochin pakhi kemne ashe jaay. Taare dhorte parle mon-beri ditam pakhir paay... Sob loke koy Lalon ki jaat shongsare? Lalon bole jaater ki roop dekhlam na ei nojore.",
        "archaic_glossary": [
            {"term": "Ochin Pakhi", "meaning": "The unknown mysterious bird; metaphor for the elusive human life-breath and soul"},
            {"term": "Moner Manush", "meaning": "The Person of the Heart; the inner divinity dwelling in every mortal body"},
            {"term": "Ektara", "meaning": "One-stringed drone instrument plucked by Baul wanderers while walking across dusty villages"}
        ],
        "default_translations": {
            "en-IN": "How does the unknown bird fly in and out of the cage of the mortal body? If only I could catch it, I would bind its feet with the chains of my devoted mind... Everyone asks: What caste does Lalon belong to in this world? Lalon replies: I have never seen what caste looks like with these mortal eyes.",
            "hi-IN": "इस नश्वर पिंजरे के भीतर वह अनजान पंछी कैसे आता और जाता है? यदि मैं उसे पकड़ पाता, तो अपने मन की बेड़ियों से उसके पांव बांध लेता... सब पूछते हैं कि इस संसार में लालन की कौन सी जाति है? लालन कहते हैं—इन आंखों से मैंने कभी जाति का कोई रूप नहीं देखा।",
            "bn-IN": "খাঁচার ভিতর অচিন পাখি কেমনে আসে যায়? তারে ধরতে পারলে মন-বেড়ি দিতাম পাখির পায়... সব লোকে কয় লালন কি জাত সংসারে? লালন বলে জাতের কি রূপ দেখলাম না এই নজরে।",
            "ta-IN": "இந்த உடலெனும் கூண்டிற்குள் தெரியாத பறவை எவ்வாறு வந்து போகிறது? உலகம் கேட்கிறது: லாலன் எந்த சாதியைச் சேர்ந்தவர்? லாலன் கூறுகிறார்: என் கண்களால் சாதியின் வடிவத்தை நான் கண்டதில்லை.",
            "mr-IN": "या शरीराच्या पिंजऱ्यात तो अनामिक पक्षी कसा येतो आणि जातो? सर्व जग विचारते की लालनची जात कोणती? लालन म्हणतात—मी माझ्या डोळ्यांनी कधी जातीचे रूप पाहिलेच नाही."
        },
        "interactive_story": {
            "title": "The River Minstrel's Journey",
            "prologue": "Twilight descends upon the Padma River. You are Shubro, an apprentice walking alongside an elder Baul singer holding an ektara.",
            "chapters": [
                {
                    "chapter_number": 1,
                    "title": "The Village Ferry",
                    "content": "At the river ghat, orthodoxy has divided the boat passengers into separate quarters. The elder minstrel plucks his single brass string. The notes hover over the dark water like fireflies.",
                    "choices": [
                        {
                            "text": "Begin singing the verse: 'What is the color of caste? Can water be divided?'",
                            "next_hint": "The villagers fall silent, touched by the timeless truth of the song."
                        },
                        {
                            "text": "Offer roasted puffed rice from your cloth pouch to all passengers equally.",
                            "next_hint": "Breaking caste taboos through simple human warmth."
                        }
                    ]
                },
                {
                    "chapter_number": 2,
                    "title": "The Gathering under the Banyan Tree",
                    "content": "Under the ancient spreading banyan, lantern light illuminates faces of Hindus, Muslims, weavers, and farmers sitting side by side in the dust, listening to the oral verses passed down through centuries.",
                    "choices": [
                        {
                            "text": "Pass the ektara to a young girl eager to learn the melody of compassion.",
                            "next_hint": "The oral tradition is passed forward to the next generation."
                        },
                        {
                            "text": "Sing into the midnight mist until dawn paints the delta with gold.",
                            "next_hint": "Music unites hearts where doctrines build walls."
                        }
                    ]
                }
            ]
        },
        "podcast_script": {
            "title": "The Bird in the Cage: The Sonic Universe of Baul Fakirs",
            "duration": "3 mins",
            "speakers": ["Host", "Ethnomusicologist"],
            "dialogue": [
                {"speaker": "Host", "cue": "[Sound of Ektara strumming, gentle river ripples, crickets]", "line": "In the waterways of the Bengal Delta, heritage wasn't carved on stone. It was sung on dusty roads and carried on the breath of wandering wanderers."},
                {"speaker": "Ethnomusicologist", "cue": "[Dubki percussion pulse joins in]", "line": "Lalon Fakir composed over two thousand songs in the nineteenth century, yet he wrote down almost none. They survived because people sang them in boats, fields, and tea stalls."},
                {"speaker": "Host", "cue": "[Warm vocal humming]", "line": "His poetry was radical. When clerics and priests asked his caste, he smiled: 'When a man is born, what mark does he bear? When a man dies, what remains?'"},
                {"speaker": "Ethnomusicologist", "cue": "[Ektara chord fades out]", "line": "UNESCO recognized the Baul songs as an Intangible Cultural Heritage of Humanity. In every strum of the ektara, humanity finds its common home."}
            ]
        },
        "guided_tour": {
            "title": "The Delta Songlines: Kushtia & The Mystic Paths",
            "total_stops": 3,
            "stops": [
                {
                    "stop_number": 1,
                    "name": "The Riverbank of the Gorai",
                    "orientation": "Standing at the edge of the silt-laden river",
                    "narrative": "Feel the damp delta breeze. Here Lalon was rescued from the river waters after being abandoned during an epidemic, and began his new life as a spiritual free-thinker.",
                    "audio_hook": "Listen to the distant call of boatmen singing Bhatiali folk songs."
                },
                {
                    "stop_number": 2,
                    "name": "The Akhra of Cheuriya",
                    "orientation": "Under the canopy of jackfruit and neem trees",
                    "narrative": "This simple courtyard became a sanctuary for seekers of all backgrounds. No sacred texts were debated here; only oral music was exchanged through night-long vigils.",
                    "audio_hook": "Notice the hypnotic rhythm of the dotara and brass cymbals."
                },
                {
                    "stop_number": 3,
                    "name": "The Tomb of the Unbound Spirit",
                    "orientation": "The serene white memorial shrine",
                    "narrative": "A place of quiet pilgrimage where millions gather each full moon. No religious symbols adorn the inner sanctum—only flowers and the living sound of poetry.",
                    "audio_hook": "Close your eyes and listen to the song that never dies."
                }
            ]
        }
    },
    {
        "id": "rani_lakshmibai_1857",
        "title": "Letter of Defiance: Rani Lakshmibai of Jhansi",
        "origin": "Jhansi Fort, Bundelkhand, Uttar Pradesh",
        "era": "c. 1857-1858 CE (The First War of Independence)",
        "script": "Hindustani in Nastaliq / Kaithi Script",
        "original_language": "Hindustani / Bundelkhandi",
        "category": "Historical Letter & Oral Testimony",
        "image_url": "https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=800&q=80",
        "summary": "The courageous declaration of Rani Lakshmibai refusing the unjust annexation under the Doctrine of Lapse: 'Main apni Jhansi nahi doongi' (I shall never surrender my Jhansi).",
        "original_script_text": "मेरी झांसी पर किसी विदेशी हुकूमत का कोई हक नहीं है। हम अपने वतन की हिफ़ाज़त के लिए आखिरी दम तक लड़ेंगे। 'मैं अपनी झांसी नहीं दूंगी!' हर मां और बेटी अपने स्वाभिमान की रक्षा करना जानती है।",
        "transliteration": "Meri Jhansi par kisi videshi hukumat ka koi haq nahi hai. Hum apne watan ki hifazat ke liye aakhiri dam tak ladenge. 'Main apni Jhansi nahi doongi!' Har maa aur beti apne swabhiman ki raksha karna jaanti hai.",
        "archaic_glossary": [
            {"term": "Swabhiman", "meaning": "Unyielding self-respect, honor, and sovereign dignity"},
            {"term": "Watan", "meaning": "Motherland, birthplace, and ancestral soil"},
            {"term": "Durga Dal", "meaning": "The all-women military regiment trained by Lakshmibai to defend Jhansi's bastions"}
        ],
        "default_translations": {
            "en-IN": "No foreign colonial power possesses any right over my Jhansi. We shall fight till our very last breath for the defense of our motherland. 'I will not surrender my Jhansi!' Every mother and daughter knows how to defend her sacred honor.",
            "hi-IN": "मेरी झांसी पर किसी विदेशी हुकूमत का कोई हक नहीं है। हम अपने वतन की हिफ़ाज़त के लिए आखिरी दम तक लड़ेंगे। 'मैं अपनी झांसी नहीं दूंगी!' हर मां और बेटी अपने स्वाभिमान की रक्षा करना जानती है।",
            "bn-IN": "আমার ঝাঁসির ওপর কোনো বিদেশি শক্তির কোনো অধিকার নেই। আমরা মাতৃভূমির রক্ষার জন্য শেষ নিঃশ্বাস পর্যন্ত লড়াই করব। 'আমি আমার ঝাঁসি দেব না!' প্রতিটি মা ও মেয়ে নিজের আত্মসম্মান রক্ষা করতে জানে।",
            "ta-IN": "எனது ஜான்சியின் மீது எந்த வெளிநாட்டு ஆதிக்கத்திற்கும் உரிமை இல்லை. நமது தாய்நாட்டின் பாதுகாப்பிற்காக கடைசி மூச்சு வரை போராடுவோம். 'நான் என் ஜான்சியை விட்டுத்தர மாட்டேன்!'",
            "mr-IN": "माझ्या झाशीवर कोणत्याही परकीय सत्तेचा अधिकार नाही. आम्ही आमच्या मातृभूमीच्या रक्षणासाठी शेवटच्या श्वासापर्यंत लढू. 'मी माझी झाशी देणार नाही!'"
        },
        "interactive_story": {
            "title": "The Lioness of Bundelkhand",
            "prologue": "March 1858. The granite walls of Jhansi Fort reverberate with the thunder of British artillery under General Rose. You are Jhalkaribai, the fierce commander of the women's Durga Dal.",
            "chapters": [
                {
                    "chapter_number": 1,
                    "title": "Defending the Western Bastion",
                    "content": "Cannonballs smash against the outer ramparts. The ammunition magazine on the Ganeshi bastion needs swift reinforcement. Rani Lakshmibai rides past on her stallion, sword flashing in the moonlight.",
                    "choices": [
                        {
                            "text": "Direct the women's gunnery battery to silence the siege guns at the breach.",
                            "next_hint": "Your counter-battery fire shatters the enemy siege artillery."
                        },
                        {
                            "text": "Disguise yourself in the royal crest to draw enemy attention away while the Queen rallies reinforcements.",
                            "next_hint": "A legendary act of self-sacrifice commemorated in Bundeli folklore."
                        }
                    ]
                },
                {
                    "chapter_number": 2,
                    "title": "The Midnight Breakout",
                    "content": "With her adopted child Damodar tied to her back, the Queen prepares to leap her horse down the steep southern bastion into the darkness to unite with Tatya Tope's forces at Kalpi.",
                    "choices": [
                        {
                            "text": "Ride vanguard ahead through the ravine to clear the cavalry patrol.",
                            "next_hint": "Guiding the Queen safely through the cordon of guards."
                        },
                        {
                            "text": "Blow up the gunpowder depot to prevent the arsenal from falling into enemy hands.",
                            "next_hint": "The blast shakes the fortress as the Queen rides toward freedom."
                        }
                    ]
                }
            ]
        },
        "podcast_script": {
            "title": "Thunder over the Ramparts: The Immortal Words of Lakshmibai",
            "duration": "3.5 mins",
            "speakers": ["Historian", "Dramatist"],
            "dialogue": [
                {"speaker": "Historian", "cue": "[Sound of cannon fire echoing in the distance, drumroll]", "line": "In March 1858, an ultimatum arrived at Jhansi Fort demanding unconditional surrender. The British commander expected a tearful capitulation."},
                {"speaker": "Dramatist", "cue": "[Sharp sound of sword drawn from scabbard]", "line": "Instead, a twenty-two-year-old queen stepped onto the battlements and uttered four words that ignited a nation: 'Main apni Jhansi nahi doongi!'"},
                {"speaker": "Historian", "cue": "[Subtle patriotic string score swells]", "line": "She had transformed Jhansi into an egalitarian citadel. Brahmin women, Muslim gunners, Dalit archers, and Bundela chieftains fought side by side as comrades."},
                {"speaker": "Dramatist", "cue": "[Hoofbeats in the night]", "line": "British General Hugh Rose himself wrote in his memoirs: 'The Rani was the bravest, the most capable military leader of the rebels.' Her legend lives forever."}
            ]
        },
        "guided_tour": {
            "title": "Citadel of Valor: Jhansi Fort Audio Trail",
            "total_stops": 4,
            "stops": [
                {
                    "stop_number": 1,
                    "name": "Khanderao Gate & The Outer Moat",
                    "orientation": "Facing the steep rocky slope of Bangira hill",
                    "narrative": "Stand at the foot of the hill where the British 1st Brigade launched their fierce assault. The solid granite hill made tunneling impossible.",
                    "audio_hook": "Feel the heat radiating from the Bundelkhand sun onto the stone."
                },
                {
                    "stop_number": 2,
                    "name": "The Great 'Kadak Bijli' Cannon",
                    "orientation": "South bastion overlooking the plains",
                    "narrative": "Gaze upon the fearsome brass cannon 'Kadak Bijli' (Lightning Strike), operated with deadly precision by Ghulam Ghaus Khan, the Queen's chief of artillery.",
                    "audio_hook": "Imagine the deafening roar as shells blasted across the rocky plain."
                },
                {
                    "stop_number": 3,
                    "name": "The Rani's Martial Courtyard",
                    "orientation": "Inside the inner palace complex",
                    "narrative": "Here Lakshmibai trained daily in horsemanship, archery, and swordsmanship with her childhood companions, defying contemporary constraints on women.",
                    "audio_hook": "Listen to the clashing of practice wooden blades."
                },
                {
                    "stop_number": 4,
                    "name": "Kudan Sthal (The Leap of Immortality)",
                    "orientation": "Sheer drop on the western rampart",
                    "narrative": "Here, with her young son tied securely in a sash, Rani Lakshmibai leaped her faithful horse Badal over the fortress wall in the dead of night to fight another day.",
                    "audio_hook": "The wind howls off the Bundelkhand plateau like an eternal battle cry."
                }
            ]
        }
    }
]
