# 🧠 ContentOrganizer  
**AI-Powered, Privacy-First Image Organizer**

> **Brings clarity to your clutter. 100% local. 100% private. Zero data leaves your machine.**

---

## 📂 What is ContentOrganizer?

**ContentOrganizer** is a smart, local-first assistant designed to help you manage and organize your image files effortlessly. Powered by  AI models, ContentOrganizer scans your image folders, understands their content, and automatically organizes them into clean, descriptive folders — all while keeping your data secure and offline.

Whether you're dealing with a massive folder, unsorted photography archive, or years of content, ContentOrganizer brings intelligent structure to your files.

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
   Browse the preview and approve the changes if you like.

5. **Organize!**  
   The app sorts the files into the newly structured folders.

---

## 🛠️ Installation

Prerequisites
- Python 3.12 or later

Steps to Install
1. **Clone the Repository**
```bash
git clone https://github.com/jharri34/ContentOrganizer
source venv/bin/activate
```

> desktop application coming soon


2. Install the Nexa SDK
To install the CPU version of the Nexa SDK, run:
```bash
pip install nexaai
```
> Note: If you encounter issues with any packages, install them individually:


3. Install Additional Dependencies
Run the following commands to install required libraries:
```bash
 pip install nltk
 pip install llama-cpp-python 
```
4. Running the Script
Activate your Python environment.

Run the script:
```bash
python src/contentorganizer/main.py    
```

## Useful links

* https://nexa.ai/
* https://www.nltk.org/
* https://github.com/ggml-org/llama.cpp
* https://github.com/QiuYannnn/Local-File-Organizer.git


## Dependencies:
* onnx
* llama-cpp-python
* nltk
* pytesseract: Requires Tesseract OCR installed on your system
* AI Models: Llama 3.2 3B, Llava v1.6
* SDK: Nexa SDK for local AI processing
* Languages: Python
* Libraries: Pillow, pytesseract, PyMuPDF, python-docx, nltk, llama-cpp-python

### Notes:

* Processing may take time depending:
 on the number and size of files.

* Multiprocessing to improve performance. COMING SOON

* Customizing Prompts:
You can adjust prompts in data_processing.py to change how metadata is generated.
