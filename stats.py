def count_words_book(filepath):
    with open(filepath) as file:
        text = file.read()
        num_words = count_words(text)
        print(f"Found {num_words} total words")

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(filepath):
    with open(filepath) as file:
        text = file.read()
        text = text.lower()
        char_count = {}
        for char in text:
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        return char_count

def sort_characters_by_count(filepath):
    char_count = count_characters(filepath)
    sorted_characters = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_characters:
        print(f"{char}: {count}")

