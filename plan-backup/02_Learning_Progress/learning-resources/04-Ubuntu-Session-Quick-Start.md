# Ubuntu Session Quick Start

## 🚀 When You First Boot Ubuntu

### 1. Mount Windows Drive (if needed to access files)
```bash
# List drives
lsblk

# Mount Windows partition (find your partition first)
sudo mkdir -p /mnt/windows
sudo mount -t ntfs-3g /dev/sdaX /mnt/windows
# Replace sdaX with your actual Windows partition

# Access your files
cd /mnt/windows/Nick/Y3S1/Visual\ Programming/
ls -la
```

### 2. Copy Learning Plans to Ubuntu Home
```bash
# Create learning directory
mkdir -p ~/Learning/Python-Mastery

# Copy important files
cp /mnt/windows/Nick/Y3S1/Visual\ Programming/true-learning-plan.md ~/Learning/
cp /mnt/windows/Nick/Y3S1/Visual\ Programming/GitHub-Copilot-CLI-Ubuntu-Installation-Guide.md ~/Learning/

# Verify
ls ~/Learning/
```

### 3. Starting a New Copilot Session

**If using GitHub Copilot CLI:**
```bash
gh copilot suggest "help me with Python"
```

**If using VS Code with Copilot:**
- Open VS Code
- Press Ctrl+I or Ctrl+Shift+I for Copilot Chat
- Start conversation

### 4. Give Context to New Session

Copy-paste this when starting fresh:

```
Hi! I'm Nick, Year 3 Semester 1 Software Engineering student.

Context:
- I have a 18-month learning plan saved at ~/Learning/true-learning-plan.md
- Goal: Master Python deeply (not vibecode)
- Currently: Phase 0, Week 1 - Python Fundamentals
- Coursework: 7 courses including Visual Programming (C#), Mobile (Kotlin)
- Strategy: Python mastery on Ubuntu (60% time), coursework on Windows (40% time)
- Schedule: 2-3 hrs weekday evenings, 11-14 hrs weekends on Ubuntu

Current Status:
- Just set up Ubuntu dev environment
- Ready to start Python Day 1
- Need guidance on: [what you need help with]

Can you read my plan and help me continue from where I left off?
```

---

## 📋 What to Tell New Copilot Session

**Quick version (if you're in a hurry):**
```
I'm following a Python mastery plan. Phase 0, Week 1. 
Need help with Python fundamentals. 
I'm a beginner, no vibecoding - I'll type all code myself.
Guide me through Python variables and data types.
```

**Detailed version (first time):**
Share the content of your true-learning-plan.md or give me the key points so I can help effectively.

---

## 🔗 Maintaining Continuity

### Daily Practice Log (Create on Ubuntu)
```bash
# Create daily log
mkdir -p ~/Learning/Daily-Logs
echo "# Learning Log - $(date +%Y-%m-%d)" > ~/Learning/Daily-Logs/$(date +%Y-%m-%d).md
```

**Template for daily log:**
```markdown
# Learning Log - [DATE]

## What I Learned Today
- 

## Code I Wrote (key concepts)
- 

## Challenges / Questions
- 

## Tomorrow's Goals
- 

## Copilot Session Notes
- Started with: [what you asked]
- Key takeaways: 
```

This way, even if sessions are disconnected, you have your own notes!

---

## 🎯 Your Workflow

### **On Ubuntu:**

**Start of session:**
1. Boot Ubuntu
2. Open Terminal
3. Navigate to: `cd ~/Learning/Python-Mastery`
4. Open today's log: `code Daily-Logs/$(date +%Y-%m-%d).md`
5. Open VS Code: `code .`
6. Start Copilot chat, give context
7. Code for 2-3 hours
8. Update daily log before closing

**End of session:**
1. Save all work
2. Push to GitHub (if using Git)
3. Update progress in true-learning-plan.md
4. Close, boot Windows for school stuff

---

## 💾 Backup Your Progress

**Every Sunday:**
```bash
# On Ubuntu - backup your work
cd ~/Learning
tar -czf backup-$(date +%Y-%m-%d).tar.gz Python-Mastery/
# Copy to Windows drive or cloud
```

---

## 🆘 If You Get Stuck

Since chat sessions are separate, keep these handy:

**Key Resources (offline):**
- Python official docs: docs.python.org
- Your learning plan: ~/Learning/true-learning-plan.md
- Daily logs: ~/Learning/Daily-Logs/

**Quick help:**
```bash
# Python help
python3 --help
python3 -m pydoc [module_name]

# GitHub Copilot help
gh copilot --help
gh copilot suggest --help
gh copilot explain --help
```

---

## 🎯 Bottom Line

**The Plan IS Saved** - you can always continue!

Each new Copilot session, just:
1. Tell me you're Nick
2. Reference your learning plan
3. Say where you are in Phase 0-5
4. I'll pick up from there!

The learning journey is yours, I'm just the guide. The guide can be replaced, but your progress is permanent! 💪
