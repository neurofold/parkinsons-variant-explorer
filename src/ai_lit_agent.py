from Bio import Entrez
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

Entrez.email = "your_email@example.com"

def fetch_pubmed_abstracts(query, max_results=3):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    ids = record["IdList"]

    abstracts = []
    for pubmed_id in ids:
        summary = Entrez.efetch(db="pubmed", id=pubmed_id, rettype="abstract", retmode="text")
        text = summary.read()
        abstracts.append(text)
    return abstracts

def summarize_with_llm(abstracts, query):
    chat = ChatOpenAI(temperature=0.4)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a biomedical research assistant."),
        ("human", f"Summarize these abstracts related to {query} and Parkinson's disease:\n\n{''.join(abstracts)}")
    ])
    return chat(prompt.format())

