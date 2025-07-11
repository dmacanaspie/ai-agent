from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


def test():

    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Test 1:")
    print(result)
    print("")

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Test 2:")
    print(result)
    print("")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Test 3:")
    print(result)
    print("")

if __name__ == "__main__":
    test()