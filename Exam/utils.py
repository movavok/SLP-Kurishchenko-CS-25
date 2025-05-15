def interface():
    while True:
        print("Welcome to the program!")
        print("1. Task 1")
        print("2. Task 2")
        print("3. Task 3")
        print("0. Exit")
        choice = input("Please select an option: ")
        match choice:
            case "1":
                list_to_clean = input("Enter a list of anything (space-separated): ").split()
                print("Original list: ", list_to_clean)
                result = clean_list(list_to_clean)
                print("Cleaned list: ", result)

            case "2":
                a = input("Enter the first number (A): ").strip()
                b = input("Enter the second number (B): ").strip()
                if not (a.isdigit() and b.isdigit() and int(a) >= 0 and int(b) >= 0):
                    print("Both inputs must be non-negative integers.")
                    continue
                result = counter(a, b)
                print("The number of distinct digits from B in A is: ", result)

            case "3":
                text = input("Enter a text: ")
                if not text:
                    print("Text cannot be empty.")
                    continue 
                find_most_frequent(text)

            case "0": 
                print("Exiting the program.")
                return
            case _:
                print("Invalid choice. Please try again.")
                interface()

def clean_list(list_to_clean):
    """
    Cleans a list by removing duplicates.
    """
    seen = set()
    cleaned_list = []
    for item in list_to_clean:
        if item not in seen:
            seen.add(item)
            cleaned_list.append(item)
    return cleaned_list

def counter(a, b):
    """
    Print the number of distinct digits from B that are present in A.
    Accepts only positive integers as input.
    """
    a = str(a)
    b = str(b)
    count = 0
    for digit in b:
        if digit in a:
            count += 1
    return count

def find_most_frequent(text):
    """
    Find the most frequent word in a text.
    """
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    if len(word_count) == len(words):
        print("All words are unique.")
    else:
        most_frequent_word = max(word_count, key=word_count.get)
        print(f"The most frequent word is '{most_frequent_word}' with {word_count[most_frequent_word]} occurrences.")
    
    