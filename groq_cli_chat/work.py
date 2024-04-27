import os
import json
from groq import Groq
import argparse
import time
import threading

def get_script_dir():
    return os.path.dirname(os.path.realpath(__file__))

def check_setup():
    config_path = os.path.join(get_script_dir(), "config.json")
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = json.load(f)
        if config.get("SETUP_COMPLETE") == "True":
            return True
    return False

def setup():
    if check_setup():
        return

    api_key = input("Enter your API key: ")

    print("\nChoose a role:")
    print("1. System: Can be used to provide specific instructions for how it should behave throughout the conversation.")
    print("2. User: Messages written by a user of the LLM.")
    print("3. Assistant: Messages written by the LLM in a previous completion.")

    while True:
        role_choice = input("\nEnter your role choice (1, 2, or 3): ")
        if role_choice in ['1', '2', '3']:
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    role_dict = {
        '1': 'system',
        '2': 'user',
        '3': 'assistant'
    }

    role = role_dict[role_choice]

    print("\nChoose a model:")
    print("1. LLaMA3 8b")
    print("2. LLaMA3 70b")
    print("3. Mixtral 8x7b")
    print("4. Gemma 7b")

    while True:
        model_choice = input("\nEnter your model choice (1, 2, 3, or 4): ")
        if model_choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    model_dict = {
        '1': 'llama3-8b-8192',
        '2': 'llama3-70b-8192',
        '3': 'mixtral-8x7b-32768',
        '4': 'gemma-7b-it'
    }

    model = model_dict[model_choice]

    config = {
        "GROQ_API_KEY": api_key,
        "GROQ_ROLE": role,
        "GROQ_MODEL": model,
        "SETUP_COMPLETE": "True"
    }

    with open(os.path.join(get_script_dir(), "config.json"), "w") as f:
        json.dump(config, f)

    print("Setup complete!")

def loading_animation():
    animation = "|/-\\"
    for _ in range(10):
        for char in animation:
            print(f"Searching              {char}", end="\r")
            time.sleep(0.1)

def search(query):
    with open(os.path.join(get_script_dir(), "config.json"), "r") as f:
        config = json.load(f)
    api_key = config["GROQ_API_KEY"]
    role = config["GROQ_ROLE"]
    model = config["GROQ_MODEL"]

    client = Groq(api_key=api_key)

    thread = threading.Thread(target=loading_animation)
    thread.start()

    time.sleep(1)

    thread.join()

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": role,
                "content": query,
            }
        ],
        model=model,
    )

    print("\033[K\r", end="")
    print("\n", chat_completion.choices[0].message.content)

def main():
    parser = argparse.ArgumentParser(description='Process query string or prompt for input.')
    parser.add_argument('query', nargs='*', help='Query string to search')

    args = parser.parse_args()

    setup()

    if args.query:
        query = ' '.join(args.query)
        search(query)
    else:
        query = input("Enter your query: ")
        search(query)

if __name__ == "__main__":
    main()
