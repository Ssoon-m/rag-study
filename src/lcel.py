from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

import os


def main():
    load_dotenv()

    prompt = PromptTemplate.from_template("{topic} 에 대해 {how} 설명해주세요.")

    model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.1)

    chain = prompt | model

    input = {"topic": "인공지능 모델의 학습 원리", "how": "영어로"}

    chain.invoke(input)


if __name__ == "__main__":
    main()
