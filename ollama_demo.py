from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate

llm = Ollama(model="llama2:chat")

prompt = PromptTemplate.from_template("""you are a terse and grumpy cartographer. You insult people who ask obvious questions but still always answer."

Answer the following question:

Question: {question}
""")

output = (prompt | llm).stream({"question": "where is paris?"})
for chunk in output:
    print(chunk, flush=True, end="")