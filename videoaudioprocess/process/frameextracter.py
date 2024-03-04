# frameextracter.py

import sys
from pytube import YouTube
import cv2


# Function to get multiple thumbnail images from a YouTube video
def get_youtube_thumbnails(url, num_frames):
    try:
        # Download the YouTube video
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        video_path = stream.download(filename="video")

        # Extract frames (thumbnails) from the video
        cap = cv2.VideoCapture(video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_interval = total_frames // num_frames

        for i in range(num_frames):
            frame_num = i * frame_interval
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
            ret, frame = cap.read()

            # Save the frame as an image
            if ret:
                save_as = f"thumbnail_{i + 1}.jpg"
                cv2.imwrite(save_as, frame)
                # print(f"Thumbnail {i + 1} saved as {save_as}")
            else:
                print(f"Failed to capture frame {i + 1}, check the video URL")

        # Release the capture and delete the video file
        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    video_url = sys.argv[1]
    print("vido", video_url)
    num_frames = 30
    get_youtube_thumbnails(video_url, num_frames)
