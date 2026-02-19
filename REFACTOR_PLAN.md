# Coworker - Refactoring Plan

## Ziel
Eine saubere, einfache Chat-App mit Sidebar (Projekte + Chats + Tasks), einem aufgeräumten Chat-Bereich und nur den nötigen Einstellungen. Der Agent fühlt sich wie ein **Teammitglied** an, nicht wie ein technisches Tool. Alle Agent-Funktionen bleiben im Backend vollständig erhalten.

**Name:** Coworker
**Branding:** Oranges "C" als Icon/Logo
**Vorgehen:** Erst aufräumen (Phase 1-4), dann UI-Redesign als separates Projekt

---

## 1. Settings vereinfachen

### Neue Tab-Struktur (4 Tabs statt 6):

| Tab | Inhalt |
|-----|--------|
| **Agent** | Agent-Name/Beschreibung, Chat-Model (= Utility + Browser), Embedding-Model (separat), Memory-Config, Speech-Config (nur STT/Mikrofon), Workdir |
| **API Keys** | Globale Model-API-Keys (OpenAI, Anthropic, Google, AssemblyAI etc.) - projektübergreifend |
| **Skills** | Skills auflisten, importieren, verwalten |
| **MCP** | Externe MCP-Server konfigurieren |

### Entfernen aus Settings:
- [ ] **Developer Tab** komplett (WebSocket-Konsole, API-Testing)
- [ ] **A2A Konfiguration** (aus MCP/A2A Tab)
- [ ] **Backup & Restore Tab** komplett
- [ ] **Tunnel / Flare** Konfiguration
- [ ] **Update Checker**
- [ ] **External API** Konfiguration
- [ ] **Authentication** Settings
- [ ] **LiteLLM** Settings
- [ ] **Separate Utility Model** Konfiguration (wird Chat-Model)
- [ ] **Separate Browser Model** Konfiguration (wird Chat-Model)
- [ ] **Kokoro TTS Toggle** (TTS wird komplett entfernt)

### Zusammenführen:
- [ ] Chat-Model, Utility-Model und Browser-Model → **ein Model-Setting** ("Chat Model")
- [ ] Embedding-Model bleibt als **separates Setting**

---

## 2. Chat-UI aufräumen

### Bottom Actions (vereinfacht):
Behalten:
- [x] Pause/Resume
- [x] Save Chat
- [x] Files (File Browser)
- [x] Knowledge Import
- [x] Speech (Mikrofon)

Entfernen:
- [ ] **Context Window Viewer** Button
- [ ] **History Viewer** Button (JSON)
- [ ] **Nudge** Button

Verschieben:
- [ ] **Clear Chat** → in Sidebar Quick Actions Menü

### Message-Darstellung vereinfachen:
- [ ] Technische Agent-Schritte (Tool-Calls, Code-Ausführung, Browser-Actions etc.) standardmäßig **zugeklappt** hinter einem einfachen "Arbeitet..."-Indikator
- [ ] Nur das **Endergebnis** (Response) wird prominent angezeigt
- [ ] Process Groups optional aufklappbar für Transparenz, aber default = zu
- [ ] Weniger Message-Types sichtbar: User-Nachrichten + Agent-Antworten als Hauptansicht
- [ ] Errors/Warnings vereinfacht darstellen (kein technisches Stack-Trace)

### Weitere Chat-UI Änderungen:
- [ ] **Message Queue Display** entfernen
- [ ] **Process Step Detail Modal** (Raw JSON Ansicht) entfernen
- [ ] Agent-Profil-Auswahl entfernen (keine Hacker/Researcher/Developer Profile)

---

## 3. Speech umbauen

### TTS (Text-to-Speech) komplett entfernen:
- [ ] `python/helpers/kokoro_tts.py` - Helper löschen
- [ ] `python/api/synthesize.py` - API-Endpoint löschen
- [ ] TTS-Logik aus `webui/components/chat/speech/speech-store.js` entfernen (~200 Zeilen)
- [ ] Kokoro-Toggle aus `webui/components/settings/agent/speech.html` entfernen
- [ ] Kokoro Dependencies aus `requirements.txt` entfernen (kokoro, soundfile, etc.)
- [ ] TTS-bezogene Einstellungen aus `python/helpers/settings.py` entfernen

### STT von Whisper auf AssemblyAI umstellen:
- [ ] Neuen Helper erstellen: `python/helpers/assemblyai_stt.py`
  - AssemblyAI REST API nutzen (Audio upload → Transkription)
  - Einfache Aufnahme (kein Real-Time Streaming)
- [ ] `python/api/transcribe.py` anpassen → AssemblyAI statt Whisper nutzen
- [ ] `python/helpers/whisper.py` entfernen
- [ ] `pip install assemblyai` zu requirements.txt hinzufügen
- [ ] Whisper Dependencies aus `requirements.txt` entfernen
- [ ] AssemblyAI API-Key in die globalen API Keys aufnehmen

### Speech-Settings danach:
- Mikrofon-Auswahl (Gerät)
- Sprache
- Silence Threshold
- Silence Duration
- (AssemblyAI API-Key unter globalen API Keys)

---

## 4. Branding → "Coworker"

- [ ] "Agent Zero" → "Coworker" überall im UI umbenennen
- [ ] Oranges "C" als Logo/Icon erstellen (SVG)
- [ ] Sidebar-Header: Logo + "Coworker" Schriftzug
- [ ] Welcome Screen: Neues Branding
- [ ] Browser-Tab Titel → "Coworker"
- [ ] Favicon → Oranges C
- [ ] PWA Manifest (`manifest.json`) → Name, Icons, Theme-Color (Orange)

---

## 5. Login entfernen

- [ ] Login-Seite (`login.html`) entfernen oder bypassen
- [ ] Authentication-Logik im Backend deaktivieren/entfernen
- [ ] Direkt auf Chat-Interface laden
- [ ] Logout-Button aus Sidebar entfernen

---

## 6. Sidebar & Navigation

### Behalten:
- [x] Projekt-Selector (oben)
- [x] Chat-Liste
- [x] Task-Liste (Scheduler)
- [x] Quick Actions (Dashboard, Memory, Scheduler, Settings + Clear Chat)
- [x] Preferences (Theme etc.)

### Aufräumen:
- [ ] Sidebar Footer vereinfachen (Versionsnummer/technische Infos entfernen)
- [ ] Clear Chat in Quick Actions verschieben

### Welcome Screen:
- [ ] Vereinfachen - nur relevante Quick Actions zeigen
- [ ] Neues Branding einsetzen

---

## 7. Modals die bleiben

- [x] Memory Dashboard
- [x] Scheduler
- [x] File Browser
- [x] Project Management (komplett mit Instructions, Memory, Secrets, Skills, File Structure)
- [x] Settings (vereinfacht, 4 Tabs)
- [x] Notifications
- [x] Image Viewer
- [x] Full-Screen Input

### Modals die entfallen:
- [ ] Context Window Modal
- [ ] History Modal (JSON)
- [ ] Process Step Detail Modal (JSON)

---

## 8. Projekt-System (bleibt komplett)

- [x] Name, Beschreibung, Farbe
- [x] Custom Instructions
- [x] Memory (isoliert pro Projekt)
- [x] Secrets (projekt-spezifisch)
- [x] Skills (pro Projekt zuweisbar)
- [x] File Structure

API Keys für Modelle sind **global** (nicht pro Projekt).

---

## 9. Backend - KEINE funktionalen Änderungen

Alle Agent-Funktionen bleiben vollständig erhalten:
- Code-Ausführung (Python, Node.js, Shell)
- Web-Suche (SearXNG)
- Browser-Automation
- Sub-Agents / Delegation
- Memory (Save/Load/Delete/Forget)
- Knowledge Base (FAISS + Embeddings)
- Alle 19 Tools
- Alle Extensions
- Scheduler
- File-Operationen
- MCP Client
- Skills

Nur die API-Endpoints für entfernte Features werden bereinigt:
- `/synthesize` (TTS) → entfernen
- `/transcribe` → auf AssemblyAI umstellen
- Auth-Endpoints → entfernen/deaktivieren

---

## 10. Dependencies bereinigen

### Entfernen:
- [ ] Kokoro TTS (`kokoro`, `soundfile`, etc.)
- [ ] Whisper (`whisper`, `openai-whisper`)
- [ ] `transformers@3.0.2.js` im Frontend (748KB, nur für lokale ML-Inference)
- [ ] Weitere unbenutzte Dependencies identifizieren

### Hinzufügen:
- [ ] `assemblyai` Python SDK

---

## 11. Dateien-Übersicht

### Hauptsächlich betroffene Frontend-Dateien:
```
webui/components/settings/          → Tabs reduzieren, Settings zusammenführen
webui/components/chat/input/        → Bottom Actions aufräumen
webui/components/chat/speech/       → TTS entfernen, STT vereinfachen
webui/components/modals/            → Context, History, Process-Detail entfernen
webui/components/messages/          → Process Groups default zugeklappt
webui/components/welcome/           → Vereinfachen + Branding
webui/components/sidebar/           → Footer aufräumen, Clear Chat verschieben
webui/components/settings/agent/    → Speech Settings anpassen
webui/js/messages.js                → Message-Rendering vereinfachen
webui/index.html                    → Branding, Login entfernen
webui/js/manifest.json              → PWA Branding
```

### Backend-Dateien:
```
python/helpers/kokoro_tts.py        → Löschen
python/helpers/whisper.py           → Löschen
python/helpers/assemblyai_stt.py    → Neu erstellen
python/api/synthesize.py            → Löschen
python/api/transcribe.py            → AssemblyAI Integration
python/helpers/settings.py          → TTS Settings entfernen
python/api/login.py                 → Deaktivieren/entfernen
requirements.txt                    → Kokoro/Whisper raus, AssemblyAI rein
```

---

## Reihenfolge der Umsetzung

### Phase 1: Settings vereinfachen
- Tabs reduzieren (6 → 4)
- Models zusammenführen (Chat = Utility = Browser)
- Unnötige Settings entfernen

### Phase 2: Chat-UI aufräumen
- Bottom Actions reduzieren
- Technische Modals entfernen
- Message-Darstellung vereinfachen (Process Groups default zu)
- Message Queue Display entfernen

### Phase 3: Speech umbauen
- TTS komplett entfernen
- AssemblyAI Helper erstellen
- Transcribe Endpoint umstellen
- Speech Settings anpassen

### Phase 4: Login & Auth entfernen
- Login-Seite deaktivieren
- Direkt auf Chat laden
- Auth-Endpoints bereinigen

### Phase 5: Branding "Coworker"
- Agent Zero → Coworker umbenennen
- Oranges "C" als Logo/Favicon/PWA-Icon
- Welcome Screen + Sidebar anpassen
- Sidebar Footer aufräumen
- Dependencies bereinigen
- Testen

---

## Danach: UI-Redesign (separates Projekt)
Nach dem Aufräumen wird die UI visuell überarbeitet (Layout, Farben, Typografie, UX).
Wird als eigener Plan erarbeitet sobald das Aufräumen abgeschlossen ist.
