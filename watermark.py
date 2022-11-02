from moviepy.editor import *

video_clip = VideoFileClip("Future_Generali_Editable_Video.mp4", audio=True)

video_clip = video_clip.subclip(0, 5)

txt_clip = TextClip("Vanshul", fontsize=30, color="black")

txt_clip = txt_clip.set_pos("bottom", 30).set_duration(5)

video = CompositeVideoClip([video_clip, txt_clip])

video.write_videofile("text_add_result.mov", fps=24)
