from functions.get_file_content import get_file_content

def test() -> None:
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    get_file_content("calculator", "main.py")
    result = get_file_content("calculator", "main.py")
    print(f"main.py length: {len(result)}")
    print(f"main.py truncated: {'truncated' in result}")
    print(f"{result}")

    get_file_content("calculator", "pkg/calculator.py")
    result = get_file_content("calculator", "pkg/calculator.py")
    print(f"pkg/calculator.py length: {len(result)}")
    print(f"pkg/calculator.py truncated: {'truncated' in result}")
    print(f"{result}")
    
    get_file_content("calculator", "/bin/cat")
    result = get_file_content("calculator", "/bin/cat")
    print(f"{result}")

    get_file_content("calculator", "pkg/does_not_exist.py") 
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"{result}")
if __name__ == "__main__":
    test()