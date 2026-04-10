import os
from datetime import datetime

def scan_folder_subfolder(folder_path):
    files_paths = []

    for item in os.listdir(folder_path):

        current_path = os.path.join(folder_path, item)

        if os.path.isfile(current_path):
            files_paths.append(current_path)

        elif os.path.isdir(current_path):
            sub_files = scan_folder_subfolder(current_path)  # call fc instead of writing same code, the fc only equal above so it returns a list
            files_paths.extend(sub_files)

    return files_paths


def file_counter(folder_path):
    return len(scan_folder_subfolder(folder_path)) if os.path.isdir(folder_path) else 0

def file_size(folder_path):
    files_path = scan_folder_subfolder(folder_path)
    files_size = {}

    if not files_path:
        return files_size

    for file in files_path:
        size = os.path.getsize(file)

        if size not in files_size:
            files_size[size] = []

        files_size[size].append(file)

    return files_size


def file_count_by_size(folder_path):
    files_size = file_size(folder_path)
    counter = {}

    if not files_size:
        return files_size

    for size, files in files_size.items():

        counter[size] = len(files)

    return counter

def duplicate_files(folder_path):
    counter = file_count_by_size(folder_path)
    duplicate = {}

    if not counter:
        return duplicate

    for size, file_count in counter.items():

        if file_count > 1:
            duplicate[size] = file_count

    return duplicate

def count_by_extension(folder_path):
    files_path = scan_folder_subfolder(folder_path)
    extensions_by_type = {
        "document": [".txt", ".pdf", ".docx", ".xlsx", ".csv"],
        "image": [".png", ".jpg", ".jpeg", ".gif"],
        "audio": [".mp3", ".wav"],
        "video": [".mp4", ".mov"],
        "archive": [".zip", ".rar"],
        "code": [".py", ".js", ".html", ".css"],
        "ps4_pkg" : [".pkg", ".iso", ".cso" ],
        "pc app" : [".exe", ".lnk"]
    }
    extension_counter = {}

    if not files_path:
        return extension_counter

    for file in files_path:

        file_name = os.path.basename(file)  # get file name only
        _, extension = os.path.splitext(file_name)
        extension = extension.lower()

        for types , extensions in extensions_by_type.items():

            if extension in extensions:

                if extension not in extension_counter:
                    extension_counter[extension] = {"types" : types, "count" : 1}
                else :
                    extension_counter[extension]["count"] += 1

    return extension_counter


def last_modification_by_day(folder_path):
    files_path = scan_folder_subfolder(folder_path)
    days = {}

    if not files_path:
        return days

    now = datetime.now()  # present

    for file in files_path:
        m_time = os.path.getmtime(file)   # gives time in seconds since 1/1/1970
        modified = datetime.fromtimestamp(m_time)  # transform it into readable date
        days_ago = (now - modified).days

        days[os.path.basename(file)] = days_ago

    return days

