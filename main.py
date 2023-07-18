from src.utils import get_users_from_json, get_books_from_csv
from configuration import INPUT_FILE_PATH

if __name__ == '__main__':
    books_file = INPUT_FILE_PATH + "books.csv"
    users_file = INPUT_FILE_PATH + "users.json"

    books = get_books_from_csv(books_file)
    users = get_users_from_json(users_file)

    print(len(books), f"{books=}")
    print(len(users), f"{users=}")
