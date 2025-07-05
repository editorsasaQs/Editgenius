import requests

API_KEY = "AIzaSyBOoGu3bZcOmlSVRCvETvRdf7kOGj3hd40"

def generate_scenes(transcript):
    prompt = f"""From this transcript, break into 5–8 scenes. Return in JSON:
[
  {{
    "start": "00:00:04",
    "end": "00:00:12",
    "subtitle": "Why Your Ads Don't Work",
    "highlight": true,
    "zoom": false,
    "transition_id": "t1.mp4"
  }}
] 
Transcript: {transcript}
"""
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY
    res = requests.post(url, json={"contents":[{"parts":[{"text": prompt}]}]})
    scenes = res.json()["candidates"][0]["content"]["parts"][0]["text"]
    return eval(scenes)  # CAUTION: Only safe here because we control the prompt
