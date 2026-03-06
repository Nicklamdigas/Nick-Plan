# GitHub Copilot CLI Installation Guide for Ubuntu

## Complete Step-by-Step Guide with Troubleshooting

---

## PART 1: Complete Removal (Clean Slate)

If you have any broken installations, let's remove everything first:

```bash
# 1. Remove GitHub CLI (gh) if installed via apt
sudo apt remove gh -y
sudo apt autoremove -y

# 2. Remove GitHub CLI if installed via snap
sudo snap remove gh

# 3. Remove any manual installations
sudo rm -rf /usr/local/bin/gh
sudo rm -rf /usr/bin/gh

# 4. Remove GitHub CLI configuration
rm -rf ~/.config/gh

# 5. Remove GitHub Copilot CLI extension
gh extension remove github/gh-copilot 2>/dev/null || true

# 6. Clean up any leftover files
rm -rf ~/.local/share/gh

# Verify everything is removed
which gh
# Should output nothing or "gh not found"
```

---

## PART 2: Prerequisites

Before installing, make sure you have:

### 1. Check Ubuntu Version
```bash
lsb_release -a
```
**Requirement:** Ubuntu 18.04 or later (should work fine)

### 2. Check Internet Connection
```bash
ping -c 3 github.com
```
**Should see:** Packets sent and received successfully

### 3. Update System
```bash
sudo apt update
sudo apt upgrade -y
```

---

## PART 3: Install GitHub CLI (gh)

GitHub Copilot CLI is an extension of GitHub CLI, so we need `gh` first.

### Method 1: Official Repository (RECOMMENDED)

```bash
# 1. Add GitHub's official GPG key
sudo mkdir -p -m 755 /etc/apt/keyrings
wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null
sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg

# 2. Add GitHub CLI repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

# 3. Update package list
sudo apt update

# 4. Install GitHub CLI
sudo apt install gh -y

# 5. Verify installation
gh --version
```

**Expected output:** `gh version X.XX.X (YYYY-MM-DD)`

### Method 2: If Method 1 Fails (Alternative)

```bash
# Download latest release directly
cd /tmp
wget https://github.com/cli/cli/releases/latest/download/gh_$(uname -m).tar.gz -O gh.tar.gz

# Extract
tar -xzf gh.tar.gz

# Move to system path
sudo mv gh_*/bin/gh /usr/local/bin/

# Verify
gh --version
```

---

## PART 4: Authenticate GitHub CLI

```bash
# Start authentication
gh auth login

# You'll be prompted with questions:
# 1. "What account do you want to log into?" 
#    → Select: GitHub.com (use arrow keys, press Enter)

# 2. "What is your preferred protocol for Git operations?"
#    → Select: HTTPS (recommended) or SSH (if you have SSH keys set up)

# 3. "Authenticate Git with your GitHub credentials?"
#    → Select: Yes

# 4. "How would you like to authenticate GitHub CLI?"
#    → Select: "Login with a web browser" (easiest)

# 5. You'll see a code (e.g., ABCD-1234)
#    → Copy this code
#    → Press Enter (browser will open or you'll get a URL)
#    → Paste code in browser
#    → Authorize GitHub CLI

# Verify authentication
gh auth status
```

**Expected output:** `✓ Logged in to github.com as YOUR_USERNAME`

---

## PART 5: Install GitHub Copilot CLI Extension

```bash
# Install the Copilot extension
gh extension install github/gh-copilot

# Verify installation
gh extension list
```

**Expected output:** Should show `gh copilot` in the list

---

## PART 6: Configure GitHub Copilot CLI

```bash
# Check Copilot status
gh copilot status

# If you need to authenticate Copilot (you should have Copilot access)
gh copilot auth
```

**Note:** You need a GitHub Copilot subscription (Student/Individual/Business)

---

## PART 7: Test GitHub Copilot CLI

```bash
# Ask Copilot a question
gh copilot suggest "list all files in current directory"

# Explain a command
gh copilot explain "tar -xzf file.tar.gz"
```

**Expected:** Copilot should respond with suggestions/explanations

---

## PART 8: Set Up Aliases (Optional but Recommended)

Make it easier to use by adding shortcuts:

```bash
# Open your shell config file
nano ~/.bashrc
# OR if you use zsh:
# nano ~/.zshrc

# Add these lines at the end:
alias ghcs='gh copilot suggest'
alias ghce='gh copilot explain'

# Save and exit (Ctrl+X, then Y, then Enter)

# Reload shell config
source ~/.bashrc
# OR
# source ~/.zshrc

# Now you can use:
ghcs "how to find large files"
ghce "find . -name '*.py'"
```

---

## COMMON ISSUES & TROUBLESHOOTING

### Issue 1: "gh: command not found"
**Cause:** GitHub CLI not installed or not in PATH

**Solution:**
```bash
# Check if gh exists
which gh

# If not found, reinstall using Method 1 or 2 above

# Add to PATH manually if needed
echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc
source ~/.bashrc
```

### Issue 2: "HTTP 403: Forbidden" during installation
**Cause:** GitHub rate limiting or authentication issue

**Solution:**
```bash
# Re-authenticate
gh auth logout
gh auth login

# Try again
gh extension install github/gh-copilot
```

### Issue 3: "extension 'github/gh-copilot' not found"
**Cause:** Wrong extension name or repository issue

**Solution:**
```bash
# Remove if exists
gh extension remove copilot 2>/dev/null

# Install with full name
gh extension install github/gh-copilot

# Update gh itself
sudo apt update
sudo apt install gh -y
```

### Issue 4: "You don't have access to GitHub Copilot"
**Cause:** No Copilot subscription

**Solution:**
- Check: https://github.com/settings/copilot
- Students get it FREE: https://education.github.com/
- Or subscribe: https://github.com/features/copilot

### Issue 5: Extensions directory permission error
**Cause:** Permission issues with .local/share/gh

**Solution:**
```bash
# Fix permissions
mkdir -p ~/.local/share/gh
chmod -R 755 ~/.local/share/gh

# Try installing again
gh extension install github/gh-copilot
```

### Issue 6: "couldn't read from remote repository"
**Cause:** Network or Git configuration issue

**Solution:**
```bash
# Check Git config
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Test GitHub connection
ssh -T git@github.com
# OR for HTTPS:
gh auth status

# If SSH fails, use HTTPS authentication
```

### Issue 7: Old version of gh
**Cause:** Outdated GitHub CLI version

**Solution:**
```bash
# Check version
gh --version

# Update
sudo apt update
sudo apt upgrade gh -y

# Or reinstall
sudo apt remove gh -y
# Then follow PART 3 again
```

---

## VERIFICATION CHECKLIST

After installation, verify everything works:

```bash
# 1. Check gh version
gh --version
# ✓ Should show version 2.X.X or higher

# 2. Check authentication
gh auth status
# ✓ Should show "Logged in to github.com"

# 3. List extensions
gh extension list
# ✓ Should show "github/gh-copilot"

# 4. Check Copilot access
gh copilot status
# ✓ Should show "You have access to GitHub Copilot"

# 5. Test suggest command
gh copilot suggest "create a new directory"
# ✓ Should show command suggestions

# 6. Test explain command
gh copilot explain "ls -la"
# ✓ Should explain the command
```

---

## ALTERNATIVE: Install via npm (If all else fails)

If the above methods don't work, you can try the npm version:

```bash
# 1. Install Node.js and npm (if not installed)
sudo apt update
sudo apt install nodejs npm -y

# 2. Install GitHub Copilot CLI via npm
npm install -g @githubnext/github-copilot-cli

# 3. Authenticate
github-copilot-cli auth

# 4. Use with:
github-copilot-cli suggest "command"
```

---

## GETTING HELP

If you're still stuck after trying everything:

```bash
# Check GitHub CLI issues
gh issue list --repo cli/cli

# Check Copilot CLI issues
gh issue list --repo github/gh-copilot

# Get debug info
gh --version
gh auth status
gh extension list
```

**Save this output and share it with me when you come back!**

---

## QUICK REFERENCE CARD

After successful installation, here are the main commands:

```bash
# Suggest commands
gh copilot suggest "what you want to do"
ghcs "what you want to do"  # if alias set up

# Explain commands
gh copilot explain "command to explain"
ghce "command to explain"  # if alias set up

# Check status
gh copilot status

# Update extension
gh extension upgrade copilot

# Reinstall extension
gh extension remove copilot
gh extension install github/gh-copilot
```

---

## FOR YOUR SPECIFIC CASE

Based on common issues students face, try this sequence:

```bash
# Complete clean install sequence
sudo apt remove gh -y
sudo apt autoremove -y
rm -rf ~/.config/gh
sudo apt update
sudo apt upgrade -y

# Install fresh
sudo mkdir -p -m 755 /etc/apt/keyrings
wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null
sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh -y

# Authenticate
gh auth login
# Follow prompts, use web browser method

# Install Copilot
gh extension install github/gh-copilot

# Test
gh copilot suggest "list files"
```

---

## WHEN YOU COME BACK

After trying this in Ubuntu, come back and tell me:

1. What step did you get stuck on?
2. What error message did you see?
3. Output of these commands:
   ```bash
   gh --version
   gh auth status
   gh extension list
   ```

Good luck! You got this! 💪
