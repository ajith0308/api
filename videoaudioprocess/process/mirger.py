import moviepy.editor as mpe

# Create VideoFileClip objects for the video and audio files
video = mpe.VideoFileClip("output_video.avi")
audio = mpe.AudioFileClip("output.mp3")

# Merge the video and audio clips
final_clip = video.set_audio(audio)

# Write the merged video file to a new file
final_clip.write_videofile("final_video.mp4")
