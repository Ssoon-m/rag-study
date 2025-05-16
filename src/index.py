from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

import os


def main():
    load_dotenv()

    template = "{country}의 수도는 어디인가요?"

    prompt_template = ChatPromptTemplate.from_template(template)
    prompt = prompt_template.format_prompt(country="대한민국")

    print(prompt.to_string())

    # openai_api_key = os.getenv("OPENAI_API_KEY")

    # print(f"OPENAI_API_KEY={openai_api_key}")

    # llm = ChatOpenAI(
    #     temperature=0.1,  # 창의성 (0.0 ~ 2.0)
    #     model="gpt-4o",
    # )

    # print(f"[답변]: {llm.invoke('대한민국의 수도는 어디인가요?')}")


if __name__ == "__main__":
    main()
