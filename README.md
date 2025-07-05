# 🎬 EditGenius AI

**EditGenius AI** is a smart, AI-powered video editing SaaS application. It lets users upload raw video, voiceovers, background music, logo, and transitions — then automatically edits and produces polished videos for YouTube or Reels.

> ✨ Built with Flask, FFmpeg, Gemini Pro, and Tailwind HTML frontend.

---

## 📦 Features

- ✂️ Smart scene detection (cutting blank or off-topic parts)
- 📜 Auto-subtitles with highlights and zoom
- 🔁 Transition effects between clips
- 🎵 Background music + voiceover mixing
- 🖼 Logo overlay on final output
- 🎯 Export in 16:9 (YouTube) or 9:16 (Instagram Reel) format

---

## 📁 Folder Structure

EditGenius/ ├── backend/                # Flask API and video processing logic │   ├── app.py │   ├── process.py │   ├── whisper.py │   ├── gemini.py │   └── requirements.txt ├── frontend/               # HTML upload form │   └── index.html ├── assets/ │   ├── transitions/        # Uploaded transition clips (t1.mp4, t2.mp4, etc.) │   └── logo/               # Uploaded logo image ├── uploads/                # Uploaded videos, audio, etc. ├── outputs/                # Final processed videos └── README.md