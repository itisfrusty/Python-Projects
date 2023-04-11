import moviepy.editor
from pathlib import Path

print("Input video file: ")
video_filename = Path(f'{input()}')
video = moviepy.editor.VideoFileClip(f'{video_filename}')
audio = video.audio
audio.write_audiofile(f'{video_filename.stem}.mp3')

