from src.main_module import main
from src.helper_module import helper_function

def test_main_function():
    assert main() == "Hello World"

def test_helper_function():
    assert helper_function() == "Helper function result"