import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    verbose = False

    if len(sys.argv[0]) != 2 and not isinstance(sys.argv[1], str):
        print("exiting with error 1")
        return 1
    
    user_prompt = sys.argv[1]

    if '--verbose' in sys.argv:
        verbose = True
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,  
    )

    if verbose:
        print(f"User prompt: {user_prompt}")
        prompt_token_qty = response.usage_metadata.prompt_token_count
        response_token_qty = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {prompt_token_qty}")
        print(f"Response tokens: {response_token_qty}")

    print(response.text)


if __name__ == "__main__":
     main()
