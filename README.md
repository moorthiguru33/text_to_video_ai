# Text-to-Video AI

This project demonstrates how to create a text-to-video AI using open-source tools.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/moorthiguru33/text_to_video_ai.git
   ```

2. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Download the `en_core_web_sm` model for `spacy`:

   ```sh
   python -m spacy download en_core_web_sm
   ```

## Usage

1. Run the `main.py` script to start the text-to-video generation process:

   ```sh
   python main.py
   ```

2. The generated video will be saved as `output_video.mp4` in the project's root directory.

## Project Structure

```plaintext
text_to_video_ai/
├── text_processing/
│   ├── nlp_model.py
│   └── text_to_storyboard.py
├── storyboarding/
│   ├── create_storyboard.py
│   └── visualize_storyboard.py
├── video_generation/
│   ├── generate_frames.py
│   └── create_video.py
├── main.py
└── README.md
```