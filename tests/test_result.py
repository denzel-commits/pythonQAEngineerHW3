import pytest
import json
from configuration import OUTPUT_FILE_PATH
from src.pydantic_schemas.result_json import User


@pytest.mark.parametrize("result_file_path", [OUTPUT_FILE_PATH+"result.json"])
def test_result_json(result_file_path):
    with open(result_file_path, "r") as json_file:
        json.load(json_file)


@pytest.mark.parametrize("result_file_path", [OUTPUT_FILE_PATH+"result.json"])
def test_result_structure(result_file_path, get_json):
    result = get_json(result_file_path)

    if isinstance(result, list):
        for user in result:
            User.model_validate(user)
    else:
        User.model_validate(result)
