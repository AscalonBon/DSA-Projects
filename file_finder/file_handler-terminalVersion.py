import os
import re

class FileHandler:
    def __init__(self):
        self.selected_file_path = None
    
    def str_finder(self):
        if not self.selected_file_path:
            print("No file selected. Please select a file first.")
            return

        # Prompt the user for the search pattern or keyword
        pattern = input("Enter the search pattern or keyword: ")
        try:
            with open(self.selected_file_path, 'r') as file:
                content = file.read()
                # Count occurrences of the pattern in the content
                count = content.count(pattern)  # Use str.count for exact matches
                result_text = f"The pattern '{pattern}' was found {count} times in the file."
        except FileNotFoundError:
            result_text = "File not found. Please ensure the file path is correct."
        except Exception as e:
            result_text = f"An error occurred: {str(e)}"

        print(result_text)

    def select_file(self):
        # Prompt user for a directory to search for files
        search_dir = input("Enter the directory to search for files (leave blank for current directory): ")
        if not search_dir:
            search_dir = os.getcwd()  # Use current directory if none provided

        # Prompt for a keyword to search for in file names
        keyword = input("Enter a keyword to search for in file names: ")
        found_files = []

        # Search for files matching the keyword
        for root, dirs, files in os.walk(search_dir):
            for file in files:
                # Check if the keyword is in the filename (case insensitive)
                if re.search(re.escape(keyword).replace(r'\*', '.*'), file, re.IGNORECASE):
                    found_files.append(os.path.join(root, file))

        # Display found files
        if found_files:
            print(f"Found {len(found_files)} file(s) matching '{keyword}':")
            for index, found_file in enumerate(found_files):
                print(f"{index + 1}: {found_file}")

            # Allow user to select a file by number
            file_choice = input("Enter the number of the file you want to select (or 'cancel' to abort): ")
            if file_choice.isdigit() and 1 <= int(file_choice) <= len(found_files):
                self.selected_file_path = found_files[int(file_choice) - 1]
                print(f"Selected file: {self.selected_file_path}")
            else:
                print("No valid file selected.")
        else:
            print(f"No files found with '{keyword}' in the name.")

    def file_finder(self):
        directories = []
        user_input_dir = input("Enter a directory (leave blank to use default directories): ")

        if user_input_dir:
            directories.append(user_input_dir)
        else:
            home_dir = os.path.expanduser("~")
            directories = [
                os.path.join(home_dir, "Desktop"),
                os.path.join(home_dir, "Documents"),
                os.path.join(home_dir, "Downloads"),
                os.path.join(home_dir, "Music"),
                os.path.join(home_dir, "Pictures"),
                os.path.join(home_dir, "Videos")
            ]

        keyword = input("Enter a keyword to search for in file names: ")
        found_files = []

        for directory in directories:
            if os.path.isdir(directory):
                for root, dirs, files in os.walk(directory):
                    for file in files:
                        if re.search(keyword, file, re.IGNORECASE):
                            found_files.append(os.path.join(root, file))

        if found_files:
            print(f"Found {len(found_files)} file(s) matching '{keyword}':")
            for found_file in found_files:
                print(found_file)
        else:
            print(f"No files found with '{keyword}' in the name.")

    def run(self):
        while True:
            general_input = input("\nEnter 'start' to proceed or 'quit' to exit the program: ").strip().lower()
            if general_input == 'quit':
                print("Exiting the program.")
                break
            elif general_input == 'start':
                print("\n--- File Handler Menu ---")
                print("1. Search String in Selected File")
                print("2. Search Files in Directory")
                print("3. Quit Program")
                choice = input("Enter your choice (1-3): ")

                if choice == '1':
                    self.select_file()  # Use terminal to select a file
                    self.str_finder()
                elif choice == '2':
                    self.file_finder()
                elif choice == '3':
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("Invalid input. Please enter 'start' or 'quit'.")

if __name__ == "__main__":
    file_handler = FileHandler()
    file_handler.run()
