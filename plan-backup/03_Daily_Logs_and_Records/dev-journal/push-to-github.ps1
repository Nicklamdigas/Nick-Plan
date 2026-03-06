# Run this script after creating the dev-journal repo on GitHub
# Replace YOUR_GITHUB_USERNAME with your actual GitHub username

$githubUsername = "YOUR_GITHUB_USERNAME"  # <-- change this

Set-Location "C:\Nick\projects\dev-journal"

# Connect local repo to GitHub
git remote add origin "https://github.com/$githubUsername/dev-journal.git"

# Push to GitHub
git push -u origin main

Write-Host ""
Write-Host "Done! Your dev journal is now live on GitHub."
Write-Host "Visit: https://github.com/$githubUsername/dev-journal"
