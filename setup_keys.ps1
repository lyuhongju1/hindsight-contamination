# One-time key setup for the hindsight study. Run in your OWN PowerShell window (not inside Claude Code):
#   powershell -ExecutionPolicy Bypass -File "C:\Users\lyuho\Downloads\hindsight contamination\setup_keys.ps1"
# Keys are typed hidden, stored as user environment variables, and never printed.

function Read-Secret($prompt) {
    $s = Read-Host -Prompt $prompt -AsSecureString
    $b = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($s)
    try { [Runtime.InteropServices.Marshal]::PtrToStringBSTR($b) } finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($b) }
}

$a = Read-Secret "Paste your Anthropic API key (hidden), then Enter"
if ($a) { [Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", $a, "User"); "Anthropic key stored." } else { "Anthropic key skipped." }

$o = Read-Secret "Paste your OpenRouter API key (hidden), or just press Enter to skip"
if ($o) { [Environment]::SetEnvironmentVariable("OPENROUTER_API_KEY", $o, "User"); "OpenRouter key stored." } else { "OpenRouter key skipped (second-vendor check not possible until added)." }
Remove-Variable a, o

"Starting GitHub login: copy the one-time code shown, then approve in the browser."
& "C:\Program Files\GitHub CLI\gh.exe" auth login --hostname github.com --web --git-protocol https

"Done. Restart Claude Code, then tell Claude: setup done."
