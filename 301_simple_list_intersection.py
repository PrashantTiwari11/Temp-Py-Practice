"""Project 301: Find Common Items in Two Lists"""
def read_items(prompt):
    return [item.strip() for item in input(prompt).split(",") if item.strip()]

def main():
    first = read_items("Enter first list items separated by commas: ")
    second = read_items("Enter second list items separated by commas: ")
    common = list(dict.fromkeys(item for item in first if item in second))
    print("Common items:", common if common else "No common items found.")

if __name__ == "__main__":
    main()
