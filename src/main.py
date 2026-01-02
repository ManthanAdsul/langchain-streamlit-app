from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0.7)

prompt = PromptTemplate(
    input_variables=["context", "gender"],
    template=(
        "Suggest five cool Indian baby names for a {gender} {context}."
    )
)

chain = prompt | llm | StrOutputParser()

def generate_names(context: str, gender: str) -> str:
    return chain.invoke({
        "context": context,
        "gender": gender
    })

if __name__ == "__main__":
    print(generate_names("new born baby", "boy"))
