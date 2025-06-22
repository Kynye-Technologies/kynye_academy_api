#!/bin/bash

echo ">>> Logging out of GitHub in VS Code..."

# Remove GitHub authentication token cache
rm -rf ~/.config/Code/User/globalStorage/github.vscode-auth
rm -rf ~/.config/Code/User/globalStorage/github.copilot
rm -rf ~/.config/Code/User/workspaceStorage/*github*

echo ">>> VS Code GitHub credentials cleared."

# Remove cached GitHub CLI credentials (optional)
if command -v gh &>/dev/null; then
    echo ">>> Clearing GitHub CLI auth (gh)..."
    gh auth logout
fi

echo ">>> Done. Now restart VS Code and sign in with your new GitHub account."
