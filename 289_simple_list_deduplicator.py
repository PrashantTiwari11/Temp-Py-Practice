"""Project 289: Remove Duplicate Items from a List"""
def main():
    raw = input("Enter items separated by commas: ")
    items = [item.strip() for item in raw.split(",") if item.strip()]
    unique_items = list(dict.fromkeys(items))
    print("Original items:", items)
    print("Items without duplicates:", unique_items)
    print("Duplicates removed:", len(items) - len(unique_items))

if __name__ == "__main__":
    main()
