"""Check whether two phrases are anagrams, ignoring spaces and case."""
def normalize(text):
    return sorted(char.lower() for char in text if char.isalnum())

def main():
    first = input("Enter the first word or phrase: ")
    second = input("Enter the second word or phrase: ")
    print("They are anagrams." if normalize(first) == normalize(second)
          else "They are not anagrams.")

if __name__ == "__main__":
    main()
