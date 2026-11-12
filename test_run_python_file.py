from functions.run_python_file import run_python_file

def test() -> None:
    print(f"running on main.py: {run_python_file("calculator", "main.py")}")
    print(f"running calculator: {run_python_file("calculator", "main.py", ["3 + 5"])}")
    print(f"running calc tests: {run_python_file("calculator", "tests.py")}")
    print(f"running on ../main.py: {run_python_file("calculator", "../main.py")}")
    print(f"running on nonexistent.py: {run_python_file("calculator", "nonexistent.py")}")
    print(f"running on lorem.txt: {run_python_file("calculator", "lorem.txt")}")


if __name__ == "__main__":
    test()