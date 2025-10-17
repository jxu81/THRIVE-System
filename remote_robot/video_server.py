from flask import Flask, render_template
from flask_socketio import SocketIO
import vlc, threading, time, random, os, simpleaudio as sa, socket
from pathlib import Path

# ============================================================
# Paths
# ============================================================
VIDEO_BASE = Path(r"C:\Jin\THRIVE-System\remote_robot\videos")
AUDIO_BASE = Path(r"C:\Jin\THRIVE-System\audio_files")

VIDEOS = {
    "0": str(VIDEO_BASE / "Hello.mp4"),
    "1": str(VIDEO_BASE / "Say.mp4"),
    "2": str(VIDEO_BASE / "Say.mp4"),
    "3": str(VIDEO_BASE / "Celebrate.mp4"),
}

AUDIO_DIRS = {
    "0": AUDIO_BASE / "intro",
    "1": AUDIO_BASE / "faster",
    "2": AUDIO_BASE / "same",
    "3": AUDIO_BASE / "end"
}

STANDBY = "0"

# ============================================================
# Flask + SocketIO setup
# ============================================================
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# ============================================================
# VLC setup (video muted)
# ============================================================
instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new(VIDEOS[STANDBY])
player.set_media(media)
player.audio_set_mute(True)
player.play()
current = STANDBY

# ============================================================
# Play random .wav using simpleaudio
# ============================================================
def play_random_audio(folder_path):
    """Play a random WAV file asynchronously (reliable on Windows)."""
    try:
        files = [f for f in os.listdir(folder_path) if f.lower().endswith(".wav")]
        if not files:
            print(f"No audio files in {folder_path}")
            return
        filename = random.choice(files)
        path = os.path.join(folder_path, filename)
        print(f"Playing external audio: {path}")
        wave_obj = sa.WaveObject.from_wave_file(path)
        play_obj = wave_obj.play()  # non-blocking
    except Exception as e:
        print(f"Audio playback error: {e}")

# ============================================================
# Background loop for Standby
# ============================================================
def loop_standby():
    global player, current
    while True:
        time.sleep(1)
        if current == STANDBY and player.get_state() in (
            vlc.State.Ended, vlc.State.Stopped, vlc.State.Error):
            print("Restarting Standby loop...")
            media = instance.media_new(VIDEOS[STANDBY])
            player.set_media(media)
            player.audio_set_mute(True)
            player.play()

threading.Thread(target=loop_standby, daemon=True).start()

# ============================================================
# Command handler (shared by WebSocket + Unity TCP)
# ============================================================
def handle_command(cmd):
    global player, current
    cmd = str(cmd).strip()
    print("Received command:", cmd)

    if cmd not in VIDEOS:
        print(f"Invalid command: {cmd}")
        return

    # --- play corresponding audio ---
    audio_folder = AUDIO_DIRS.get(cmd)
    if audio_folder:
        threading.Thread(target=play_random_audio, args=(audio_folder,), daemon=True).start()

    # --- play silent video ---
    current = cmd
    media = instance.media_new(VIDEOS[cmd])
    player.set_media(media)
    player.audio_set_mute(True)
    player.play()
    print(f"Playing silent video: {VIDEOS[cmd]}")

    # --- return to standby when finished ---
    def restore():
        global current
        while player.get_state() != vlc.State.Ended:
            time.sleep(0.5)
        media = instance.media_new(VIDEOS[STANDBY])
        player.set_media(media)
        player.audio_set_mute(True)
        player.play()
        current = STANDBY

    threading.Thread(target=restore, daemon=True).start()

# ============================================================
# WebSocket route
# ============================================================
@socketio.on("command")
def handle_socketio_command(cmd):
    socketio.start_background_task(handle_command, cmd)

# ============================================================
# Flask web route
# ============================================================
@app.route("/")
def index():
    return render_template("index.html")

# ============================================================
# TCP server for Unity client
# ============================================================
TCP_HOST = "0.0.0.0"
TCP_PORT = 23456
BUFFER_SIZE = 1024

def tcp_server():
    """Simple TCP server that accepts commands from Unity."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((TCP_HOST, TCP_PORT))
    s.listen(1)
    print(f"🎮 TCP server listening for Unity on {TCP_HOST}:{TCP_PORT}")

    while True:
        conn, addr = s.accept()
        print(f"Unity connected from {addr}")
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

def handle_client(conn, addr):
    """Handle one Unity client."""
    try:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                print(f"Unity {addr} disconnected")
                break
            cmd = data.decode("utf-8").strip()
            print(f"Received from Unity: {cmd}")
            socketio.start_background_task(handle_command, cmd)
    except Exception as e:
        print(f"Unity client error {addr}: {e}")
    finally:
        conn.close()

# start the TCP server in background
threading.Thread(target=tcp_server, daemon=True).start()

# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("Starting WebSocket + Unity TCP video controller...")
    socketio.run(app, host="0.0.0.0", port=12345)
