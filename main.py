import os
from LOGIC.core import (
    file_counter,
    file_size,
    file_count_by_size,
    duplicate_files,
    count_by_extension,
    last_modification_by_day
)
from UTILITY.tools import (
    search_file,
    searched_file_size,
    searched_by_extension
)

def main():
    folder_path = input("Enter folder path: ").strip()

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    while True:
        print("\n=== FILE MANAGEMENT TOOL ===")
        print("1. Search file by name")
        print("2. Search file by extension")
        print("3. Search file size")
        print("4. Count all files")
        print("5. Count files by extension type")
        print("6. Show duplicate files")
        print("7. Last modification by day")
        print("8. Show all file sizes")
        print("9. Count files by size")
        print("10. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            search_file(folder_path)

        elif choice == "2":
            searched_by_extension(folder_path)

        elif choice == "3":
            results = searched_file_size(folder_path)
            if results:
                print("\nFile size results:")
                for size, files in results.items():
                    print(f"\nSize: {size} bytes")
                    for f in files:
                        print(" -", f)

        elif choice == "4":
            total = file_counter(folder_path)
            print(f"\nTotal files: {total}")

        elif choice == "5":
            ext_count = count_by_extension(folder_path)
            print("\nFiles by extension type:")
            for ext, count in ext_count.items():
                print(f"{ext}: {count}")

        elif choice == "6":
            dup = duplicate_files(folder_path)
            if dup:
                print("\nDuplicate files by size:")
                for size, count in dup.items():
                    print(f"{size} bytes → {count} files")
            else:
                print("No duplicates found.")

        elif choice == "7":
            mods = last_modification_by_day(folder_path)
            print("\nLast modification (days ago):")
            for file, days in mods.items():
                print(f"{file}: {days} days ago")

        elif choice == "8":
            sizes = file_size(folder_path)
            print("\n=== FILE SIZES ===")
            for size, files in sizes.items():
                print(f"\n{size} bytes:")
                for f in files:
                    print(" -", f)

        elif choice == "9":
            counts = file_count_by_size(folder_path)
            print("\n=== FILE COUNT BY SIZE ===")
            for size, count in counts.items():
                print(f"{size} bytes → {count} file(s)")

        elif choice == "10":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()