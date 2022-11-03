# Import everything needed to edit video clips
from moviepy.editor import *

# Load myHolidays.mp4 and select the subclip 00:00:00 - 00:00:05
video_clip = VideoFileClip("Future_Generali_Editable_Video.mp4").subclip(0, 5)

# Reduce the audio volume (volume x 0.8)
# video_clip = clip.volumex(0.8)

# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip("Keval - +919892580676", fontsize=70, color='black')

# Say that you want it to appear 5s at the center of the screen
txt_clip = txt_clip.set_pos('center').set_duration(5)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([video_clip, txt_clip])

# Write the result to a file (many options available !)
video.write_videofile('text_add_result.mov', fps=24, codec='libx264')
