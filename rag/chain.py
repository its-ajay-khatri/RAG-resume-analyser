from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama
from prompts.role_prompt import prompt_template


def generate_response(query, docs):

    llm = Ollama(model="llama3.2:3b")

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context"]
    )

    final_prompt = prompt.format(context=context)

    response = llm.invoke(final_prompt)

    return response