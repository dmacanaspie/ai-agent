import os

def write_file(working_directory, file_path, content):
    abs_file_path = os.path.abspath(working_directory, file_path)
    abs_working_dir = os.path.abspath(working_directory)
    if not abs_file_path.startswith(abs_working_dir):
        f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(abs_file_path):
            with open(file_path, "x") as f:
                f.write(content)
        else:
            with open(file_path, "w") as f:
                f.write(content)
    except Exception as e:
        return "Error: Writing to {file_path}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'