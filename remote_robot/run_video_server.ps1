$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

Write-Host "=== THRIVE Remote Video Server ===" -ForegroundColor Cyan

# --- 1. Check / install uv (manages Python + dependencies for us) ---
$uv = Get-Command uv -ErrorAction SilentlyContinue
if (-not $uv) {
    Write-Host "uv (Python package manager) was not found - installing it now..."
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    $uvDir = Join-Path $env:USERPROFILE ".local\bin"
    $env:Path = "$uvDir;$env:Path"
    $uv = Get-Command uv -ErrorAction SilentlyContinue
    if (-not $uv) {
        Write-Host ""
        Write-Host "ERROR: uv install did not complete." -ForegroundColor Red
        Write-Host "Install it manually from https://docs.astral.sh/uv/getting-started/installation/ then re-run this script."
        exit 1
    }
}
Write-Host "Found $(& uv --version)"

# --- 2. Check VLC media player ---
$vlcFound = (Test-Path "HKLM:\SOFTWARE\VideoLAN\VLC") -or (Test-Path "HKLM:\SOFTWARE\WOW6432Node\VideoLAN\VLC")
if (-not $vlcFound) {
    Write-Host ""
    Write-Host "ERROR: VLC media player was not found on this machine." -ForegroundColor Red
    Write-Host "video_server.py uses VLC as its video-playback engine (python-vlc is just bindings, not a full install)."
    Write-Host "Download the 64-bit installer from https://www.videolan.org/vlc/download-windows.html, install it, then re-run this script."
    exit 1
}
Write-Host "Found VLC media player."

# --- 3. Sync dependencies (uv downloads a matching Python + creates .venv + installs deps from uv.lock) ---
Write-Host "Syncing dependencies (this can take a minute the first time)..."
& uv sync
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "ERROR: 'uv sync' failed." -ForegroundColor Red
    Write-Host "If the error above mentions 'Microsoft Visual C++ 14.0 or greater is required' (from building simpleaudio),"
    Write-Host "install 'Build Tools for Visual Studio' (Desktop development with C++ workload) from:"
    Write-Host "https://visualstudio.microsoft.com/visual-cpp-build-tools/"
    Write-Host "then re-run this script."
    exit 1
}

# --- 4. Run the server ---
Write-Host ""
Write-Host "Starting video_server.py ... (press Ctrl+C to stop)" -ForegroundColor Green
& uv run python video_server.py
