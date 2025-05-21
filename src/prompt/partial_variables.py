from datetime import datetime
from langchain_core.prompts import PromptTemplate

datetime.now().strftime("%B %d")

def get_today():
    return datetime.now().strftime("%B %d")

def partial_variables_test():
    prompt = PromptTemplate(
        template="오늘의 날짜는 {today} 입니다. 오늘이 생일인 유명인 {n}명을 나열해 주세요. 생년월일을 표기해주세요.",
        input_variables=["n"],
        partial_variables={
            "today": get_today  # dictionary 형태로 partial_variables를 전달
        },
    )


    print(prompt.invoke({"n": 10}))
    # text='오늘의 날짜는 May 21 입니다. 오늘이 생일인 유명인 10명을 나열해 주세요. 생년월일을 표기해주세요.'
    # print(prompt.invoke({"today": "Jan 02", "n": 3}))
    # partial_variables의 today에 값을 직접 넣어주면 직접 넣어준 값이 나옴
    # text='오늘의 날짜는 Jan 02 입니다. 오늘이 생일인 유명인 3명을 나열해 주세요. 생년월일을 표기해주세요.'

if __name__ == "__main__":
    partial_variables_test()
