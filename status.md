# 🛰️ THRIVE System Dashboard

This document tracks the current configuration and deployment status of all THRIVE hardware units.

***

## 🤖 THRIVE with Robot System
Each system is uniquely paired with a Computer ID, Camera ID, Robot ID, and Router ID.

| System ID  | Computer ID | Camera ID | Robot ID | Router ID | Network & IP                    | Status                                                                                  |
| :--------- | :---------: | :-------: | :------: | :-------: | :------------------------------ | :-------------------------------------------------------------------------------------- |
| **SYS-R1** |     #9    |    #7   |    #1    |     #1    | Linksys-01428 (`192.168.1.200`) | ![GSU](https://img.shields.io/badge/Location-GSU-blue?style=for-the-badge)         |
| **SYS-R2** |      #3     |     #3    |    #2    |     #2    | Linksys-00605 (`192.168.1.100`) | ![GSU](https://img.shields.io/badge/Location-GSU-blue?style=for-the-badge)         |
| **SYS-R3** |      #5     |     #4    |    #3    |     #3    | TPLink-1AC6 (`192.168.0.101`)   | ![GSU](https://img.shields.io/badge/Location-GSU-blue?style=for-the-badge)              |
| **SYS-R4** |     `??`    |    `??`   |    #4    |     #4    | TPLink-2053 (`192.168.0.104`)   | ![Ready](https://img.shields.io/badge/Status-Ready-success?style=for-the-badge) |
| **SYS-R5** |     #11    |    #8   |    #5    |     #5    | TPLink-1F6C (`192.168.0.105`) | ![GSU](https://img.shields.io/badge/Location-GSU-blue?style=for-the-badge)          |
| **SYS-R6** |     `??`    |    `??`   |    #6    |     #6    | TPLink-2110 (`192.168.0.106`) | ![Ready](https://img.shields.io/badge/Status-Ready-success?style=for-the-badge)         |
| **SYS-R7** |     #6    |    #9   |    #7    |     #7    | TPLink-20E9 (`192.168.0.107`) | ![GSU](https://img.shields.io/badge/Location-GSU-blue?style=for-the-badge)         |


***

## 📷 Camera Only System

| System ID  | Computer ID | Camera Type  | Notes                    | Status                                                                       |
| :--------- | :---------: | :----------- | :----------------------- | :----------------------------------------------------------------------- |
| **SYS-C1** |      #1     | Azure Kinect | Earlier version          | ![Active](https://img.shields.io/badge/Status-Active-blue?style=flat-square) |
| **SYS-C3** |      #4     |              | Used for legacy SuperPop | ![Active](https://img.shields.io/badge/Status-Active-blue?style=flat-square) |
| **SYS-C4** |      #7     | Legacy Kinect| Used for legacy SuperPop | ![Active](https://img.shields.io/badge/Status-Active-blue?style=flat-square) |
| **SYS-C5** |      #10    | Femto Bolt #6|        8/11/26           | ![Active](https://img.shields.io/badge/Status-Active-blue?style=flat-square) |

***

> \[!TIP]
> **Maintenance Note:** When deploying a system to a new site, please update the **System ID** status and the corresponding **Network & IP** column to ensure remote SSH/VNC access remains valid.
