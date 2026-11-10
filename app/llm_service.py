from langchain_ollama import ChatOllama

def get_llm():
    llm = ChatOllama(model= "llama3.2:latest", temperature =0)
    return llm
if __name__ == "__main__":
    print("Starting the LLM service..", flush = True)
    llm = get_llm()
    print("LLm service started..", flush=True)
    response = llm.invoke("Explain the software testing life cycle.")
    print("\n Response:", flush=True)
    print(response.content,flush=True)
    
    
