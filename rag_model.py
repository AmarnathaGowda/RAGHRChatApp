#Import OS, Document Loader, Text Splitter, Bedrock Embeddings, Vector DB, VectorStoreIndex, Bedrock-LLM
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.llms.bedrock import Bedrock

#wrap within a function
def hr_index():
    #Define the data source and load data with PDFLoader
    data_load = PyPDFLoader('https://www.upl-ltd.com/images/people/downloads/Leave-Policy-India.pdf')
    # data_test = data_load.load_and_split()
    # print(len(data_test))

    #Split the text based on charater, Token etc - Recursively split by character - ["\n\n", "\n", " ", ""]
    data_split = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=100,chunk_overlap=10)

    #Create Embedding - Clint connect
    data_embeddings = BedrockEmbeddings(
        credentials_profile_name='default',
        model_id='amazon.titan-embed-text-v1'
    )

    #Create Vector DB, Store Embeddings and Index for Search - VectorstoreIndexCreator
    data_index = VectorstoreIndexCreator(
        text_splitter=data_split,
        embedding=data_embeddings,
        vectorstore_cls=FAISS
    )

    #Create index for HR Policy Document
    db_index = data_index.from_loaders([data_load])

    return db_index



#Write a function to connect to Bedrock Foundation Model
def hr_llm():
    llm = Bedrock(
        credentials_profile_name='default',
        model_id='anthropic.claude-v2',
        model_kwargs={
        "max_tokens_to_sample":3000,
        "temperature": 0.1,
        "top_p": 0.9}
    )
    return llm


#Write a function which searchs the user prompt, searches the best match from Vector DB and sends both to LLM
def hr_rag_response(index,question):
    rag_llm=hr_llm()
    hr_rag_query=index.query(question=question,llm=rag_llm)
    return hr_rag_query