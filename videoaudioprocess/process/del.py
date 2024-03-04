import os


def delete_matching_files(folder_path, prefix="thumb", suffix=".jpg"):
    for filename in os.listdir(folder_path):
        if filename.startswith(prefix) and filename.endswith(suffix):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                except FileNotFoundError:
                    print(f"File '{file_path}' not found.")
                except PermissionError:
                    print(f"Permission denied while deleting '{file_path}'.")


# Example usage
folder_to_search = "C:/Users/ACS/Desktop/ecom/vid_summary_api/vid_summary_api"  # Replace with your actual folder path
delete_matching_files(folder_to_search)
