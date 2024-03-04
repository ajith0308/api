import os


def delete_matching_files(prefix="thumb", suffix=".jpg"):
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory)
    folder_path = os.path.abspath(
        os.path.join(os.path.abspath(os.path.join(file_path, os.pardir)), os.pardir)
    )
    print("folder_path", folder_path)
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
if __name__ == "__main__":
    delete_matching_files()
