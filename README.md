# 🧠 ContentOrganizer  
**AI-Powered, Privacy-First Image Organizer**

> **Bring visual clarity to your clutter. 100% local. Zero data leaves your machine.**

---

## 📂 What is ContentOrganizer?

**ContentOrganizer** is a smart, local-first assistant designed to help you manage and organize your image files effortlessly. Powered by cutting-edge AI models, ContentOrganizer scans your image folders, understands their content, and automatically organizes them into clean, descriptive folders — all while keeping your data secure and offline.

Whether you're dealing with a massive folder, unsorted photography archive, or years of content, ContentOrganizer brings intelligent structure to your visual files.

---

## 🧠 Key Features

- ✅ **Visual Understanding of Images**  
  Uses advanced AI to "look" at each image and generate relevant metadata, descriptions, and tags.

- 🗂️ **Automatic Folder Structuring**  
  Groups images into folders based on their content — people, objects, places, time, etc.

- 🖥️ **Preview Before You Organize**  
  Review suggested folders and file names in a user-friendly interface before confirming.

- 🛡️ **100% Local & Private**  
  All AI processing is done on your machine — **no cloud, no APIs, no internet needed**.

- 💻 **Cross-Platform**  
  Runs on **macOS**, **Linux**, and **Windows**.

---

## 🔍 Supported File Types

- `.png`  
- `.jpg` / `.jpeg`  
- `.gif`  
- `.bmp`

---

## 🚀 How It Works

1. **Choose a Folder**  
   Select the image directory you want to clean up.

2. **AI-Powered Analysis**  
   ContentOrganizer visually interpret each image and generate context-aware metadata.

3. **Folder & Filename Suggestions**  
   Based on image content, the app suggests an organized folder structure

4. **Review & Confirm**  
   Browse the preview and approve the changes you like.

5. **Organize!**  
   The app sorts the files into the newly structured folders.

---

## 🛠️ Installation

> _Coming soon_: 


This intelligent file organizer harnesses the power of advanced AI models, including language models (LMs) and vision-language models (VLMs), to automate the process of organizing files by:

Scanning a specified input directory for files.

Content Understanding:

Textual Analysis: Uses the Llama3.2 3B to analyze and summarize text-based content, generating relevant descriptions and filenames.
Visual Content Analysis: Uses the LLaVA-v1.6 , based on Vicuna-7B, to interpret visual files such as images, providing context-aware categorization and descriptions.
Understanding the content of your files (text, images, and more) to generate relevant descriptions, folder names, and filenames.

Organizing the files into a new directory structure based on the generated metadata.

The best part? All AI processing happens 100% on your local device using the Nexa SDK. No internet connection required, no data leaves your computer, and no AI API is needed - keeping your files completely private and secure.

1. Install Python
Before installing the Local File Organizer, make sure you have Python installed on your system. We recommend using Python 3.12 or later.

You can download Python from the official website.

Follow the installation instructions for your operating system.

2. Clone the Repository
Clone this repository to your local machine using Git:

git clone https://github.com/QiuYannnn/Local-File-Organizer.git
Or download the repository as a ZIP file and extract it to your desired location.

4. Install Nexa SDK ️
CPU Installation
To install the CPU version of Nexa SDK, run:

pip install nexaai --prefer-binary --index-url https://nexaai.github.io/nexa-sdk/whl/cpu --extra-index-url https://pypi.org/simple --no-cache-dir

Note: If you encounter issues with any packages, install them individually:

pip install nexa Pillow pytesseract PyMuPDF python-docx
With the environment activated and dependencies installed, run the script using:

6. Running the Script🎉
python main.py
Notes
SDK Models:

The script uses NexaVLMInference and NexaTextInference models usage.
Ensure you have access to these models and they are correctly set up.
You may need to download model files or configure paths.
Dependencies:

pytesseract: Requires Tesseract OCR installed on your system

Processing Time:

Processing may take time depending on the number and size of files.
The script uses multiprocessing to improve performance.
Customizing Prompts:

You can adjust prompts in data_processing.py to change how metadata is generated.

https://github.com/QiuYannnn/Local-File-Organizer/tree/main


 Using Llama3.2 3B and Llava v1.6 models with the Nexa SDK, it intuitively scans, restructures, and organizes files for quick, seamless access and easy retrieval.

 Nexa SDK is a comprehensive toolkit for supporting GGML and ONNX models. It supports text generation, image generation, vision-language models (VLM), Audio Language Model, auto-speech-recognition (ASR), and text-to-speech (TTS) capabilities.

 pip install nexaai
 pip install --user -U nltk
 pip install llamacpp
 

 https://nexa.ai/
 https://www.nltk.org/
 https://github.com/ggml-org/llama.cpp