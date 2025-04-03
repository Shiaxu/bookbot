from stats import *
import sys

try:
    input1, input2 = sys.argv
    book_path = input2
except Exception:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(file_path):
    try:
        with open(file_path) as f:
            file_contents = f.read()
        return file_contents
    except Exception as e:
        print(e)
        sys.exit(1)

def main():

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words(get_book_text(book_path))} total words")
        print("--------- Character Count -------")
        final_dict = sorted_dict(char_num_times(get_book_text(book_path)))
        for dict in final_dict:
            if dict["char"].isalpha():
                print(f"{dict["char"]}: {dict["num"]}")
        print("============= END ===============")

main()