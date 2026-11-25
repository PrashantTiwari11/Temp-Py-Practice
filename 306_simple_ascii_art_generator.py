# Simple ASCII Art Generator

print("Choose an art:")
print("1. Heart")
print("2. Star")
print("3. Smiley")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    print("  **   **")
    print(" **** ****")
    print("***********")
    print(" *********")
    print("  *******")
    print("   *****")
    print("    ***")
    print("     *")
elif choice == "2":
    print("    *")
    print("   ***")
    print("  *****")
    print(" *******")
    print("*********")
    print("   ***")
    print("   ***")
elif choice == "3":
    print("  *****")
    print(" *     *")
    print("*  o o  *")
    print("*   ^   *")
    print("*  \\_/  *")
    print(" *     *")
    print("  *****")
else:
    print("Invalid choice.")
