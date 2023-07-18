import os.path
import json
import csv


def json_dump(obj: dict, filename: str) -> None:
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)


def get_books_from_csv(filename: str) -> list[dict]:
    if os.path.exists(filename):
        with open(filename, "r", newline="") as csvfile:
            return list(csv.DictReader(csvfile))
    else:
        raise FileNotFoundError(
            f'Файл {filename} не найден,\n'
            'пожалуйста, предоставьте файл по указанному пути')


def get_users_from_json(filename: str) -> list[dict]:
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    else:
        raise FileNotFoundError(
                f'Файл {filename} не найден,\n'
                'пожалуйста, предоставьте файл по указанному пути')
