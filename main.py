import sys
from stats import count_words_book, sort_characters_by_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    count_words_book(filepath)
    print("--------- Character Count -------")
    sort_characters_by_count(filepath)
    print("============= END ===============")

main()