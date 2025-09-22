from stats import word_count
from stats import character_count
from stats import dict_to_list
from stats import dict_format
from stats import sort_on
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]


def get_book_text(file):
    with open(file) as f:
        content = f.read()
        return content

def main():
    story = get_book_text(book)
    total_words = word_count(story)
    x = character_count(story)
    list = dict_format(x)
    list.sort(reverse=True,key=sort_on)
    for i in list:
        print(f"{i["char"]}: {i["num"]}")
main()




