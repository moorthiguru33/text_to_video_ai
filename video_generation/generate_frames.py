import random

def generate_frames(storyboard):
    frames = []
    for scene in storyboard:
        frame = f"Frame for: {scene['text']}"
        frames.append(frame)
    return frames