# ElevenLabs Multi-Language Voice Localization Demo

This repository demonstrates a lightweight automated localization workflow built using the **ElevenLabs Text-to-Speech API**. It simulates how entertainment and gaming studios can rapidly convert dialogue scripts into localized voice tracks for pre-visualization, dubbing, and scratch audio pipelines.

## Features
- **Multi-Language Generation:** Automates audio generation across English and Spanish.
- **Voice Profile Selection:** Uses high-fidelity ElevenLabs voice models (`eleven_multilingual_v2`).
- **Pipeline Integration:** Designed to integrate with localized game scripts or media dubbing pipelines.

## Setup & Prerequisites
1. Python installed on your PC.
2. An active ElevenLabs API Key.

### Installation
Open your Windows Command Prompt and run:
```cmd
pip install elevenlabs
Usage
Set your API key as an environment variable in your Command Prompt and run the generator:

set ELEVENLABS_API_KEY="your_actual_api_key_here"
python main.py
Business Impact & Use Cases
Media Dubbing & Localization: Drastically reduces turnaround time for localized audio testing across 70+ languages.

AAA Gaming Pre-Production: Allows narrative directors and sound designers to evaluate localized dialogue timing before full studio recording sessions.

Human-in-the-Loop Workflows: Enables hybrid production teams (like ElevenProductions) to blend AI speed with professional audio mastering.
