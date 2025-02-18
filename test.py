from moviepy.editor import TextClip

clip = TextClip("Hello, World!", fontsize=70, color='white', bg_color='black', size=(1920, 1080))
clip.write_videofile("test.mp4", fps=24)