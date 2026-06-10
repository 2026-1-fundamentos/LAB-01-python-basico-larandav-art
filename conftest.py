import os
import pytest

@pytest.fixture(autouse=True)
def change_dir():
    root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(os.path.join(root, "homework"))
    yield
    os.chdir(root)