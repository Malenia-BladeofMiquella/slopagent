import os


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_working_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_working_path, file_path))
        
        if os.path.commonpath([abs_working_path, target_path]) != abs_working_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_path, "r") as file:
            file_content = file.read(10000)
            if file.read(1):
                file_content += f'[...File "{file_path}" truncated at {10000} characters]'

        return file_content

    except Exception as e:
        return f"Error: {e}"

        
schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the content of a file (at most 10,000 characters) of a specified file within the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "path to the file to read, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}