from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Keep conversation context
conversation = [
    {"role": "system", "content": 
     "You are Abhimanyu, a friendly and knowledgeable technical tutor. "
     "You can answer questions about DSA, Python, SQL Server, Angular, "
     "basic Data Science, and Azure. Explain clearly in English with examples. "
     "Answer concisely and provide only accurate technical information."}
]

def ask_abhi(prompt):
    # Append user input
    conversation.append({"role": "user", "content": prompt})
    
    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation
    )
    
    reply = response.choices[0].message.content
    # Append AI reply to conversation
    conversation.append({"role": "assistant", "content": reply})
    return reply

def print_response_in_chunks(text, chunk_size=500):
    for i in range(0, len(text), chunk_size):
        print(f"Abhi: {text[i:i+chunk_size]}")

if __name__ == "__main__":
    print("Abhimanyu Multi-Topic Chatbot (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Abhi: Theek hai bhai, milte hain! 🚀")
            break
        try:
            reply = ask_abhi(user_input)
            print_response_in_chunks(reply)
        except Exception as e:
            print(f"Abhi: Error occurred - {e}")
