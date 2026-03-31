# 🛰️ THRIVE System Dashboard

This document tracks the current configuration and deployment status of all THRIVE hardware units.

***

## 🤖 THRIVE with Robot System

These units are fully integrated with robotic arms and dedicated network routing.

| System ID  | Computer ID | Camera ID | Robot ID | Router ID | Network & IP                    | Status                                                                                  |
| :--------- | :---------: | :-------: | :------: | :-------: | :------------------------------ | :-------------------------------------------------------------------------------------- |
| **SYS-R1** |     `??`    |    `??`   |    #1    |     #1    | Linksys-01428 (`192.168.1.200`) | ![Ready](https://img.shields.io/badge/Status-Ready-success?style=for-the-badge)         |
| **SYS-R2** |      #3     |     #3    |    #2    |     #2    | Linksys-00605 (`192.168.1.100`) | ![Ready](https://img.shields.io/badge/Status-Ready-success?style=for-the-badge)         |
| **SYS-R3** |      #5     |     #4    |    #3    |     #3    | TPLink-1AC6 (`192.168.0.101`)   | ![GSU](https://img.shields.io/badge/Location-GSU-blue?style=for-the-badge)              |
| **SYS-R4** |     `??`    |    `??`   |    #4    |     #4    | TPLink-2053 (`192.168.0.102`)   | ![Setup](https://img.shields.io/badge/Status-In_Progress-lightgrey?style=for-the-badge) |

***

## 📷 Camera Only System

These units are designated for vision-specific tasks and do not include robotic hardware.

| System ID  | Computer ID | Camera Type  | Notes                    | Status                                                                       |
| :--------- | :---------: | :----------- | :----------------------- | :--------------------------------------------------------------------------- |
| **SYS-C1** |      #1     | Azure Kinect | Earlier version          | ![Active](https://img.shields.io/badge/Status-Active-blue?style=flat-square) |
| **SYS-C2** |      #2     | Azure Kinect | Earlier version          | ![Active](https://img.shields.io/badge/Status-Active-blue?style=flat-square) |
| **SYS-C3** |      #4     |              | Used for legacy SuperPop | ![Active](https://img.shields.io/badge/Status-Active-blue?style=flat-square) |
| **SYS-C4** |      #7     | Legacy Kinect| Used for legacy SuperPop | ![Active](https://img.shields.io/badge/Status-Active-blue?style=flat-square) |

***

> \[!TIP]
> **Maintenance Note:** When deploying a system to a new site, please update the **System ID** status and the corresponding **Network & IP** column to ensure remote SSH/VNC access remains valid.
