import os
import subprocess

def run_python_file(
        working_directory: str, file_path: str, args: list[str] | None = None 
) -> str:

    try:    
        abs_working_path = os.path.abspath(working_directory)
        absolute_file_path = os.path.normpath(os.path.join(abs_working_path, file_path))

        if os.path.commonpath([abs_working_path, absolute_file_path]) != abs_working_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", absolute_file_path]

        if args:
            command.extend(args)

        sprocess = subprocess.run(command, capture_output=True, text=True, timeout=30)

        output_str = ""

        output_str += f"STDOUT: {sprocess.stdout}, STDERR: {sprocess.stderr}"
        if sprocess.returncode != 0:
            output_str += f"Process exited with code {sprocess.returncode}"

        if sprocess.stdout == sprocess.stderr == None:
            output_str += f"No output produced"

        return output_str

    except Exception as e:
        return f"Error: executing Python file: {e}"