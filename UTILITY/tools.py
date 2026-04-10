import os
from LOGIC.core import scan_folder_subfolder, file_size

def search_file(folder_path):
    files_path = scan_folder_subfolder(folder_path)

    while True:
        user = input("Please enter your file name or 'exit' to quit: ").strip()

        if user.lower() == 'exit':
            print("Exiting...")
            break

        if not user:
            print("Please enter a valid file name or 'exit' to quit")
            continue

        matches = []
        for file in files_path:
            file_name = os.path.basename(file)
            name, extension = os.path.splitext(file_name) # remove extension limitation

            if user.lower() == name.lower():
                matches.append(file)

        if matches:
            print(f"Found {len(matches)} file(s):")
            for m in matches:
                print(" -", m)
            return matches
        else:
            print("No files found with that name. Try again.")


def searched_file_size(folder_path):
    files_size = file_size(folder_path)

    while True:
        user = input("Please enter your file name or 'exit' to quit: ").strip()

        if user.lower() == 'exit':
            print("Exiting...")
            break

        if not user:
            print("Please enter a valid file name or 'exit' to quit")
            continue

        results = {}

        for size, files in files_size.items():
            for file in files:
                file_name = os.path.basename(file)

                if user.lower() == file_name.lower():
                    if size not in results:
                        results[size] = []
                    results[size].append(file)

        if results:

            return results
        else:
            print("No files found with that name. Try again.")

def searched_by_extension(folder_path):
    files_path = scan_folder_subfolder(folder_path)

    while True:
        user = input("Please enter the extension of the file (.png) or 'exit' to quit: ").strip()

        if user.lower() == 'exit':
            print("Exiting...")
            break

        elif not user:
            print("Please enter a valid file extension or 'exit' to quit")
            continue

        matches = []

        if not user.startswith('.'):
             user = "." + user

        for file in files_path:
            file_name = os.path.basename(file)
            _, extension = os.path.splitext(file_name)

            if user.lower() == extension.lower():
                matches.append(file)

        if matches:
            print(f"Found {len(matches)} file(s):")
            for m in matches:
                print(" -", m)
            return matches

        else:
            print("No files found with that extension. Try again.")



