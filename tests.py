from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


def test():

    result = run_python_file("calculator", "main.py")
    print("Test 1:")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Test 2:")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Test 3:")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Test 4:")
    print(result)
    print("")

if __name__ == "__main__":
    test()