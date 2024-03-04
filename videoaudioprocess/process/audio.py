import sys
import pyttsx3
from summarize import *


def text_to_speech(text, output_file):
    summaryoftext = summarize_text(text)
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty("rate", 200)  # Speed percent (can go over 100)
    engine.setProperty("volume", 1)  # Volume 0-1

    # Save audio to a file
    engine.save_to_file(summaryoftext, output_file)

    # Wait for the speech to complete
    engine.runAndWait()


# Example usage:
if __name__ == "__main__":
    text = sys.argv[1]
    output_file = "output.mp3"
    text_to_speech(text, output_file)
    print(f"Audio saved to {output_file}")
