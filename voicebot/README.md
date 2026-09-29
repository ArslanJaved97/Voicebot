\# Offline Voice Bot



A fully offline voice assistant that runs locally on your Windows PC. No APIs, no cloud services, and no costs.



\## Prerequisites



Before you begin, you'll need to have a few tools installed:



1\.  \*\*Miniconda:\*\* For managing the Python environment. \[Download here](https://docs.conda.io/en/latest/miniconda.html).

2\.  \*\*Ollama:\*\* For running the AI language model locally. \[Download here](https://ollama.com/download).



\## Setup Instructions



1\.  \*\*Clone the repository:\*\*

&#x20;   ```bash

&#x20;   git clone https://github.com/YOUR\ArslanJaved97/voicebot.git

&#x20;   cd voicebot



Create and activate the conda environment:

conda create -n voicebot python=3.11 -y

conda activate voicebot





Install the required Python packages:



python -m pip install -r requirements.txt





Install FFmpeg (required for audio processing):



conda install -c conda-forge ffmpeg -y





Download the AI model for Ollama:

Open a new terminal and run:



ollama pull llama3.2



&#x20;   Make sure the Ollama application is running in your system tray.



How to Run



Once the setup is complete, run the bot from your project directory:

The bot will start listening for your voice. Speak your query, and it will respond. Say "goodbye" to exit.

Customization



You can customize the bot's knowledge and personality by editing the Script.txt file.

