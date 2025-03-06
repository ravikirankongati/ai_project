import os

from dotenv import load_dotenv
from openai import OpenAI


# load_dotenv()
load_dotenv(dotenv_path=".env")


# Load the API key from the environment
# create an instance of the OpenAI class
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "Write a limerick about the Python programming language.",
        },
    ],
)

response = completion.choices[0].message.content
