import os
from langchain import OpenAI, ConversationChain

os.environ["OPENAI_API_KEY"] = "sk-"


llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

conversation.predict(input="Hi there!")
conversation.predict(input="I'm doing well! Just having a conversation with an AI.")
conversation.predict(input="tell me about embedding")
conversation.predict(input="tell me more")