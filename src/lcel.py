from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
)
from operator import itemgetter
from datetime import datetime


def main():
    prompt = PromptTemplate.from_template("{topic} 에 대해 {how} 설명해주세요.")
    model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.1)
    parser = StrOutputParser()

    chain = prompt | model | parser

    input = {"topic": "인공지능 모델의 학습 원리", "how": "영어로"}

    answer = chain.invoke(input)

    print(answer)


def output_parser_test():
    template = """
    당신은 영어를 가르치는 10년차 영어 선생님입니다. 주어진 상황에 맞는 영어 회화를 작성해 주세요.
    양식은 [FORMAT]을 참고하여 작성해 주세요.

    #상황:
    {question}

    #FORMAT:
    - 영어 회화:
    - 한글 해석:
    """

    # 프롬프트 템플릿을 이용하여 프롬프트를 생성합니다.
    prompt = PromptTemplate.from_template(template)

    # ChatOpenAI 챗모델을 초기화합니다.
    model = ChatOpenAI(model_name="gpt-4-turbo")
    parser = StrOutputParser()

    chain = prompt | model | parser

    input = {"question": "저는 식당에 가서 음식을 주문하고 싶어요"}

    answer = chain.stream(input)

    for chunk in answer:
        print(chunk, end="", flush=True)


# 한번에 여러 개의 입력을 처리하는 배치 처리
def lcel_batch_test():
    prompt = PromptTemplate.from_template("{topic} 에 대해 설명해주세요.")
    model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.1)
    parser = StrOutputParser()

    chain = prompt | model | parser

    input = [
        {"topic": "ChatGPT"},
        {"topic": "Instagram"},
    ]

    answer = chain.batch(input, config={"max_concurrency": 2})

    print(answer)


def runnable_parrel_test():
    model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.1)

    chain1 = (
        PromptTemplate.from_template("{country} 의 수도는 어디야?")
        | model
        | StrOutputParser()
    )

    chain2 = (
        PromptTemplate.from_template("{country} 의 면적은 얼마야?")
        | model
        | StrOutputParser()
    )

    # 위 2개의 체인을 동시에 생성하는 병렬 실행 체인을 생성합니다.
    # 첫 번째 체인 답변에 대한걸 capital이라는 키에 넣고, 두 번째 체인 답변에 대한걸 area라는 키에 넣습니다.
    combined = RunnableParallel(capital=chain1, area=chain2)

    input = {"country": "한국"}

    # 병렬 실행 체인을 실행
    answer = combined.invoke(input)

    print(answer)
    # 출력 : {'capital': '한국의 수도는 서울입니다.', 'area': '한국(대한민국)의 면적은 약 100,210 제곱킬로미터입니다.'}


# 배치에서의 병렬처리 테스트
def runnable_parrel_batch_test():
    model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.1)

    chain1 = (
        PromptTemplate.from_template("{country} 의 수도는 어디야?")
        | model
        | StrOutputParser()
    )

    chain1.batch([{"country": "한국"}, {"country": "미국"}])

    chain2 = (
        PromptTemplate.from_template("{country} 의 면적은 얼마야?")
        | model
        | StrOutputParser()
    )

    chain2.batch([{"country": "한국"}, {"country": "미국"}])

    combined = RunnableParallel(capital=chain1, area=chain2)

    answer = combined.batch([{"country": "한국"}, {"country": "미국"}])

    print(answer)


def runnable_passthrough_test():
    model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.1)
    chain1 = (
        {"country": RunnablePassthrough()}
        | PromptTemplate.from_template("{country} 의 수도는?")
        | model
        | StrOutputParser()
    )

    answer = chain1.invoke("한국")
    print(answer)


def runnable_lambda_test():
    prompt = PromptTemplate.from_template(
        "{today} 가 생일인 유명인 {n} 명을 나열하세요. 생년월일을 표기해 주세요."
    )
    llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0.1)

    chain = (
        {"today": RunnableLambda(get_today), "n": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    answer = chain.invoke(3)

    print(answer)


def get_today(a):
    return datetime.now().strftime("%Y-%m-%d")


if __name__ == "__main__":
    load_dotenv()
    runnable_lambda_test()
