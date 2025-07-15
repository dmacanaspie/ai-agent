import os
from functions.get_files_info import get_files_info
from config import CHAR_LIMIT
from google import genai


def get_file_content(working_directory, file_path):
    """
    given file name and working directory, return up to CHAR_LIMIT characters
    """

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_file_path, "r") as f:
            content = f.read(CHAR_LIMIT)
            if os.path.getsize(abs_file_path) > CHAR_LIMIT:
                content += (
                    f'[...File "{file_path}" truncated at {CHAR_LIMIT} characters]'
                )
        return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'

schema_get_files_info = genai.types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "directory": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

available_functions = genai.types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)
