from text_processing.nlp_model import process_text
from text_processing.text_to_storyboard import create_storyboard
from storyboarding.create_storyboard import visualize_storyboard
from video_generation.generate_frames import generate_frames
from video_generation.create_video import create_video

def main():
    text = "Your story text here..."
    sentences = process_text(text)
    storyboard = create_storyboard(sentences)
    visualize_storyboard(storyboard)
    frames = generate_frames(storyboard)
    create_video(frames)

if __name__ == "__main__":
    main()