import os.path

from src.utils import json_load, csv_read_gen, json_dump, csv_read
from configuration import INPUT_FILE_PATH, OUTPUT_FILE_PATH


def distribute_books(books_file, users_file):
    users = json_load(users_file)

    users_output = [{
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": [],
        } for user in users]

    users_num = len(users)
    for i, book in enumerate(csv_read_gen(books_file)):
        users_output[i % users_num]["books"].append({
            "title": book["Title"],
            "author": book["Author"],
            "pages": int(book["Pages"]),
            "genre": book["Genre"],
        })

    return users_output


if __name__ == '__main__':
    books_file_path = os.path.join(INPUT_FILE_PATH, "books.csv")
    users_file_path = os.path.join(INPUT_FILE_PATH, "users.json")
    result_file_path = os.path.join(OUTPUT_FILE_PATH, "result.json")

    print("result path", result_file_path)

    json_dump(
        distribute_books(books_file_path, users_file_path),
        result_file_path
    )
