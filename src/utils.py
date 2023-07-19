import os.path
import json
import csv
from typing import Generator


def json_dump(obj: dict, filename: str) -> None:
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)


def csv_read(filename: str) -> list[dict]:
    if os.path.exists(filename):
        with open(filename, "r", newline="") as csvfile:
            return list(csv.DictReader(csvfile))
    else:
        raise FileNotFoundError(
            f'Файл {filename} не найден,\n'
            'пожалуйста, предоставьте файл по указанному пути')


def json_load(filename: str) -> list[dict]:
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    else:
        raise FileNotFoundError(
                f'Файл {filename} не найден,\n'
                'пожалуйста, предоставьте файл по указанному пути')


def csv_read_gen(filename: str) -> Generator[dict, None, None]:
    if os.path.exists(filename):
        with open(filename, "r", newline="") as csvfile:
            for row in csv.DictReader(csvfile):
                yield row
    else:
        raise FileNotFoundError(
            f'Файл {filename} не найден,\n'
            'пожалуйста, предоставьте файл по указанному пути')
