# Cowork UI Redesign - Implementierungsplan

## 🎯 Ziel
Modernes, elegantes UI-Design mit neuem Farbschema (Midnight Navy, Champagne, Dusty Rose) bei **vollständiger Erhaltung aller bestehenden Funktionen**.

---

## 📋 Anforderungen

### MUST HAVE (Funktionen müssen erhalten bleiben)

#### Sidebar
- [ ] Header Icons: Menu Toggle + Logo
- [ ] Quick Actions: 5 Icons (Dashboard, Memory, Scheduler, Settings, Dropdown)
- [ ] Quick Actions Dropdown: Projects, New Chat, Load Chat, Save Chat, Clear Chat
- [ ] Chats List: Collapsible, Aktive-Auswahl, 3-Punkte-Menü
- [ ] Tasks List: Collapsible, Status-Badges, Task-Aktionen
- [ ] Preferences Panel: Dark Mode Toggle, Chat Width, Detail Mode, Speech
- [ ] Version Info: Versionsnummer + Datum

#### Chat-Bereich
- [ ] Chat Top: Zeit/Datum, Sync Status, Project Selector
- [ ] Input Area: Textarea, Send Button, Mic Button, Attachment
- [ ] Bottom Actions: Pause/Resume, Save, Import, Files
- [ ] Progress Bar: Fortschrittsanzeige + Navigation
- [ ] Attachments: Drag & Drop Overlay, Preview
- [ ] Message Queue: Warteschlange-Anzeige

#### Messages
- [ ] User Messages: Rechtsbündig, eigener Stil
- [ ] AI Messages: Links, verschiedene Typen (agent, tool, code-exe, etc.)
- [ ] Process Groups: Expandable/Collapsible mit Animation
- [ ] Badges: Status-Badges (GEN, END, USE, etc.)
- [ ] Code Blocks: Syntax Highlighting, Copy Button
- [ ] Tables: Markdown Tables Styling

#### Modals
- [ ] Settings: Tabs (Agent, External, MCP, Skills)
- [ ] File Browser: Upload, Download, Rename, Navigate
- [ ] File Editor: ACE Editor Integration
- [ ] Memory Dashboard: Suche, Filter, Mass Actions
- [ ] Scheduler: Task List, Editor, Detail View
- [ ] Image Viewer: Zoom, Pan
- [ ] Process Step Detail: KVPs, Raw JSON

#### Projects
- [ ] Project Selector: Dropdown mit aktivem Projekt
- [ ] Project List: Cards mit Farben
- [ ] Project Create/Edit: Formular mit Tabs

#### Notifications
- [ ] Notification Icons: Badge mit Counter
- [ ] Notification Modal: Liste mit Details
- [ ] Toast Stack: Popup-Benachrichtigungen

### SHOULD HAVE (Design-Verbesserungen)
- [ ] Glassmorphism Effekte
- [ ] Verbesserte Animationen
- [ ] Neues Farbschema (60-30-10 Regel)
- [ ] Bessere Typografie
- [ ] Verbesserte Hover-States

---

## 🎨 Design-System (Neu)

### Farbschema

```css
/* Primary Colors */
--color-navy: #192A56;
--color-navy-dark: #0F1A36;
--color-navy-light: #1E3160;
--color-champagne: #F7D794;
--color-rose: #EDA6A3;
--color-pearl: #FCFBFB;

/* Semantic (Dark Mode) */
--color-bg: var(--color-navy-dark);
--color-surface: var(--color-navy);
--color-surface-hover: rgba(247, 215, 148, 0.08);
--color-text: var(--color-pearl);
--color-text-secondary: rgba(252, 251, 251, 0.65);
--color-text-muted: rgba(252, 251, 251, 0.45);
--color-accent: var(--color-rose);
--color-border: rgba(247, 215, 148, 0.12);
```

### Layout-Variablen

```css
--sidebar-width: 280px;
--sidebar-collapsed: 72px;
--radius-sm: 8px;
--radius-md: 12px;
--radius-lg: 16px;
--radius-xl: 20px;
```

---

## 🗂️ Implementierungs-Phasen

### Phase 1: Foundation (Sicher)
**Ziel:** Design Tokens einführen, bestehendes Design nicht brechen

| Datei | Änderungen |
|-------|------------|
| `webui/index.css` | Neue CSS-Variablen hinzufügen, bestehende behalten |
| `webui/index.html` | Keine Änderungen |

**Aufgaben:**
1. Neue CSS-Variablen am Ende von `:root` hinzufügen
2. Keine bestehenden Variablen entfernen
3. Testen: Alles funktioniert noch?

**Zeitschätzung:** 1-2 Stunden
**Risiko:** Sehr niedrig

---

### Phase 2: Sidebar Redesign (Kritisch)
**Ziel:** Sidebar mit neuem Design, alle Funktionen erhalten

| Komponente | Datei | Änderungen |
|------------|-------|------------|
| Left Sidebar | `components/sidebar/left-sidebar.html` | Neue Farben, Gradient-Hintergrund |
| Header Icons | `components/sidebar/top-section/header-icons.html` | Neues Logo-Design, Toggle-Button Style |
| Quick Actions | `components/sidebar/top-section/quick-actions.html` | Neue Button-Styles, Dropdown-Styling |
| Chats List | `components/sidebar/chats/chats-list.html` | Neue Chat-Item Styles |
| Tasks List | `components/sidebar/tasks/tasks-list.html` | Neue Task-Item Styles, Badges |
| Preferences | `sidebar/bottom/preferences/preferences-panel.html` | Neue Toggle-Styles |
| Sidebar Bottom | `components/sidebar/bottom/sidebar-bottom.html` | Footer-Styling |

**Funktionen die erhalten bleiben müssen:**
- `$store.sidebar.isOpen`, `isCollapsed`, `toggle()`
- `$store.sidebar.isSectionOpen()`, `toggleSection()`
- `$store.sidebar.updateDropdownPosition()`
- `$store.chats.newChat()`, `selectChat()`, `killChat()`
- `$store.tasks.selectTask()`, `openDetail()`, `reset()`, `deleteTask()`
- Bootstrap Collapse für Sections
- Alle Event Handler

**Zeitschätzung:** 4-6 Stunden
**Risiko:** Mittel (viele Interaktionen)

---

### Phase 3: Chat Input Bereich
**Ziel:** Input-Bereich modernisieren

| Komponente | Datei | Änderungen |
|------------|-------|------------|
| Chat Bar | `components/chat/input/chat-bar.html` | Neuer Container-Style |
| Chat Bar Input | `components/chat/input/chat-bar-input.html` | Neue Input-Styles, Button-Styles |
| Bottom Actions | `components/chat/input/bottom-actions.html` | Neue Button-Styles |
| Progress | `components/chat/input/progress.html` | Progress-Bar Styling |
| Attachments | `components/chat/attachments/*.html` | Preview-Styles |
| Message Queue | `components/chat/message-queue/*.html` | Queue-Styles |

**Funktionen die erhalten bleiben müssen:**
- `$store.chatInput.sendMessage()`, `pauseAgent()`
- `$store.speech.handleMicrophoneClick()`, `stop()`
- `$store.chatAttachments`
- `$store.messageQueue`
- `$store.chatNavigation`
- ACE Editor Integration (Full Screen Input)

**Zeitschätzung:** 3-4 Stunden
**Risiko:** Niedrig-Mittel

---

### Phase 4: Messages & Process Groups
**Ziel:** Nachrichten-Design überarbeiten

| Komponente | Datei | Änderungen |
|------------|-------|------------|
| Messages CSS | `css/messages.css` | Neue Message-Styles |
| Process Group | `components/messages/process-group/*.css` | Neue Badge-Styles, Animationen |

**Funktionen die erhalten bleiben müssen:**
- `.message-user`, `.message-agent`, `.message-tool`, etc.
- `.process-group` Expand/Collapse
- `.step-badge` System (GEN, END, USE, etc.)
- `.message-collapsible` mit Fade-Out
- Smooth Render Animationen

**Zeitschätzung:** 3-4 Stunden
**Risiko:** Mittel (viele Message-Typen)

---

### Phase 5: Welcome Screen
**Ziel:** Startbildschirm modernisieren

| Komponente | Datei | Änderungen |
|------------|-------|------------|
| Welcome | `components/welcome/welcome-screen.html` | Neue Card-Styles, Input-Styles |

**Funktionen die erhalten bleiben müssen:**
- `$store.welcomeStore.executeAction()`
- Banner-System (info, warning, error)
- Action Cards Grid

**Zeitschätzung:** 1-2 Stunden
**Risiko:** Niedrig

---

### Phase 6: Modals
**Ziel:** Modal-Grundstyling überarbeiten

| Komponente | Datei | Änderungen |
|------------|-------|------------|
| Modals CSS | `css/modals.css` | Neue Modal-Styles |
| Settings | `components/settings/settings.html` | Tab-Styles |
| File Browser | `components/modals/file-browser/*.html` | List-Styles |
| Memory | `components/modals/memory/*.html` | Table-Styles |
| Scheduler | `components/modals/scheduler/*.html` | Form-Styles |

**Funktionen die erhalten bleiben müssen:**
- Alle Modal-Öffnungs-/Schließ-Logiken
- `$store.*` für alle Modals
- Form-Validierungen
- ACE Editor in Context/File Editor

**Zeitschätzung:** 4-6 Stunden
**Risiko:** Mittel (viele Modals)

---

### Phase 7: Projects & Notifications
**Ziel:** Restliche Komponenten

| Komponente | Datei | Änderungen |
|------------|-------|------------|
| Projects | `components/projects/*.html` | Card-Styles, Form-Styles |
| Notifications | `components/notifications/*.html` | Toast-Styles, Badge-Styles |
| Sync | `components/sync/*.html` | Status-Icon-Styles |

**Zeitschätzung:** 2-3 Stunden
**Risiko:** Niedrig

---

### Phase 8: Testing & Polishing
**Ziel:** Alles testen und fixen

- [ ] Dark Mode funktioniert
- [ ] Light Mode funktioniert
- [ ] Sidebar Collapse funktioniert
- [ ] Alle Modals öffnen/schließen
- [ ] Chat-Verlauf wird korrekt angezeigt
- [ ] Process Groups expand/collapse
- [ ] Task-Status werden angezeigt
- [ ] Preferences werden gespeichert
- [ ] Mobile Ansicht (optional)

**Zeitschätzung:** 2-4 Stunden
**Risiko:** Unbekannt (Bugfixing)

---

## 📝 Checkliste pro Komponente

Für jede geänderte Komponente muss geprüft werden:

```markdown
- [ ] HTML-Struktur unverändert (keine Elemente entfernt)
- [ ] Alle `x-data` Attribute vorhanden
- [ ] Alle `@click` Handler funktionieren
- [ ] Alle `$store.*` Verbindungen funktionieren
- [ ] Alle `x-show` / `x-if` Konditionen funktionieren
- [ ] Bootstrap Collapse funktioniert (wo verwendet)
- [ ] Neue CSS-Klassen sind spezifisch genug
- [ ] Dark Mode sieht gut aus
- [ ] Light Mode sieht gut aus
```

---

## 🔄 Rollback-Strategie

Falls etwas schiefgeht:

1. **Git-History:** Alle Änderungen in einem separaten Branch
2. **CSS-Backups:** Originale CSS-Dateien vorher kopieren
3. **Inkrementell:** Phase für Phase commiten
4. **Feature-Flags:** Neue Styles könnten hinter CSS-Variable versteckt werden

---

## 📊 Zeitschätzung Gesamt

| Phase | Zeit | Risiko |
|-------|------|--------|
| Phase 1: Foundation | 1-2h | Sehr niedrig |
| Phase 2: Sidebar | 4-6h | Mittel |
| Phase 3: Chat Input | 3-4h | Niedrig-Mittel |
| Phase 4: Messages | 3-4h | Mittel |
| Phase 5: Welcome | 1-2h | Niedrig |
| Phase 6: Modals | 4-6h | Mittel |
| Phase 7: Projects/Notifications | 2-3h | Niedrig |
| Phase 8: Testing | 2-4h | Unbekannt |
| **Gesamt** | **20-31h** | **Mittel** |

---

## ✅ Freigabe

Dieser Plan muss vom Benutzer freigegeben werden, bevor die Implementierung beginnt.

**Fragen an den Benutzer:**
1. Stimmt die Priorisierung der Phasen?
2. Sollen wir mit Phase 1 beginnen?
3. Sollen bestimmte Features anders priorisiert werden?
4. Gibt es Design-Elemente, die anders aussehen sollen?
