import argparse
import os
import json
import sys

from prompts import system_prompt
from dotenv import load_dotenv
from openai import OpenAI
from call_function import available_functions, call_function


def main() -> None:
    parser = argparse.ArgumentParser(description="slopagent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("environment variable/api key not found")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")

    for _ in range(20):

        iteration_result = generate_content(client, messages, args.verbose)
        if iteration_result:
            print(iteration_result)
            return

    print("maximum number of iterations reached")
    sys.exit(1)

def generate_content(client: OpenAI, messages: list, verbose: bool) -> str | None:

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        )
    if not response.usage:
        raise RuntimeError("failed API request (empty response variable)")

    if verbose:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")


    message = response.choices[0].message
    messages.append(message)
    if message.tool_calls:
        for tool_call in message.tool_calls:
            if tool_call.type != "function":
                continue
            result_message = call_function(tool_call, verbose)
            if not result_message["content"]:
                raise Exception(f"empty function response for {tool_call.function.name}")
            messages.append(result_message)

            if verbose:
                print(f"-> {result_message['content']}")
    else:
            
            return f"Response: {message.content}"
            

if __name__ == "__main__":
    main()