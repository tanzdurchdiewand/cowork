# Cowork UI Redesign - Implementierungsplan

## 🎯 Ziel
Modernes, elegantes UI-Design mit neuem Farbschema bei **vollständiger Erhaltung aller bestehenden Funktionen**.

---

## 🎨 FINALES DESIGN-SYSTEM

### 3-Farben-System pro Mode (60-30-10 Regel)

#### 🌙 DARK MODE (Luxury & Elegant)

| Prozent | Farbe | Hex | Verwendung |
|---------|-------|-----|------------|
| **60%** | Midnight Navy | #192A56 | Hintergrund, Surface, Panels |
| **30%** | Pearl White | #FCFBFB | Text, Content, Icons |
| **10%** | Dusty Rose | #EDA6A3 | **Alle Akzente**: CTA, Buttons, Logo, Mic, Send, Badges, Glow |

**CSS Variablen:**
```css
--lux-navy: #192A56;
--lux-rose: #EDA6A3;
--lux-pearl: #FCFBFB;
```

#### ☀️ LIGHT MODE (Earthy & Organic)

| Prozent | Farbe | Hex | Verwendung |
|---------|-------|-----|------------|
| **60%** | Warm Beige | #F5E6CC | Hintergrund, Surface, Panels |
| **30%** | Forest Green | #2D4F1E | Text, Content, Icons |
| **10%** | Terracotta | #E27D60 | **Alle Akzente**: CTA, Buttons, Logo, Mic, Send, Badges, Glow |

**CSS Variablen:**
```css
--earth-green: #2D4F1E;
--earth-beige: #F5E6CC;
--earth-terracotta: #E27D60;
```

### Aktivierung
```html
<!-- Dark Mode (Default) -->
<body class="new-design">

<!-- Light Mode -->
<body class="new-design light-mode">
```

---

## 📋 MUST HAVE - Funktionen die erhalten bleiben

### Sidebar
- [x] Header Icons: Menu Toggle + Logo
- [x] Quick Actions: 5 Icons (Dashboard, Memory, Scheduler, Settings, Dropdown)
- [x] Quick Actions Dropdown: Projects, New Chat, Load Chat, Save Chat, Clear Chat
- [x] Chats List: Collapsible, Aktive-Auswahl, 3-Punkte-Menü
- [x] Tasks List: Collapsible, Status-Badges, Task-Aktionen
- [x] Preferences Panel: Dark Mode Toggle, Chat Width, Detail Mode, Speech
- [x] Version Info: Versionsnummer + Datum

### Chat-Bereich
- [x] Chat Top: Zeit/Datum, Sync Status, Project Selector
- [x] Input Area: Textarea, Send Button, Mic Button, Attachment
- [x] Bottom Actions: Pause/Resume, Save, Import, Files
- [x] Progress Bar: Fortschrittsanzeige + Navigation
- [x] Attachments: Drag & Drop Overlay, Preview
- [x] Message Queue: Warteschlange-Anzeige

### Messages
- [x] User Messages: Rechtsbündig, eigener Stil
- [x] AI Messages: Links, verschiedene Typen (agent, tool, code-exe, etc.)
- [x] Process Groups: Expandable/Collapsible mit Animation
- [x] Badges: Status-Badges (GEN, END, USE, etc.) - mit 10% Farbe
- [x] Code Blocks: Syntax Highlighting, Copy Button
- [x] Tables: Markdown Tables Styling

### Modals
- [x] Settings: Tabs (Agent, External, MCP, Skills)
- [x] File Browser: Upload, Download, Rename, Navigate
- [x] File Editor: ACE Editor Integration
- [x] Memory Dashboard: Suche, Filter, Mass Actions
- [x] Scheduler: Task List, Editor, Detail View
- [x] Image Viewer: Zoom, Pan
- [x] Process Step Detail: KVPs, Raw JSON

### Projects & Notifications
- [x] Project Selector: Dropdown mit aktivem Projekt
- [x] Project List: Cards mit Farben
- [x] Project Create/Edit: Formular mit Tabs
- [x] Notification Icons: Badge mit Counter
- [x] Notification Modal: Liste mit Details
- [x] Toast Stack: Popup-Benachrichtigungen

---

## 🗂️ IMPLEMENTIERUNGS-PHASEN

### Phase 1: ✅ FOUNDATION (Abgeschlossen)
**Was:** Design Tokens einfügen

| Datei | Änderungen |
|-------|------------|
| `webui/index.css` | Neue CSS-Variablen für 3-Farben-System |
| `webui/index.html` | `new-design` Klasse zum Body hinzugefügt |

**Ergebnis:**
- ✅ 3 Farben für Dark Mode (Navy, Pearl, Rose)
- ✅ 3 Farben für Light Mode (Beige, Green, Terracotta)
- ✅ Logo, Icons, Buttons verwenden 10% Akzentfarbe
- ✅ `.new-design` Klasse aktiviert neues Schema

---

### Phase 2: SIDEBAR REDESIGN (Nächster Schritt)
**Ziel:** Sidebar mit neuem Design, alle Funktionen erhalten

**Betroffene Komponenten:**
| Komponente | Datei | Änderungen |
|------------|-------|------------|
| Left Sidebar | `components/sidebar/left-sidebar.html` | Neue Farben, Gradient-Hintergrund |
| Header Icons | `components/sidebar/top-section/header-icons.html` | Logo in 10% Akzentfarbe |
| Quick Actions | `components/sidebar/top-section/quick-actions.html` | Buttons in 10% Akzentfarbe |
| Chats List | `components/sidebar/chats/chats-list.html` | Aktive Chat-Items mit 10% Farbe |
| Tasks List | `components/sidebar/tasks/tasks-list.html` | Badges, Status-Dots |
| Preferences | `sidebar/bottom/preferences/preferences-panel.html` | Toggle-Switches in 10% Farbe |
| Sidebar Bottom | `components/sidebar/bottom/sidebar-bottom.html` | Footer-Styling |

**Zu erhaltende Funktionen:**
- `$store.sidebar.isOpen`, `isCollapsed`, `toggle()`
- `$store.sidebar.isSectionOpen()`, `toggleSection()`
- Bootstrap Collapse für Sections
- Alle Event Handler
- Dropdown-Menü Positioning

**Zeitschätzung:** 4-6 Stunden

---

### Phase 3: CHAT INPUT BEREICH
**Ziel:** Input-Bereich modernisieren

**Betroffene Komponenten:**
| Komponente | Datei | Änderungen |
|------------|-------|------------|
| Chat Bar | `components/chat/input/chat-bar.html` | Neuer Container-Style |
| Chat Bar Input | `components/chat/input/chat-bar-input.html` | Input-Styles, Send/Mic in 10% Farbe |
| Bottom Actions | `components/chat/input/bottom-actions.html` | Button-Styles |
| Progress | `components/chat/input/progress.html` | Progress-Bar in 10% Farbe |
| Attachments | `components/chat/attachments/*.html` | Preview-Styles |
| Message Queue | `components/chat/message-queue/*.html` | Queue-Styles |

**Zeitschätzung:** 3-4 Stunden

---

### Phase 4: MESSAGES & PROCESS GROUPS
**Ziel:** Nachrichten-Design überarbeiten

**Betroffene Dateien:**
| Datei | Änderungen |
|-------|------------|
| `css/messages.css` | Neue Message-Styles |
| `components/messages/process-group/*.css` | Badges in 10% Farbe |

**Zu erhaltendes:**
- `.message-user`, `.message-agent`, `.message-tool`, etc.
- `.process-group` Expand/Collapse
- `.step-badge` System (GEN, END, USE, etc.) - mit 10% Farbe!
- `.message-collapsible` mit Fade-Out

**Zeitschätzung:** 3-4 Stunden

---

### Phase 5: WELCOME SCREEN
**Ziel:** Startbildschirm modernisieren

| Komponente | Datei | Änderungen |
|------------|-------|------------|
| Welcome | `components/welcome/welcome-screen.html` | Action Cards mit 10% Akzentfarbe, Input-Styles |

**Zeitschätzung:** 1-2 Stunden

---

### Phase 6: MODALS
**Ziel:** Modal-Grundstyling überarbeiten

| Komponente | Datei | Änderungen |
|------------|-------|------------|
| Modals CSS | `css/modals.css` | Neue Modal-Styles |
| Settings | `components/settings/settings.html` | Tab-Styles |
| File Browser | `components/modals/file-browser/*.html` | List-Styles |
| Memory | `components/modals/memory/*.html` | Table-Styles |
| Scheduler | `components/modals/scheduler/*.html` | Form-Styles |

**Zeitschätzung:** 4-6 Stunden

---

### Phase 7: PROJECTS & NOTIFICATIONS
**Ziel:** Restliche Komponenten

| Komponente | Datei | Änderungen |
|------------|-------|------------|
| Projects | `components/projects/*.html` | Cards mit 10% Akzentfarbe |
| Notifications | `components/notifications/*.html` | Toast-Styles, Badge-Styles in 10% Farbe |
| Sync | `components/sync/*.html` | Status-Icon-Styles |

**Zeitschätzung:** 2-3 Stunden

---

### Phase 8: TESTING & POLISHING
**Ziel:** Alles testen und fixen

**Checkliste:**
- [ ] Dark Mode zeigt Navy/Perl/Rose
- [ ] Light Mode zeigt Beige/Green/Terracotta
- [ ] Alle Icons (inkl. Logo) in 10% Akzentfarbe
- [ ] Sidebar Collapse funktioniert
- [ ] Alle Modals öffnen/schließen
- [ ] Chat-Verlauf wird korrekt angezeigt
- [ ] Process Groups expand/collapse
- [ ] Task-Status werden angezeigt
- [ ] Preferences werden gespeichert

**Zeitschätzung:** 2-4 Stunden

---

## 📊 Zeitschätzung Gesamt

| Phase | Zeit | Status |
|-------|------|--------|
| Phase 1: Foundation | 1-2h | ✅ Done |
| Phase 2: Sidebar | 4-6h | 🔄 Next |
| Phase 3: Chat Input | 3-4h | ⏳ Pending |
| Phase 4: Messages | 3-4h | ⏳ Pending |
| Phase 5: Welcome | 1-2h | ⏳ Pending |
| Phase 6: Modals | 4-6h | ⏳ Pending |
| Phase 7: Projects/Notifications | 2-3h | ⏳ Pending |
| Phase 8: Testing | 2-4h | ⏳ Pending |
| **Gesamt** | **20-31h** | **1/8 Done** |

---

## ✅ Freigabe für Phase 2

**Farbschema ist final definiert:**
- ✅ 3 Farben Dark Mode (Navy, Pearl, Rose)
- ✅ 3 Farben Light Mode (Beige, Green, Terracotta)
- ✅ Alle Icons/Buttons/Logo in 10% Akzentfarbe
- ✅ 60-30-10 Regel konsistent angewendet

**Soll ich mit Phase 2 (Sidebar Redesign) beginnen?**
