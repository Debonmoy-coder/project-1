/**
 * HeritageVerse: Master Application Logic
 */

let appState = {
  currentArchive: null,
  currentTranscription: "",
  currentTitle: "Heritage Inscription",
  currentEra: "Ancient Period",
  targetLanguage: "hi-IN",
  currentNarrationAudio: null,
  isRecordingAudio: false,
  mediaRecorder: null,
  recordedAudioChunks: []
};

document.addEventListener("DOMContentLoaded", async () => {
  if (window.lucide) window.lucide.createIcons();
  await checkSystemStatus();
  await loadHeritageVault();
  setupEventListeners();
});

// -------------------------------------------------------------
// System Status & API Key Management
// -------------------------------------------------------------
async function checkSystemStatus() {
  try {
    const res = await fetch("/api/status");
    const data = await res.json();
    const badge = document.getElementById("apiKeyBadge");
    const quotaText = document.getElementById("quotaBannerText");
    const quotaBanner = document.getElementById("quotaBanner");

    if (data.sarvam_status.has_credits) {
      badge.innerHTML = `<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-emerald-950 text-emerald-300 border border-emerald-600/40"><span class="w-2 h-2 mr-1.5 bg-emerald-400 rounded-full animate-pulse"></span>Sarvam AI Live (Credits Active)</span>`;
      quotaBanner.classList.add("hidden");
    } else if (data.sarvam_status.configured) {
      badge.innerHTML = `<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-amber-950 text-amber-300 border border-amber-600/40"><span class="w-2 h-2 mr-1.5 bg-amber-400 rounded-full"></span>Key Connected (Quota 0 • Fallback Active)</span>`;
      quotaText.innerText = data.sarvam_status.message;
      quotaBanner.classList.remove("hidden");
    } else {
      badge.innerHTML = `<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-800 text-gray-300 border border-gray-600/40">Demo Simulator Mode</span>`;
      quotaBanner.classList.add("hidden");
    }
  } catch (err) {
    console.error("Failed to fetch system status:", err);
  }
}

async function saveApiKey() {
  const keyInput = document.getElementById("apiKeyInput");
  const newKey = keyInput.value.trim();
  if (!newKey) return;

  try {
    const res = await fetch("/api/settings/key", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ api_key: newKey })
    });
    const data = await res.json();
    alert(`API Key updated! Status: ${data.health.message}`);
    closeApiKeyModal();
    checkSystemStatus();
  } catch (err) {
    alert("Error updating API key: " + err);
  }
}

function openApiKeyModal() {
  document.getElementById("apiKeyModal").classList.remove("hidden");
}

function closeApiKeyModal() {
  document.getElementById("apiKeyModal").classList.add("hidden");
}

// -------------------------------------------------------------
// Tabs Navigation
// -------------------------------------------------------------
function switchTab(tabId) {
  document.querySelectorAll(".tab-content").forEach(el => el.classList.add("hidden"));
  document.querySelectorAll(".tab-btn").forEach(el => el.classList.remove("active"));

  const target = document.getElementById(tabId);
  const btn = document.getElementById(`tab_btn_${tabId}`);

  if (target) target.classList.remove("hidden");
  if (btn) btn.classList.add("active");

  if (window.lucide) window.lucide.createIcons();
}

// -------------------------------------------------------------
// Heritage Vault Loader
// -------------------------------------------------------------
async function loadHeritageVault() {
  const container = document.getElementById("vaultGrid");
  if (!container) return;

  try {
    const res = await fetch("/api/vault");
    const data = await res.json();
    const items = data.vault || [];

    container.innerHTML = items.map(item => `
      <div class="heritage-card overflow-hidden flex flex-col group cursor-pointer" onclick="selectVaultItem('${item.id}')">
        <div class="h-44 w-full overflow-hidden relative">
          <img src="${item.image_url}" alt="${item.title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
          <span class="absolute top-3 left-3 text-[11px] px-2 py-0.5 bg-black/60 backdrop-blur text-amber-300 rounded border border-amber-500/30 font-medium">
            ${item.era}
          </span>
          <span class="absolute bottom-2 left-3 text-xs text-amber-200/90 font-serif">
            📍 ${item.origin}
          </span>
        </div>
        <div class="p-4 flex-1 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between text-xs text-amber-500 font-semibold mb-1">
              <span>${item.script}</span>
              <span class="text-gray-400 font-normal">${item.category}</span>
            </div>
            <h3 class="text-base font-bold text-amber-100 group-hover:text-amber-300 transition-colors line-clamp-1">${item.title}</h3>
            <p class="text-xs text-gray-400 mt-2 line-clamp-2 leading-relaxed">${item.summary}</p>
          </div>
          <div class="mt-4 pt-3 border-t border-amber-900/30 flex items-center justify-between text-xs text-amber-400 font-medium">
            <span>Explore Archive</span>
            <span class="group-hover:translate-x-1 transition-transform">→</span>
          </div>
        </div>
      </div>
    `).join("");

    // Automatically select first item
    if (items.length > 0) {
      selectVaultItem(items[0].id);
    }
  } catch (err) {
    container.innerHTML = `<p class="text-red-400">Failed to load Heritage Vault archives.</p>`;
  }
}

async function selectVaultItem(archiveId) {
  try {
    const res = await fetch(`/api/vault/${archiveId}`);
    const item = await res.json();
    appState.currentArchive = item;
    appState.currentTitle = item.title;
    appState.currentEra = item.era;
    appState.currentTranscription = item.original_script_text || item.summary;

    // Update Banner / Detail View
    const heroTitle = document.getElementById("activeArchiveTitle");
    const heroSubtitle = document.getElementById("activeArchiveSubtitle");
    const scriptBox = document.getElementById("activeScriptBox");
    const translitBox = document.getElementById("activeTranslitBox");
    const glossaryContainer = document.getElementById("archaicGlossaryList");

    if (heroTitle) heroTitle.innerText = item.title;
    if (heroSubtitle) heroSubtitle.innerText = `${item.era} • ${item.origin} • Script: ${item.script}`;
    if (scriptBox) scriptBox.innerText = item.original_script_text;
    if (translitBox) translitBox.innerText = item.transliteration || "";

    if (glossaryContainer && item.archaic_glossary) {
      glossaryContainer.innerHTML = item.archaic_glossary.map(g => `
        <div class="p-2.5 rounded bg-amber-950/20 border border-amber-900/30">
          <span class="text-xs font-bold text-amber-300">${g.term}</span>:
          <span class="text-xs text-gray-300 ml-1 font-serif">${g.meaning}</span>
        </div>
      `).join("");
    }

    // Populate Translation Tab with default translation
    const transInput = document.getElementById("translateSourceText");
    if (transInput) {
      transInput.value = item.default_translations["en-IN"] || item.transliteration;
    }
    const transOutput = document.getElementById("translatedOutputText");
    if (transOutput) {
      transOutput.value = item.default_translations[appState.targetLanguage] || item.default_translations["hi-IN"] || "";
    }

    // Populate Story Workshop with interactive story
    if (item.interactive_story) {
      window.storyStudio.renderStory(item.interactive_story);
    }

    // Setup chat context
    const chatContextTitle = document.getElementById("chatContextTitle");
    if (chatContextTitle) chatContextTitle.innerText = item.title;

  } catch (err) {
    console.error("Error selecting vault item:", err);
  }
}

// -------------------------------------------------------------
// Manuscript OCR & Audio Ingestion
// -------------------------------------------------------------
async function processManuscriptUpload() {
  const fileInput = document.getElementById("manuscriptFileInput");
  const textInput = document.getElementById("rawTextInput");
  const resultsDiv = document.getElementById("ingestionResults");
  const loadingIndicator = document.getElementById("ingestionLoading");

  const formData = new FormData();
  if (fileInput.files.length > 0) {
    formData.append("file", fileInput.files[0]);
  } else if (textInput.value.trim()) {
    formData.append("raw_text", textInput.value.trim());
    formData.append("title", "User Uploaded Archival Excerpt");
  } else {
    alert("Please upload a manuscript image or paste archival text.");
    return;
  }

  loadingIndicator.classList.remove("hidden");
  resultsDiv.classList.add("hidden");

  try {
    const res = await fetch("/api/transcribe/manuscript", {
      method: "POST",
      body: formData
    });
    const data = await res.json();
    loadingIndicator.classList.add("hidden");
    resultsDiv.classList.remove("hidden");

    if (data.status === "success") {
      const r = data.result;
      document.getElementById("detectedScriptBadge").innerText = r.detected_script;
      document.getElementById("scriptEraBadge").innerText = r.script_era;
      document.getElementById("transcribedContent").innerText = r.transcription;

      appState.currentTranscription = r.transcription;
      appState.currentTitle = r.title;
      appState.currentEra = r.script_era;

      // Also forward to translation input
      document.getElementById("translateSourceText").value = r.transcription;
    }
  } catch (err) {
    loadingIndicator.classList.add("hidden");
    alert("Failed to analyze manuscript: " + err);
  }
}

// -------------------------------------------------------------
// Oral Archive Recording & STT
// -------------------------------------------------------------
async function toggleAudioRecording() {
  const btn = document.getElementById("recordOralAudioBtn");
  const statusLabel = document.getElementById("recordStatusLabel");

  if (!appState.isRecordingAudio) {
    // Start Recording
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      appState.mediaRecorder = new MediaRecorder(stream);
      appState.recordedAudioChunks = [];

      appState.mediaRecorder.ondataavailable = (e) => {
        if (e.data.size > 0) appState.recordedAudioChunks.push(e.data);
      };

      appState.mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(appState.recordedAudioChunks, { type: "audio/wav" });
        await sendAudioForSTT(audioBlob);
      };

      appState.mediaRecorder.start();
      appState.isRecordingAudio = true;
      btn.classList.add("bg-red-600", "animate-pulse");
      btn.innerHTML = `<i data-lucide="square" class="w-4 h-4 mr-1.5"></i> Stop Recording`;
      statusLabel.innerText = "🔴 Listening to oral testimony...";
      if (window.lucide) window.lucide.createIcons();
    } catch (err) {
      alert("Microphone access denied or unsupported: " + err);
    }
  } else {
    // Stop Recording
    if (appState.mediaRecorder) {
      appState.mediaRecorder.stop();
    }
    appState.isRecordingAudio = false;
    btn.classList.remove("bg-red-600", "animate-pulse");
    btn.innerHTML = `<i data-lucide="mic" class="w-4 h-4 mr-1.5"></i> Record Oral Archive`;
    statusLabel.innerText = "Processing oral recording with Sarvam STT...";
    if (window.lucide) window.lucide.createIcons();
  }
}

async function sendAudioForSTT(blob) {
  const formData = new FormData();
  formData.append("file", blob, "oral_archive.wav");

  try {
    const res = await fetch("/api/transcribe/audio", {
      method: "POST",
      body: formData
    });
    const data = await res.json();
    const statusLabel = document.getElementById("recordStatusLabel");
    statusLabel.innerText = `Transcription Complete (${data.engine})`;

    if (data.transcript) {
      document.getElementById("transcribedContent").innerText = data.transcript;
      document.getElementById("ingestionResults").classList.remove("hidden");
      document.getElementById("translateSourceText").value = data.transcript;
      appState.currentTranscription = data.transcript;
    }
  } catch (err) {
    alert("Error transcribing oral audio: " + err);
  }
}

// -------------------------------------------------------------
// Sarvam Mayura Translation
// -------------------------------------------------------------
async function executeTranslation() {
  const sourceText = document.getElementById("translateSourceText").value.trim();
  const targetLang = document.getElementById("targetLanguageSelect").value;
  const outArea = document.getElementById("translatedOutputText");
  const engineBadge = document.getElementById("translationEngineBadge");
  const noticeBanner = document.getElementById("translationNotice");

  if (!sourceText) {
    alert("Please provide source text to translate.");
    return;
  }

  outArea.value = "Translating with Sarvam Mayura API...";
  appState.targetLanguage = targetLang;

  try {
    const res = await fetch("/api/translate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        text: sourceText,
        source_language: "auto",
        target_language: targetLang,
        mode: "formal"
      })
    });
    const data = await res.json();

    outArea.value = data.translated_text || "";
    engineBadge.innerText = data.engine;

    if (data.notice) {
      noticeBanner.innerText = data.notice;
      noticeBanner.classList.remove("hidden");
    } else {
      noticeBanner.classList.add("hidden");
    }

    // Automatically sync translated text into the Narration Theater!
    document.getElementById("narrationTextInput").value = data.translated_text || sourceText;
    document.getElementById("voiceLangSelect").value = targetLang;

  } catch (err) {
    outArea.value = "Translation error: " + err;
  }
}

// -------------------------------------------------------------
// Story Transformation (Story / Podcast / Tour)
// -------------------------------------------------------------
async function transformStoryMode(mode) {
  // Update mode buttons
  document.querySelectorAll(".story-mode-btn").forEach(b => b.classList.remove("bg-amber-600", "text-white"));
  const activeBtn = document.getElementById(`mode_btn_${mode}`);
  if (activeBtn) activeBtn.classList.add("bg-amber-600", "text-white");

  // If vault item is selected and has pre-built mode, use it
  if (appState.currentArchive) {
    if (mode === "interactive_story" && appState.currentArchive.interactive_story) {
      window.storyStudio.renderStory(appState.currentArchive.interactive_story);
      return;
    } else if (mode === "podcast" && appState.currentArchive.podcast_script) {
      window.storyStudio.renderPodcast(appState.currentArchive.podcast_script);
      return;
    } else if (mode === "guided_tour" && appState.currentArchive.guided_tour) {
      window.storyStudio.renderTour(appState.currentArchive.guided_tour);
      return;
    }
  }

  // Otherwise, request transformation from server
  try {
    const res = await fetch("/api/story/transform", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title: appState.currentTitle,
        transcription: appState.currentTranscription,
        era: appState.currentEra,
        mode: mode
      })
    });
    const data = await res.json();

    if (mode === "interactive_story") {
      window.storyStudio.renderStory(data.content);
    } else if (mode === "podcast") {
      window.storyStudio.renderPodcast(data.content);
    } else if (mode === "guided_tour") {
      window.storyStudio.renderTour(data.content);
    }
  } catch (err) {
    alert("Error transforming story: " + err);
  }
}

// -------------------------------------------------------------
// Sarvam Bulbul TTS Voice Narration
// -------------------------------------------------------------
async function generateAndPlayNarration() {
  const text = document.getElementById("narrationTextInput").value.trim();
  const lang = document.getElementById("voiceLangSelect").value;
  const speaker = document.getElementById("voiceSpeakerSelect").value;
  const soundscape = document.getElementById("soundscapeSelect").value;
  const pace = parseFloat(document.getElementById("paceSlider").value);
  const playBtn = document.getElementById("playNarrationBtn");

  if (!text) {
    alert("Please provide narrative text to speak.");
    return;
  }

  if (window.heritageAudio.isPlaying) {
    window.heritageAudio.stopPlayback();
    return;
  }

  playBtn.innerHTML = `<span class="inline-block animate-spin mr-2">⏳</span> Synthesizing with Sarvam AI...`;

  try {
    const res = await fetch("/api/narration/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        text: text,
        language_code: lang,
        speaker: speaker,
        pace: pace,
        model: "bulbul:v3",
        soundscape: soundscape
      })
    });
    const data = await res.json();

    playBtn.innerHTML = `<i data-lucide="square" class="w-5 h-5 mr-2"></i> Stop Narration`;
    if (window.lucide) window.lucide.createIcons();

    window.heritageAudio.playNarration({
      audioBase64: data.audio_base64,
      format: data.format || "wav",
      text: text,
      soundscape: soundscape,
      languageCode: lang,
      useWebSpeech: data.use_web_speech || false
    });

  } catch (err) {
    playBtn.innerHTML = `<i data-lucide="play" class="w-5 h-5 mr-2"></i> Play Story Narration`;
    if (window.lucide) window.lucide.createIcons();
    alert("Error generating narration: " + err);
  }
}

// -------------------------------------------------------------
// Heritage Scholar Q&A Chat
// -------------------------------------------------------------
async function sendHeritageChat() {
  const input = document.getElementById("chatInput");
  const query = input.value.trim();
  const messagesDiv = document.getElementById("chatMessages");
  if (!query) return;

  // Append user message
  messagesDiv.innerHTML += `
    <div class="flex justify-end mb-3">
      <div class="bg-amber-600/30 text-amber-100 border border-amber-500/40 px-3.5 py-2 rounded-lg max-w-[80%] text-sm">
        ${query}
      </div>
    </div>
  `;
  input.value = "";
  messagesDiv.scrollTop = messagesDiv.scrollHeight;

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        query: query,
        context_title: appState.currentTitle,
        transcription: appState.currentTranscription
      })
    });
    const data = await res.json();

    messagesDiv.innerHTML += `
      <div class="flex justify-start mb-3">
        <div class="bg-indigo-950/40 text-gray-200 border border-indigo-700/40 px-3.5 py-2.5 rounded-lg max-w-[85%] text-sm font-serif">
          <div class="text-[11px] text-amber-400 font-sans font-semibold mb-1">📜 ${data.persona}</div>
          ${data.chronicler_response}
        </div>
      </div>
    `;
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
  } catch (err) {
    messagesDiv.innerHTML += `<div class="text-xs text-red-400">Failed to consult scholar: ${err}</div>`;
  }
}

// -------------------------------------------------------------
// Event Listeners Setup
// -------------------------------------------------------------
function setupEventListeners() {
  // Volume controls
  const ambientVol = document.getElementById("ambientVolSlider");
  if (ambientVol) {
    ambientVol.addEventListener("input", (e) => {
      window.heritageAudio.setAmbientVolume(e.target.value);
    });
  }

  const voiceVol = document.getElementById("voiceVolSlider");
  if (voiceVol) {
    voiceVol.addEventListener("input", (e) => {
      window.heritageAudio.setVoiceVolume(e.target.value);
    });
  }

  // Chat Enter Key
  const chatInput = document.getElementById("chatInput");
  if (chatInput) {
    chatInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") sendHeritageChat();
    });
  }
}
