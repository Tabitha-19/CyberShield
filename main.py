from password_checker import check_password
from url_checker import check_url
from file_checker import check_file

print("================================")
print("          CyberShield")
print("================================")

while True:
    print("\nChoose a security option:")
    print("1. Password Security")
    print("2. URL Safety Checker")
    print("3. File Integrity Checker")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        check_password()

    elif choice == "2":
        check_url()

    elif choice == "3":
        check_file()

    elif choice == "4":
        print("\nThank you for using CyberShield!")
        break

    else:
        print("\nInvalid choice. Please enter 1, 2, 3, or 4.")