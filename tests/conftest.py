import pytest
from src.utils import json_load


@pytest.fixture
def get_json():
    return json_load
