import sys
import os
import pytest
from pathlib import Path

# Get the absolute path to the project root directory
project_root = Path(__file__).parent.parent.absolute()

# Add the project root to Python path
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))


@pytest.fixture(scope="session", autouse=True)
def tests_setup_and_teardown():
    os.environ["PYTHON_ENVIRONMENT"] = "test"
    yield
    os.environ["PYTHON_ENVIRONMENT"] = "development"
