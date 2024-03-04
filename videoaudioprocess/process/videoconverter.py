import cv2
import os


# Function to merge images into a video
def images_to_video(video_name, fps=1):
    images = [img for img in os.listdir() if img.endswith(".jpg")]
    if not images:
        print("No JPEG images found in the working directory.")
        return

    frame = cv2.imread(images[0])
    height, width, layers = frame.shape

    video = cv2.VideoWriter(
        video_name, cv2.VideoWriter_fourcc(*"DIVX"), fps, (width, height)
    )

    for image in images:
        video.write(cv2.imread(image))

    cv2.destroyAllWindows()
    video.release()


# Example usage
if __name__ == "__main__":
    video_name = "output_video.avi"
    images_to_video(video_name, fps=1)
