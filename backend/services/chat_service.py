from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from backend.ai.llm import llm
from backend.ai.memory import get_session_history

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm

chat_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

def ask_ai(message: str, session_id="default"):
    response = chat_with_memory.invoke(
        {"input": message},
        config={"configurable": {"session_id": session_id}}
    )
    return response.content