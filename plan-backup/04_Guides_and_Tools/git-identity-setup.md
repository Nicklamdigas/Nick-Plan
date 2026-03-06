# One Step Left — Configure Git Identity

Before you can commit code to GitHub, run these two commands in your terminal.
Use the SAME email you signed up to GitHub with.

```powershell
git config --global user.name "Nicholas Lamdi"
git config --global user.email "your-github-email@example.com"
```

Replace "Nicholas Lamdi" with your actual full name (or preferred name for GitHub).
Replace the email with your actual GitHub email.

## Verify it worked
```powershell
git config --global user.name
git config --global user.email
```

Both should print your details back to you.

## Why this matters
Every commit you push to GitHub will be signed with this name and email.
This is how your GitHub contribution graph gets built — every green square is a commit.
