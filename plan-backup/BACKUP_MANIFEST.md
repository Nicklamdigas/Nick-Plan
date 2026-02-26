# Nick's Career Plan — Backup Manifest
**Created:** 2026-02-25  
**Purpose:** Complete snapshot of all files related to the 12-week learning plan and career prep.  
**Backed up from:** `C:\Nick\career-plan\`, `C:\Nick\projects\dev-journal\`, `C:\Nick\Learning-Resources\`

---

## Folder Structure

```
plan-backup/
├── BACKUP_MANIFEST.md                    ← this file
├── plan.md                               ← MASTER 12-week career plan (start here)
├── session-context.md                    ← AI session resume file (paste into new AI sessions)
├── life_os_v5.1.html                     ← Life OS dashboard (open in browser)
├── git-cheatsheet.md                     ← Git command reference
├── git-identity-setup.md                 ← How to configure Git identity
│
├── roadmaps/                             ← 9 self-teaching roadmap PDFs from roadmap.sh
│   ├── python.pdf                        ← PRIORITY 1 — start here
│   ├── computer-science.pdf              ← PRIORITY 2
│   ├── datastructures-and-algorithms.pdf ← PRIORITY 3
│   ├── full-stack.pdf                    ← PRIORITY 4
│   ├── backend.pdf                       ← PRIORITY 5
│   ├── linux.pdf                         ← PRIORITY 6
│   ├── devops.pdf                        ← PRIORITY 7 (Docker + CI/CD parts only)
│   ├── system-design.pdf                 ← PRIORITY 8
│   └── aws.pdf                           ← PRIORITY 9 (Phase 5+, not yet)
│
├── dev-journal/                          ← Daily learning journal entries
│   ├── 2026-02-24.md                     ← Day 1 entry (first day of break)
│   ├── README.md                         ← Journal repo README
│   └── push-to-github.ps1               ← Script to push journal to GitHub
│
├── learning-resources/                   ← Planning documents from earlier sessions
│   ├── 01-MASTER-PLAN-18-Month-Python-Journey.md   ← First-ever plan (superseded by plan.md)
│   ├── 02-Visual-Programming-Course-Plan.md         ← Zetech Visual Prog study plan
│   ├── 03-Ubuntu-Copilot-Installation-Guide.md      ← Ubuntu dev environment setup
│   ├── 04-Ubuntu-Session-Quick-Start.md             ← Quick start for Ubuntu sessions
│   ├── 05-Ubuntu-Primary-Development-Strategy.md    ← Original strategy doc (superseded)
│   └── README.md                                    ← Overview of learning resources folder
│
└── session-records/                      ← AI session history and notes
    ├── session-plan.md                   ← Current session working plan
    └── checkpoint-001.md                 ← Checkpoint: Roadmap Integration + Life OS v5 upgrade
```

---

## What Each Key File Is

### `plan.md` — THE master document
The single source of truth for the 12-week learning plan. Contains:
- Roadmap priority table (which PDFs to follow in what order)
- Phase 0–5 breakdown with topics, resources, and projects
- Week-by-week schedule (Weeks 1–12)
- CV template
- Kenya tech networking contacts
- Anti-AI-crutch rules

**If you lose everything else, keep this file.**

### `session-context.md` — Resume file for AI sessions
Paste this into any new AI chat session to restore full context.  
The `WHERE WE STOPPED` section at the bottom is the most important part.

### `life_os_v5.1.html` — Daily dashboard
Open in any browser (double-click the file). No internet needed for core features.  
Features:
- **Schedule tab** — weekly calendar with Break mode (current) and School mode (May onwards)
- **Today Focus bar** — shows what you should be doing RIGHT NOW and what's NEXT
- **Roadmap tab** — all 5 phases with checkboxes to track progress
- **Habit Tracker** — daily freecodecamp the python certification / LeetCode / GitHub / Journal tracking with streak
- **Quick Journal Note** — type a daily note, auto-saved in the browser
- **Week Deep Dive** — detailed breakdown of each week's goals

---

## What's Not In This Backup

| Item | Location | Why not included |
|------|----------|-----------------|
| `academic_automator/` project | `C:\Nick\projects\academic_automator\` | Has its own `.git` — back up separately with `git push` |
| `academic_link/` project | `C:\Nick\projects\academic_link\` | Has its own `.git` — back up separately |
| Books (PDFs) | `C:\Nick\Books\` | 8 reference books, large files — back up separately to USB/Drive |
| `Y3S1/` university notes | `C:\Nick\Y3S1\` | Not part of the career plan |

---

## How To Restore From This Backup

1. Copy the entire `plan-backup/` folder to a USB drive or Google Drive
2. To restore: copy files back to their original locations:
   - `plan.md` → `C:\Nick\career-plan\plan.md`
   - `session-context.md` → `C:\Nick\career-plan\session-context.md`
   - `life_os_v5.1.html` → rename to `life_os_v4.html` and copy to `C:\Nick\career-plan\`
   - `roadmaps/` → copy PDFs back to `C:\Nick\career-plan\Self-Teaching roadmaps\`
3. Dev journal entries → `C:\Nick\projects\dev-journal\`

---

## Backup Recommendation

**Do this weekly** — copy the updated files to:
- USB drive (keep one at home, one in your bag)
- Google Drive or OneDrive
- Push `plan.md` and `session-context.md` to a private GitHub repo

The habit tracker and roadmap checkbox data lives in your **browser's localStorage** — it is NOT in these files. If you clear your browser or use a different computer, that data resets. The files here are the permanent record.

---

*Last updated: 2026-02-25 | Nick Lamdigas | Zetech University | Software Engineering Y3S1*
