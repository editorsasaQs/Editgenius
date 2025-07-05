from flask import Flask, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import os
from process import process_video
from whisper import transcribe_audio
from gemini import generate_scenes

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route('/api/upload', methods=['POST'])
def upload():
    files = request.files
    video = files.get('video')
    voiceover = files.get('voiceover')
    bgm = files.get('bgm')
    logo = files.get('logo')

    video_path = os.path.join(UPLOAD_FOLDER, secure_filename(video.filename))
    voiceover_path = os.path.join(UPLOAD_FOLDER, secure_filename(voiceover.filename))
    bgm_path = os.path.join(UPLOAD_FOLDER, secure_filename(bgm.filename))
    logo_path = os.path.join('assets/logo', secure_filename(logo.filename))

    video.save(video_path)
    voiceover.save(voiceover_path)
    bgm.save(bgm_path)
    logo.save(logo_path)

    transcript = transcribe_audio(voiceover_path)
    scenes = generate_scenes(transcript)

    output_path = process_video(video_path, voiceover_path, bgm_path, logo_path, scenes)

    return jsonify({"download_url": f"/download/{os.path.basename(output_path)}"})

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
