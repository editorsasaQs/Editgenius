from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, AudioFileClip, TextClip
import os

def process_video(video_path, voice_path, bgm_path, logo_path, scenes):
    base = os.path.splitext(os.path.basename(video_path))[0]
    output_path = f"outputs/{base}_final.mp4"

    clips = []
    original = VideoFileClip(video_path)
    logo = (VideoFileClip(logo_path).resize(height=50).set_duration(1))

    for scene in scenes:
        start = convert_to_seconds(scene["start"])
        end = convert_to_seconds(scene["end"])
        clip = original.subclip(start, end)

        if scene.get("zoom"):
            clip = clip.resize(1.1)
        if scene.get("highlight"):
            subtitle = TextClip(scene["subtitle"], fontsize=50, color='white').set_duration(clip.duration)
            clip = CompositeVideoClip([clip, subtitle.set_pos('bottom')])

        clip = CompositeVideoClip([clip, logo.set_pos(("left", "top"))])
        clips.append(clip)

    final = concatenate_videoclips(clips)
    audio = AudioFileClip(voice_path).fx(AudioFileClip.set_duration, final.duration)
    bgm = AudioFileClip(bgm_path).volumex(0.3).fx(AudioFileClip.set_duration, final.duration)
    final = final.set_audio(audio.set_duration(final.duration).audio_fadein(1).audio_fadeout(1).volumex(1).overlay(bgm))

    final.write_videofile(output_path, codec="libx264")
    return output_path

def convert_to_seconds(time_str):
    h, m, s = map(float, time_str.split(':'))
    return h*3600 + m*60 + s
