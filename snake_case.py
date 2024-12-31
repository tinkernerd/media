import os
import re


def to_snake_case(name):
    """Converts a string to snake_case."""
    base, ext = os.path.splitext(name)  # Split the name into base and extension
    base = re.sub(
        r"[^a-zA-Z0-9]", "_", base
    )  # Replace non-alphanumeric characters with underscores
    base = re.sub(
        r"(?<!^)(?=[A-Z])", "_", base
    ).lower()  # Add underscores before capital letters and convert to lowercase
    base = (
        re.sub(r"_+", "_", base).strip("_").rstrip("_ ").strip()
    )  # Remove consecutive underscores, trailing underscores/spaces, and strip leading/trailing whitespace
    return f"{base}{ext}"  # Recombine base with the original extension


def rename_files_to_snake_case():
    root_folder = os.getcwd()  # Get the current working directory
    for root, dirs, files in os.walk(root_folder):
        # Skip any folders or files that start with a dot (including `.github`)
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        for file_name in files:
            if file_name.startswith("."):
                continue

            old_path = os.path.join(root, file_name)
            new_name = to_snake_case(file_name)
            new_path = os.path.join(root, new_name)

            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")


if __name__ == "__main__":
    rename_files_to_snake_case()
