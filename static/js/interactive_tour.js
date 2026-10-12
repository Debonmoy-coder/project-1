/**
 * HeritageVerse Story, Podcast & Virtual Tour Player
 */

class InteractiveStoryStudio {
  constructor() {
    this.currentStory = null;
    this.currentChapterIndex = 0;
    this.currentTourStopIndex = 0;
  }

  // -------------------------------------------------------------
  // Interactive Story Renderer
  // -------------------------------------------------------------
  renderStory(storyData) {
    this.currentStory = storyData;
    this.currentChapterIndex = 0;

    const container = document.getElementById("storyContentArea");
    if (!container) return;

    const chapters = storyData.chapters || [];
    if (!chapters.length) {
      container.innerHTML = `<p class="text-gray-400">No chapters found for this story.</p>`;
      return;
    }

    this.renderChapter(0);
  }

  renderChapter(idx) {
    this.currentChapterIndex = idx;
    const container = document.getElementById("storyContentArea");
    const chapter = this.currentStory.chapters[idx];
    if (!chapter || !container) return;

    let choicesHtml = "";
    if (chapter.choices && chapter.choices.length > 0) {
      choicesHtml = `
        <div class="mt-6 border-t border-amber-900/40 pt-4">
          <p class="text-xs uppercase tracking-widest text-amber-400 font-semibold mb-3">Choose Your Path:</p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
            ${chapter.choices.map((c, cIdx) => `
              <button onclick="window.storyStudio.selectChoice(${cIdx})"
                class="choice-btn text-left p-3.5 rounded-lg border border-amber-800/40 hover:border-amber-400 group">
                <span class="block text-sm text-amber-200 group-hover:text-amber-100 font-medium">${c.text}</span>
                <span class="block text-xs text-amber-500/70 mt-1">${c.next_hint || c.consequence || ""}</span>
              </button>
            `).join("")}
          </div>
        </div>
      `;
    } else {
      choicesHtml = `
        <div class="mt-6 p-4 rounded-lg bg-amber-950/20 border border-amber-800/30 text-center">
          <p class="text-amber-300 font-medium text-sm">✨ You have completed this historical chronicle.</p>
          <button onclick="window.storyStudio.renderChapter(0)" class="mt-3 px-4 py-1.5 text-xs bg-amber-500/20 text-amber-300 border border-amber-500/40 rounded-full hover:bg-amber-500/30">
            Restart Chronicle
          </button>
        </div>
      `;
    }

    container.innerHTML = `
      <div class="animate-fadeIn">
        <div class="flex items-center justify-between border-b border-amber-900/40 pb-3 mb-4">
          <div>
            <span class="text-xs text-amber-400 uppercase tracking-widest">Chapter ${chapter.chapter_number} of ${this.currentStory.chapters.length}</span>
            <h3 class="text-lg font-bold text-amber-100">${chapter.title}</h3>
          </div>
          <span class="text-xs px-2.5 py-1 bg-amber-900/30 text-amber-300 rounded border border-amber-700/30">
            ${this.currentStory.era || "Historical Era"}
          </span>
        </div>

        <div class="prose prose-invert max-w-none text-gray-200 text-sm leading-relaxed space-y-3 font-serif">
          <p>${chapter.content}</p>
        </div>

        ${choicesHtml}
      </div>
    `;

    // Populate Narration Box with current chapter content
    const narrationText = document.getElementById("narrationTextInput");
    if (narrationText) {
      narrationText.value = `${chapter.title}. ${chapter.content}`;
    }
  }

  selectChoice(choiceIdx) {
    const nextIdx = this.currentChapterIndex + 1;
    if (nextIdx < this.currentStory.chapters.length) {
      this.renderChapter(nextIdx);
    }
  }

  // -------------------------------------------------------------
  // Podcast Script Renderer
  // -------------------------------------------------------------
  renderPodcast(podcastData) {
    const container = document.getElementById("storyContentArea");
    if (!container) return;

    let fullScript = "";

    container.innerHTML = `
      <div class="animate-fadeIn">
        <div class="flex items-center justify-between border-b border-amber-900/40 pb-3 mb-4">
          <div>
            <span class="text-xs text-amber-400 uppercase tracking-widest">Audio Drama / Podcast</span>
            <h3 class="text-lg font-bold text-amber-100">${podcastData.title}</h3>
          </div>
          <span class="text-xs px-2.5 py-1 bg-amber-900/30 text-amber-300 rounded border border-amber-700/30">
            Est. ${podcastData.duration_est || podcastData.duration || "3 mins"}
          </span>
        </div>

        <div class="space-y-4 max-h-[420px] overflow-y-auto pr-2">
          ${podcastData.dialogue.map((d, idx) => {
            fullScript += `${d.speaker}: ${d.line} `;
            const isFirst = d.speaker.includes("1") || d.speaker.includes("Chronicler") || d.speaker.includes("Host");
            return `
              <div class="p-3 rounded-lg ${isFirst ? 'bg-amber-950/20 border-l-4 border-amber-500' : 'bg-indigo-950/20 border-l-4 border-blue-400'}">
                <div class="flex items-center justify-between text-xs mb-1">
                  <span class="font-bold ${isFirst ? 'text-amber-300' : 'text-blue-300'}">${d.speaker}</span>
                  ${d.cue ? `<span class="text-gray-400 italic text-[11px]">${d.cue}</span>` : ''}
                </div>
                <p class="text-sm text-gray-200 font-serif leading-relaxed">${d.line}</p>
              </div>
            `;
          }).join("")}
        </div>
      </div>
    `;

    const narrationText = document.getElementById("narrationTextInput");
    if (narrationText) {
      narrationText.value = fullScript.slice(0, 800);
    }
  }

  // -------------------------------------------------------------
  // Guided Virtual Tour Renderer
  // -------------------------------------------------------------
  renderTour(tourData) {
    this.currentTour = tourData;
    this.currentTourStopIndex = 0;
    this.renderTourStop(0);
  }

  renderTourStop(stopIdx) {
    this.currentTourStopIndex = stopIdx;
    const container = document.getElementById("storyContentArea");
    if (!container || !this.currentTour) return;

    const stops = this.currentTour.stops || [];
    const stop = stops[stopIdx];
    if (!stop) return;

    container.innerHTML = `
      <div class="animate-fadeIn">
        <div class="flex items-center justify-between border-b border-amber-900/40 pb-3 mb-4">
          <div>
            <span class="text-xs text-amber-400 uppercase tracking-widest">Waypoint ${stop.stop_number || stopIdx + 1} of ${stops.length}</span>
            <h3 class="text-lg font-bold text-amber-100">${stop.name}</h3>
          </div>
          <span class="text-xs px-2.5 py-1 bg-amber-900/30 text-amber-300 rounded border border-amber-700/30">
            🧭 ${stop.orientation || "Viewpoint"}
          </span>
        </div>

        <div class="p-4 rounded-lg bg-amber-950/15 border border-amber-900/30 mb-4 font-serif text-sm text-gray-200 leading-relaxed">
          <p>${stop.narrative}</p>
          ${stop.audio_hook || stop.audio_cue ? `
            <div class="mt-3 p-2 bg-amber-900/20 rounded border border-amber-800/30 text-xs text-amber-300 flex items-center">
              <span class="mr-2">🎧</span>
              <span><strong>Audio Cue:</strong> ${stop.audio_hook || stop.audio_cue}</span>
            </div>
          ` : ''}
        </div>

        <div class="flex items-center justify-between pt-2">
          <button onclick="window.storyStudio.renderTourStop(${Math.max(0, stopIdx - 1)})"
            ${stopIdx === 0 ? 'disabled' : ''}
            class="px-3.5 py-1.5 text-xs rounded bg-gray-800 text-gray-300 hover:bg-gray-700 disabled:opacity-30 disabled:cursor-not-allowed">
            ← Previous Stop
          </button>

          <div class="flex space-x-1">
            ${stops.map((_, i) => `
              <span class="w-2.5 h-2.5 rounded-full ${i === stopIdx ? 'bg-amber-400' : 'bg-gray-700'}"></span>
            `).join("")}
          </div>

          <button onclick="window.storyStudio.renderTourStop(${Math.min(stops.length - 1, stopIdx + 1)})"
            ${stopIdx === stops.length - 1 ? 'disabled' : ''}
            class="px-3.5 py-1.5 text-xs rounded bg-amber-600 text-white hover:bg-amber-500 disabled:opacity-30 disabled:cursor-not-allowed">
            Next Stop →
          </button>
        </div>
      </div>
    `;

    const narrationText = document.getElementById("narrationTextInput");
    if (narrationText) {
      narrationText.value = `${stop.name}. ${stop.narrative}`;
    }
  }
}

window.storyStudio = new InteractiveStoryStudio();
