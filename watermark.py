from moviepy.editor import *

video_clip = VideoFileClip("Future_Generali_Editable_Video.mp4").subclip(0, 5)

txt_clip = TextClip("Vanshul", fontsize=30, color="black").set_duration(5)

txt_clip = txt_clip.set_position("bottom","right")

video = CompositeVideoClip([video_clip, txt_clip])

video.write_videofile("test.mp4")
