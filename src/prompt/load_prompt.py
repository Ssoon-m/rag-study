from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

def load_prompt_test():
    prompt = load_prompt("src/prompt/prompts/capital.yaml") 
    model = ChatOpenAI(model="gpt-4o", temperature=0.1)
    chain = prompt | model | StrOutputParser()


    answer = chain.stream({"country": "한국"})
    for chunk in answer:
        print(chunk, end="", flush=True)

if __name__ == "__main__":
    load_prompt_test()
