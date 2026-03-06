# Git Cheat Sheet — Nick's Reference

## The 5 Commands You'll Use Every Single Day

```powershell
git status              # What files have changed? What's staged?
git add .               # Stage ALL changed files for commit
git add filename.py     # Stage ONE specific file
git commit -m "message" # Save a snapshot with a description
git push                # Upload your commits to GitHub
```

## Starting a Project (Two Ways)

### Way 1 — You create the repo on GitHub first (recommended)
```powershell
git clone https://github.com/YourUsername/repo-name.git
cd repo-name
# Start coding. Add, commit, push.
```

### Way 2 — You already have local files
```powershell
cd your-project-folder
git init
git add .
git commit -m "feat: initial commit"
git remote add origin https://github.com/YourUsername/repo-name.git
git push -u origin main
```

## The Daily Workflow (Do This Every Time You Code)

```powershell
# 1. Check what's changed
git status

# 2. Stage your changes
git add .

# 3. Commit with a meaningful message
git commit -m "feat: add login form validation"

# 4. Push to GitHub
git push
```

## Commit Message Format (Always Use This)

```
feat: add new feature
fix: correct a bug
docs: update README
refactor: clean up code without changing behaviour
test: add tests
chore: update dependencies or config
```

Examples:
- `feat: add student grade calculator`
- `fix: correct average calculation for empty list`
- `docs: add setup instructions to README`
- `refactor: simplify file reading logic`

BAD commit messages (never do these):
- `update`
- `fix stuff`
- `asdfgh`
- `final`
- `final2`

## Branches (Use When Working on a New Feature)

```powershell
git branch                        # List all branches
git checkout -b feature-name      # Create + switch to new branch
git checkout main                 # Switch back to main branch
git merge feature-name            # Merge feature into main
```

## Checking History

```powershell
git log --oneline                 # Short list of all commits
git diff                          # See exact changes not yet staged
git diff --staged                 # See exact changes staged for commit
```

## Undoing Mistakes

```powershell
# Undo changes to a file (before staging)
git checkout -- filename.py

# Unstage a file (undo git add)
git reset HEAD filename.py

# Undo last commit (keep the changes in your files)
git reset --soft HEAD~1
```

## Connecting Local Repo to GitHub

```powershell
# Add GitHub as remote origin
git remote add origin https://github.com/YourUsername/repo-name.git

# First push (sets upstream tracking)
git push -u origin main

# All future pushes (just this)
git push
```

## Useful Shortcuts

```powershell
git add . && git commit -m "your message"   # Stage + commit in one line
git log --oneline --graph                   # Visual branch history
git remote -v                               # Show connected remote repos
```
