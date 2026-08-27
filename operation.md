# Running a THRIVE Session

THRIVE can be run two ways: with a **physical robot**, or with a **remote-presence robot** (a video/audio stand-in with no hardware). Pick the section below for the one you're using.

## 1. Run THRIVE with a Physical Robot

### System components

A physical-robot system is made up of four pieces: a **computer**, an **FB (Femto Bolt) camera**, a **robot**, and a **router**. Each piece has an ID, and the IDs of all four **must match** (i.e. belong to the same numbered system) for everything to work together. Check [status.md](status.md) for the full inventory of which computer/camera/robot/router IDs are paired into each system.

### Setup

1. Turn on the wireless router. Make sure it's powered on and its network can be found before continuing.
2. Turn on the robot and the computer.
3. The computer should automatically connect to the system's designated wifi network. If it doesn't, connect manually — the wifi password is written on the back of the wireless router.
4. Connect the FB camera to the computer over USB. It's recommended to use the camera's additional power adapter rather than relying on USB bus power alone.
5. When the robot is connected to the network and powered on properly, it will say **"Hello World,"** its eyes will turn green, and it will flex both arms 💪.
6. Once you hear the robot say **"Hello World,"** you're ready to start the game.

### Running the Game

![Menu Illustration](menu.PNG)

7. Open the Kinect Game (`KinectGame.exe`). Click **Intro**; the robot should do the self-introduction.
8. Click on **Start** to play a game without the robot.
9. At the end of the game, please write down the **Average Movement Time** and **Target Movement Time**.
10. Click **Next**, and enter the Target Movement Time in the box labeled **Target MT**.
11. Click **Start Robot** to begin the interaction.

### Troubleshooting

1. **No camera feed:**
   - Check that the camera is on — its front LED should be a stable white when powered.
   - If it's on but there's still no feed, check the USB connection: unplug and replug it.
   - If that still doesn't work, try opening `Desktop\OrbbecViewer_v1.8.1_202310162037_win_x64_release\OrbbecViewer.exe` to see if you can get a camera feed there.
   - Also try `Desktop\Orbbec_SDK_K4A_Wrapper_v1.8.3_windows_64_release\Orbbec_SDK_K4A_Wrapper_v1.8.3_windows_64_release\bin\k4aviewer.exe` — you should get a camera feed there as well.
   - For more on the camera itself, see the [Orbbec Femto Bolt manual](https://www.orbbec.com/products/tof-camera/femto-bolt/).
2. **Have camera feed but no tracking** — reposition the camera / check for obstructions and lighting. Try opening the viewer paths listed above to make sure you're actually getting a camera feed.
3. **Robot repeatedly saying "Hello World"** — this usually means the robot isn't connected to the wifi network and/or the computer. Make sure the wifi network is on, and that you're using the matched router and computer for this system (see System components above).
4. **Robot not responding at all** — make sure the computer is on the wifi network. Use VNC Viewer to remotely log into the Raspberry Pi and check its status (both username and password are `admin`).

For setting up the robot itself (network, systemd service), see [robot-setup.md](robot-setup.md).

## 2. Run THRIVE with a Remote-Presence Robot

1. On the PC that will display the remote-presence robot, open **Git Bash** (or another command-line interface).
2. `cd` into the `remote_robot` folder.
3. Activate the virtual environment:
   ```
   source .venv/Scripts/activate
   ```
4. Start the video server:
   ```
   python video_server.py
   ```
   Wait until it's ready (you'll see a Standby video playing).
5. Run **`KinectGame.exe`** — same as with the physical robot.

For the full setup (installing dependencies, connecting Unity, deploying to a new laptop) and troubleshooting, see [unity-dev-setup.md](unity-dev-setup.md).
