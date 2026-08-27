# THRIVE System

**THRIVE: Therapeutic Humanoid Robot In Virtual Environment** — [arxiv.org/abs/2608.14462](https://arxiv.org/abs/2608.14462)

> This paper presents THRIVE (Therapeutic Humanoid Robot In Virtual Environment), an at-home rehabilitation platform that integrates a suite of virtual-reality upper-body rehabilitation games, a real-time camera-based motion-tracking system, and a socially interactive robot therapist. The system is designed for therapy and intervention in children with upper-limb motor impairments, which can be improved through consistent, task-specific practice. THRIVE features a set of newly designed, engaging games that target functional reaching, grasping, and object-manipulation movements through customizable popping, hitting, catching, and grabbing tasks, while the camera-based tracking system captures the child's kinematic performance during play. A robot therapist - deployable either as a physical robotic coach or as a remote-presence virtual agent - delivers adaptive, dynamic feedback to motivate the child and guide their movements toward therapeutic goals. THRIVE decouples the therapeutic games from the robot embodiment, extending the platform to support various embodiments and different robots within one modular system. This robot-agnostic design makes THRIVE affordable, scalable, and readily adaptable for sustained use in the home, offering a practical pathway to more consistent and engaging upper-limb therapy for children with motor function impairments.

![THRIVE system diagram: RGB-D camera skeleton tracking feeding a rehabilitation game, with a robot therapist giving real-time feedback](img/diagram.png)

## The Robot

<img src="img/physical_thrive.jpg" alt="The THRIVE robot" width="400">

## Documentation

| Page | What it covers |
|---|---|
| [operation.md](operation.md) | Running a THRIVE session with a physical robot or a remote-presence robot: setup, playing the game, and troubleshooting. |
| [robot-setup.md](robot-setup.md) | Setting up the Raspberry Pi that drives the physical robot — static IP, Python environment, and the auto-start service. |
| [unity-dev-setup.md](unity-dev-setup.md) | Getting the Unity project running, and connecting it to either a physical robot or a remote-presence robot. |
| [status.md](status.md) | Inventory of all deployed THRIVE systems and their current status. |
