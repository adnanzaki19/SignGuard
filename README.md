# SignGuard: Gestrure Triggered Emergency Alert System
![DALL·E 2024-01-10 00 46 48 - Create a simplified logo for 'SignGuard'  The logo should focus on the text 'SignGuard' in a modern, clean font, suitable for a high-tech brand  Use a](https://github.com/adnanzaki19/SignGuard/assets/68474810/617be6c6-488a-4ed9-87f5-fa6d42e14425)

## Overview
SignGuardian is a desktop application that utilizes advanced computer vision and machine learning technologies to recognize American Sign Language (ASL) gestures, specifically targeting emergency distress signals. The application runs silently in the background and triggers alerts or contacts emergency services when a specific ASL gesture for help is detected.

## Features
- **Real-time Gesture Recognition**: Employs MediaPipe and OpenCV to accurately detect ASL help gestures.
- **Automated Alert System**: Configurable to notify emergency contacts or services upon detecting distress signals.
- **Background Operation**: Designed to run unobtrusively in the background, ensuring constant monitoring without disrupting user activities.
- **Scalable Architecture**: Future plans for integration with server systems to facilitate public safety monitoring using IP cameras.

## Technical Challenges
Packaging the application for various desktop environments posed significant challenges, particularly in embedding the necessary libraries for gesture recognition. Solutions explored included PyInstaller and cx_Freeze, highlighting the project's emphasis on robustness and compatibility.

## Installation and Usage
Currently simply run main.py and perform the following gesture at your webcam:
![Signal_for_Help_gestures](https://github.com/adnanzaki19/SignGuard/assets/68474810/ecf13726-b85d-4fb2-8502-95a4a2ccf574)
Consolidated desktop app coming soon!
