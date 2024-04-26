import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def setup():
    if os.path.exists(".env"):
        print("Setup has already been completed. Skipping...")
        return
    
    api_key = input("Enter your Groq API key: ")
    role = input("Enter your role (e.g., 'user'): ")
    model = input("Enter the model (e.g., 'mixtral-8x7b-32768'): ")


    with open(".env", "w") as f:
        f.write(f"GROQ_API_KEY={api_key}\n")
        f.write(f"GROQ_ROLE={role}\n")
        f.write(f"GROQ_MODEL={model}\n")

    print("Setup complete!")

def search(query):

    api_key = os.getenv("GROQ_API_KEY")
    role = os.getenv("GROQ_ROLE")
    model = os.getenv("GROQ_MODEL")


    client = Groq(api_key=api_key)  


    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": role,
                "content": query,
            }
        ],
        model=model,
    )


    print(chat_completion.choices[0].message.content)

def main():

    setup() 
    query = input("Enter your query: ")
    search(query)

if __name__ == "__main__":
    main()
