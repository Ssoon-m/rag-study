from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

import os

def main():
    load_dotenv()

    openai_api_key = os.getenv("OPENAI_API_KEY")

    print(f"OPENAI_API_KEY={openai_api_key}")

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        openai_api_key=openai_api_key
    )


    print(f"[답변]: {llm.invoke('대한민국의 수도는 어디인가요?')}")


if __name__ == "__main__":
    main()
