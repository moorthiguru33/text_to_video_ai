import cv2
import numpy as np
from PIL import Image
from gtts import gTTS
from moviepy.editor import *

def create_video(frames, audio_text):
    height, width = 1080, 1920
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter('output_video.mp4', fourcc, 24.0, (width, height))

    tenali_img = Image.open('assets/tenali_raman.png').convert("RGBA")
    king_img = Image.open('assets/king.png').convert("RGBA")

    for frame in frames:
        img = Image.new('RGB', (width, height), color=(0, 0, 0))
        tenali_resized = tenali_img.resize((300, 300))
        king_resized = king_img.resize((300, 300))

        img.paste(tenali_resized, (100, 100), tenali_resized)
        img.paste(king_resized, (1500, 100), king_resized)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 40)
        y_text = 450
        for line in frame.split('\n'):
            draw.text((50, y_text), line, font=font, fill=(255, 255, 255))
            y_text += 50

        frame_np = np.array(img)
        video.write(cv2.cvtColor(frame_np, cv2.COLOR_RGB2BGR))

    video.release()
    print("Video saved as output_video.mp4")

    # Generate audio
    tts = gTTS(audio_text, lang='en')
    tts.save("output_audio.mp3")

    # Combine video and audio
    video_clip = VideoFileClip("output_video.mp4")
    audio_clip = AudioFileClip("output_audio.mp3")
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile("final_output_video.mp4", codec='libx264', audio_codec='aac')
    print("Final video saved as final_output_video.mp4")