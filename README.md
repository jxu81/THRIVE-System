# THRIVE System
 

# Instructions to Run THRIVE System

## Setup

1. Connect the wireless router to a power outlet. The white LED indicator should light up in solid white color.
2. Connect the Kinect's USB port to the PC and connect the Kinect's power cable to a power source.
3. Open the computer and ensure you are connected to the network **Linksys00605**.
4. Connect the robot power by switching the power button to the **ON** position.
5. Wait until the robot boots up. When you hear **"Hello World,"** proceed to the next step.

## Running the Game and Robot

![Menu Illustration](menu.PNG)

6. Open the Kinect Game. Click on **Test**; the robot will enter **Self-introduction** mode.
7. Click on **Start** to play a game without the robot.
8. At the end of the game, please write down the **Average Movement Time** and **Target Movement Time**.
9. Click **Next**, and enter the Target Movement Time in the box labeled **Target MT**.
10. Click **Start Robot** to begin the interaction.


### setup new robot
sudo nano /etc/systemd/system/robot2.service
sudo systemctl start robot2.service
sudo systemctl status robot2.service