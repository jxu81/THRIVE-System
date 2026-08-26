$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

Write-Host "=== THRIVE Remote Video Server ===" -ForegroundColor Cyan

# --- 1. Check Python ---
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host ""
    Write-Host "ERROR: Python was not found on this machine." -ForegroundColor Red
    Write-Host "Install Python 3.10 or newer from https://www.python.org/downloads/"
    Write-Host "During install, check the box 'Add python.exe to PATH', then re-run this script."
    exit 1
}
$pyVersionOutput = & python --version 2>&1
Write-Host "Found $pyVersionOutput"

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

# --- 3. Create / reuse a virtual environment next to this script ---
$venvDir = Join-Path $ScriptDir ".venv"
$venvPython = Join-Path $venvDir "Scripts\python.exe"
if (-not (Test-Path $venvPython)) {
    Write-Host "Creating virtual environment in $venvDir ..."
    & python -m venv $venvDir
}

# --- 4. Install dependencies ---
Write-Host "Installing dependencies (this can take a minute the first time)..."
& $venvPython -m pip install --upgrade pip --quiet
& $venvPython -m pip install -r (Join-Path $ScriptDir "requirements.txt")
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "ERROR: Dependency install failed." -ForegroundColor Red
    Write-Host "If the error above mentions 'Microsoft Visual C++ 14.0 or greater is required' (from simpleaudio),"
    Write-Host "install 'Build Tools for Visual Studio' (Desktop development with C++ workload) from:"
    Write-Host "https://visualstudio.microsoft.com/visual-cpp-build-tools/"
    Write-Host "then re-run this script."
    exit 1
}

# --- 5. Run the server ---
Write-Host ""
Write-Host "Starting video_server.py ... (press Ctrl+C to stop)" -ForegroundColor Green
& $venvPython (Join-Path $ScriptDir "video_server.py")
