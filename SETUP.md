# One-time setup (PI only, about 30 minutes)

Do these steps in a **separate PowerShell window**, not inside Claude Code. That way no key ever appears in the chat transcript. When you have finished, restart Claude Code and tell Claude "setup done". Claude then runs `python -I setup_check.py`, which checks that everything is in place without printing any secret.

---

## 1. Anthropic API key

1. **Optional:** revoke the APS-era key and create a new one. The old key was once stored in a plain-text scratchpad file (since deleted), so revoking it is a precaution. The PI decided to keep the existing key, which already has a spend limit.
2. Store the key as a user environment variable:

```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "PASTE-KEY-HERE", "User")
```

## 2. Second vendor: gateway key (strongly recommended)

1. Create an OpenRouter account (or another multi-vendor gateway), add credit, and set a spend limit. Suggested: $1,000.
2. Store the key:

```powershell
[Environment]::SetEnvironmentVariable("OPENROUTER_API_KEY", "PASTE-KEY-HERE", "User")
```

Without this key, the design falls back to a test of one model family only (design v3 §4).

## 3. Git identity and GitHub CLI

```powershell
git config --global user.name "Hong Joo Ryoo"
git config --global user.email "lyuhongju1@gmail.com"
winget install --id GitHub.cli
```

Close and reopen PowerShell, then run:

```powershell
gh auth login
```

Choose GitHub.com → HTTPS → log in with a browser.

## 4. Repository

After `gh auth login`, tell Claude to create the public repository `lyuhongju1/hindsight-contamination`. Claude then sets up the skeleton and makes the first freeze commit.

To let Claude push freezes without asking each time, approve the allow rules Claude proposes for this folder's `.claude/settings.local.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(git push origin main)",
      "PowerShell(git push origin main)"
    ]
  }
}
```

These rules match only the exact command `git push origin main`, run from this project folder. Force-pushes and pushes to other branches or remotes still ask you. Note that the rule matches the command text, not the repository, so it relies on `origin` in this folder being the study repository.

## 5. Zenodo (can wait until the first deposit)

On zenodo.org, open Account → Applications → Personal access token, with scopes `deposit:write` and `deposit:actions`. Then:

```powershell
[Environment]::SetEnvironmentVariable("ZENODO_TOKEN", "PASTE-TOKEN-HERE", "User")
```

## 6. Two decisions (reply in chat)

- **GPU for the causal arm:** yes (which provider or allocation) / no.
- **Target journal:** check its policy on AI-conducted research before Claude drafts Stage 1.
