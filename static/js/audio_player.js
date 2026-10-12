/**
 * HeritageVerse Audio Player & Soundscape Mixer
 * Powered by Sarvam Bulbul TTS & Web Audio API Ambient Synthesizer
 */

class HeritageAudioStudio {
  constructor() {
    this.audioCtx = null;
    this.ambientNodes = [];
    this.ambientGainNode = null;
    this.voiceGainNode = null;
    this.currentAudioEl = null;
    this.isPlaying = false;
    this.currentSoundscape = "temple_drone";
    this.ambientVolume = 0.35;
    this.voiceVolume = 1.0;
    this.speechUtterance = null;
    this.activeWords = [];
    this.currentWordIdx = 0;
    this.captionTimer = null;
  }

  initAudioContext() {
    if (!this.audioCtx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      this.audioCtx = new AudioContext();
      this.ambientGainNode = this.audioCtx.createGain();
      this.ambientGainNode.gain.value = this.ambientVolume;
      this.ambientGainNode.connect(this.audioCtx.destination);
    }
    if (this.audioCtx.state === 'suspended') {
      this.audioCtx.resume();
    }
  }

  setAmbientVolume(val) {
    this.ambientVolume = parseFloat(val);
    if (this.ambientGainNode) {
      this.ambientGainNode.gain.setValueAtTime(this.ambientVolume, this.audioCtx.currentTime);
    }
  }

  setVoiceVolume(val) {
    this.voiceVolume = parseFloat(val);
    if (this.currentAudioEl) {
      this.currentAudioEl.volume = this.voiceVolume;
    }
  }

  // -------------------------------------------------------------
  // Ambient Soundscape Synthesizer (Web Audio API)
  // -------------------------------------------------------------
  startAmbient(soundscapeId) {
    this.stopAmbient();
    this.initAudioContext();
    this.currentSoundscape = soundscapeId;

    if (soundscapeId === "none" || !soundscapeId) return;

    const ctx = this.audioCtx;
    const now = ctx.currentTime;

    if (soundscapeId === "temple_drone") {
      // 432Hz Sacred Tanpura Drone + Chimes
      const freqs = [216, 432, 648];
      freqs.forEach(freq => {
        const osc = ctx.createOscillator();
        const oscGain = ctx.createGain();
        osc.type = "sine";
        osc.frequency.setValueAtTime(freq, now);
        oscGain.gain.setValueAtTime(0.08, now);
        osc.connect(oscGain);
        oscGain.connect(this.ambientGainNode);
        osc.start();
        this.ambientNodes.push({ osc, gain: oscGain });
      });

      // Periodic Bell Chime Loop
      const bellInterval = setInterval(() => {
        if (!this.isPlaying) {
          clearInterval(bellInterval);
          return;
        }
        this.playTempleBell();
      }, 7000);
      this.bellInterval = bellInterval;
      this.playTempleBell();

    } else if (soundscapeId === "royal_court") {
      // Sitar / Darbar Drone (D and A notes: 293.66Hz, 440Hz)
      const freqs = [146.83, 293.66, 440.0];
      freqs.forEach(freq => {
        const osc = ctx.createOscillator();
        const oscGain = ctx.createGain();
        osc.type = "triangle";
        osc.frequency.setValueAtTime(freq, now);
        oscGain.gain.setValueAtTime(0.06, now);
        osc.connect(oscGain);
        oscGain.connect(this.ambientGainNode);
        osc.start();
        this.ambientNodes.push({ osc, gain: oscGain });
      });

    } else if (soundscapeId === "monsoon_library" || soundscapeId === "ancient_caravan") {
      // Filtered Pink/Brown noise for rain or desert wind
      const bufferSize = ctx.sampleRate * 2;
      const noiseBuffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
      const output = noiseBuffer.getChannelData(0);
      let b0 = 0, b1 = 0, b2 = 0;
      for (let i = 0; i < bufferSize; i++) {
        const white = Math.random() * 2 - 1;
        b0 = 0.99886 * b0 + white * 0.0555179;
        b1 = 0.99332 * b1 + white * 0.0750759;
        b2 = 0.96900 * b2 + white * 0.1538520;
        output[i] = (b0 + b1 + b2) * 0.12;
      }
      const whiteNoise = ctx.createBufferSource();
      whiteNoise.buffer = noiseBuffer;
      whiteNoise.loop = true;

      const filter = ctx.createBiquadFilter();
      filter.type = soundscapeId === "monsoon_library" ? "lowpass" : "bandpass";
      filter.frequency.value = soundscapeId === "monsoon_library" ? 650 : 350;

      whiteNoise.connect(filter);
      filter.connect(this.ambientGainNode);
      whiteNoise.start();
      this.ambientNodes.push({ osc: whiteNoise });

    } else if (soundscapeId === "battlefield_echoes") {
      // Distant War Drum loop
      const drumInterval = setInterval(() => {
        if (!this.isPlaying) {
          clearInterval(drumInterval);
          return;
        }
        this.playWarDrum();
      }, 1800);
      this.drumInterval = drumInterval;
      this.playWarDrum();
    }
  }

  playTempleBell() {
    if (!this.audioCtx) return;
    const ctx = this.audioCtx;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    const now = ctx.currentTime;
    osc.type = "sine";
    osc.frequency.setValueAtTime(880, now); // A5 Bell tone
    osc.frequency.exponentialRampToValueAtTime(1760, now + 0.04);
    osc.frequency.exponentialRampToValueAtTime(880, now + 0.15);

    gain.gain.setValueAtTime(0.15, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 4.5);

    osc.connect(gain);
    gain.connect(this.ambientGainNode);
    osc.start(now);
    osc.stop(now + 4.5);
  }

  playWarDrum() {
    if (!this.audioCtx) return;
    const ctx = this.audioCtx;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    const now = ctx.currentTime;
    osc.type = "sine";
    osc.frequency.setValueAtTime(110, now);
    osc.frequency.exponentialRampToValueAtTime(45, now + 0.4);

    gain.gain.setValueAtTime(0.25, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.6);

    osc.connect(gain);
    gain.connect(this.ambientGainNode);
    osc.start(now);
    osc.stop(now + 0.6);
  }

  stopAmbient() {
    if (this.bellInterval) clearInterval(this.bellInterval);
    if (this.drumInterval) clearInterval(this.drumInterval);
    this.ambientNodes.forEach(node => {
      try {
        if (node.osc) {
          node.osc.stop();
          node.osc.disconnect();
        }
      } catch (e) {}
    });
    this.ambientNodes = [];
  }

  // -------------------------------------------------------------
  // Voice Narration Playback
  // -------------------------------------------------------------
  playNarration({ audioBase64, format, text, soundscape, languageCode, useWebSpeech }) {
    this.stopPlayback();
    this.initAudioContext();
    this.isPlaying = true;

    // Start ambient accompaniment
    this.startAmbient(soundscape || this.currentSoundscape);

    // Setup synchronized captions
    this.setupCaptions(text);

    // If Web Speech API fallback is requested (e.g., quota 0 fallback with Indic voice)
    if (useWebSpeech || !audioBase64) {
      this.playWithWebSpeech(text, languageCode, audioBase64);
      return;
    }

    // Standard Sarvam AI Base64 WAV / MP3 Audio Element
    const mime = format === "mp3" ? "audio/mpeg" : "audio/wav";
    const audioUrl = `data:${mime};base64,${audioBase64}`;
    this.currentAudioEl = new Audio(audioUrl);
    this.currentAudioEl.volume = this.voiceVolume;

    // Update Visualizer
    const visualizer = document.getElementById("audioVisualizer");
    if (visualizer) visualizer.classList.remove("opacity-0");

    this.currentAudioEl.onended = () => {
      this.stopPlayback();
    };

    this.currentAudioEl.onerror = (e) => {
      console.warn("Audio element error, falling back to Web Speech:", e);
      this.playWithWebSpeech(text, languageCode);
    };

    this.currentAudioEl.play().catch(err => {
      console.warn("Autoplay policy or decode error:", err);
      this.playWithWebSpeech(text, languageCode);
    });

    this.startCaptionHighlighting(this.currentAudioEl);
  }

  playWithWebSpeech(text, languageCode = "hi-IN", base64BackgroundWav = null) {
    if (!('speechSynthesis' in window)) {
      console.warn("Browser does not support Web Speech API");
      return;
    }
    window.speechSynthesis.cancel();

    // If a background harmonic chord was provided, play it quietly
    if (base64BackgroundWav) {
      try {
        const bgAudio = new Audio(`data:audio/wav;base64,${base64BackgroundWav}`);
        bgAudio.volume = 0.2;
        bgAudio.loop = true;
        bgAudio.play().catch(() => {});
        this.currentAudioEl = bgAudio;
      } catch (e) {}
    }

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = languageCode;
    utterance.rate = 0.95; // Steady storytelling pace
    utterance.pitch = 0.95; // Resonant tone

    // Attempt to match an Indian voice if available
    const voices = window.speechSynthesis.getVoices();
    const match = voices.find(v => v.lang.startsWith(languageCode.split("-")[0])) ||
                  voices.find(v => v.lang.includes("IN"));
    if (match) utterance.voice = match;

    const visualizer = document.getElementById("audioVisualizer");
    if (visualizer) visualizer.classList.remove("opacity-0");

    utterance.onboundary = (e) => {
      if (e.name === 'word') {
        this.highlightNextCaption();
      }
    };

    utterance.onend = () => {
      this.stopPlayback();
    };

    this.speechUtterance = utterance;
    window.speechSynthesis.speak(utterance);
  }

  setupCaptions(text) {
    const captionContainer = document.getElementById("captionContainer");
    if (!captionContainer) return;

    captionContainer.innerHTML = "";
    if (!text) return;

    const words = text.split(/\s+/);
    this.activeWords = words;
    this.currentWordIdx = 0;

    words.forEach((w, idx) => {
      const span = document.createElement("span");
      span.id = `caption_word_${idx}`;
      span.className = "mr-1.5 inline-block text-gray-300 transition-colors";
      span.innerText = w;
      captionContainer.appendChild(span);
    });
  }

  highlightNextCaption() {
    if (this.currentWordIdx >= this.activeWords.length) return;
    const prev = document.getElementById(`caption_word_${this.currentWordIdx - 1}`);
    if (prev) {
      prev.className = "mr-1.5 inline-block text-amber-200";
    }
    const curr = document.getElementById(`caption_word_${this.currentWordIdx}`);
    if (curr) {
      curr.className = "mr-1.5 inline-block font-semibold text-amber-400 bg-amber-500/20 px-1 rounded shadow-sm scale-105";
      curr.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    }
    this.currentWordIdx++;
  }

  startCaptionHighlighting(audioEl) {
    if (!this.activeWords.length) return;
    // Calculate approximate duration per word
    const approxTotalSec = audioEl.duration && !isNaN(audioEl.duration) ? audioEl.duration : (this.activeWords.length * 0.35);
    const msPerWord = (approxTotalSec / this.activeWords.length) * 1000;

    this.captionTimer = setInterval(() => {
      if (!this.isPlaying || this.currentWordIdx >= this.activeWords.length) {
        clearInterval(this.captionTimer);
        return;
      }
      this.highlightNextCaption();
    }, msPerWord);
  }

  stopPlayback() {
    this.isPlaying = false;
    this.stopAmbient();
    if (this.captionTimer) clearInterval(this.captionTimer);

    if (this.currentAudioEl) {
      try {
        this.currentAudioEl.pause();
        this.currentAudioEl.currentTime = 0;
      } catch (e) {}
      this.currentAudioEl = null;
    }

    if (window.speechSynthesis) {
      window.speechSynthesis.cancel();
    }

    const visualizer = document.getElementById("audioVisualizer");
    if (visualizer) visualizer.classList.add("opacity-0");

    const playBtn = document.getElementById("playNarrationBtn");
    if (playBtn) {
      playBtn.innerHTML = `<i data-lucide="play" class="w-5 h-5 mr-2"></i> Play Story Narration`;
      if (window.lucide) window.lucide.createIcons();
    }
  }
}

window.heritageAudio = new HeritageAudioStudio();
