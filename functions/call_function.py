from functions import get_file_content, get_files_info, run_python, write_file
from google import genai

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_name = function_call_part.name
    working_directory = "./calculator"
    functions = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python": run_python,
        "write_file": write_file,
    }

    if function_call_part.name not in functions.keys():
        return genai.types.Content(
            role="tool",
            parts=[
                genai.types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    kwargs = [working_directory].extend(function_call_part.args)
    function_result = functions[function_name](**kwargs)

    return genai.types.Content(
        role="tool",
        parts=[
            genai.types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )