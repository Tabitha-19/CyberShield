import hashlib
import os

def check_file():

    print("================================")
    print("   CyberShield - File Check")
    print("================================")

    file_name = input("Enter the file name: ")

    # Read the file
    with open(file_name, "rb") as file:
        data = file.read()

    # Create the hash
    current_hash = hashlib.sha256(data).hexdigest()

    # Make a separate hash file for each file
    hash_file = file_name + ".hash"

    # First time checking the file
    if not os.path.exists(hash_file):

        with open(hash_file, "w") as file:
            file.write(current_hash)

        print("\nOriginal hash saved.")
        print("Run the checker again to check for changes.")

    else:
        print("\n1. Check file")
        print("2. Save current file as new original")

        choice = input("Enter your choice: ")

        if choice == "1":

            with open(hash_file, "r") as file:
                original_hash = file.read().strip()

            if current_hash == original_hash:
                print("\nFile is unchanged.")
            else:
                print("\nWarning: File has been modified.")

        elif choice == "2":

            with open(hash_file, "w") as file:
                file.write(current_hash)

            print("\nCurrent file saved as the new original.")

        else:
            print("\nInvalid choice.")