from functions.write_file import write_file

def test() -> None:
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"result: {result}")

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"result: {result}")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"result: {result}")

if __name__ == "__main__":
    test()