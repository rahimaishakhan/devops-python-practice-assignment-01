import shutil # Default library for high-level file operations (like copying files).
import os     # Default library for interacting with the operating system (checking paths, joining directories).
import sys    # Default library to read command-line arguments (used for source and destination paths).
from datetime import datetime # Default library to handle dates and times (used for unique timestamps).

# ------------------------- FUNCTION DEFINITION ----------------------------------

def backup_files(source_dir: str, destination_dir: str):
    """
    Copies files from source to destination, adding a timestamp on conflict to ensure uniqueness.
    """
    print(f"Starting backup from '{source_dir}' to '{destination_dir}'...")

    # 1. Error Handling: Check if the source directory exists.

    # os.path.isdir() is a DEFAULT PYTHON FUNCTION that checks if the path is a valid directory.
    if not os.path.isdir(source_dir):
        print(f"❌ Error: Source directory '{source_dir}' does not exist.")
        return # Stop execution if the source is missing.

    # 2. Ensure the destination directory exists (create it if needed).
    try:
        # os.makedirs() creates the directory. exist_ok=True is a Best Practice 
        # because it ignores the error if the folder already exists.
        os.makedirs(destination_dir, exist_ok=True) 
        print(f"Destination directory '{destination_dir}' is ready.")
    except Exception as e:
        print(f"❌ Error creating destination directory: {e}")
        return

    # 3. Get the list of files to copy.
    # os.listdir() lists contents. The list comprehension filters it to ONLY include files.
    files_to_copy = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    
    if not files_to_copy:
        print("ℹ️ Source directory is empty. Nothing to copy.")
        return

    # Loop through every file found in the source directory.
    for filename in files_to_copy:
        # os.path.join() is a Best Practice to correctly combine directory names across different operating systems.
        source_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(destination_dir, filename)

        # Check for file existence in the destination.
        if os.path.exists(dest_path):
            # If the file exists, we create a timestamp for the new file name.
            current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # os.path.splitext() separates the filename (e.g., 'report.txt') into the base ('report') and the extension ('.txt').
            base, ext = os.path.splitext(filename)
            # Create the unique new file name: base_timestamp.ext
            new_filename = f"{base}_{current_timestamp}{ext}"
            final_dest_path = os.path.join(destination_dir, new_filename)
            
            print(f"⚠️ Conflict! Saving '{filename}' as '{new_filename}' to ensure uniqueness.")
        else:
            # If no conflict, we use the original destination path.
            final_dest_path = dest_path

        # 4. Perform the copy operation.
        try:
            # shutil.copy2 is the recommended method for backup as it preserves file details like creation time.
            shutil.copy2(source_path, final_dest_path) 
            print(f"✅ Successfully backed up: {filename}")
        except Exception as e:
            # Handle unexpected errors during the copy process (e.g., permissions error).
            print(f"❌ Failed to copy '{filename}': {e}")
    
    print("\n✨ Backup process completed.")


# ------------------------- SCRIPT EXECUTION ----------------------------------
if __name__ == "__main__":
    # Check if the user provided the two necessary command-line arguments (source and destination).
    # sys.argv is a list of arguments: [script_name, arg1, arg2]. We need a length of 3.
    if len(sys.argv) != 3:
        print("Usage: python q4_backup_utility.py <source_directory> <destination_directory>")
        sys.exit(1) # Exit with an error code if arguments are missing.
    
    # sys.argv[1] is the first argument the user typed (the source directory name).
    source = sys.argv[1] 
    # sys.argv[2] is the second argument (the destination directory name).
    destination = sys.argv[2] 
    
    backup_files(source, destination)
