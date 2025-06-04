from langchain_community.document_loaders import PyPDFLoader
import pprint
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from langchain_qdrant import QdrantVectorStore
from llm import get_answer

file_path = "./nke-10k-2023.pdf"

loader = PyPDFLoader(file_path=file_path)

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    add_start_index=True
)

all_splits = text_splitter.split_documents(docs)

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# vector_1 = embeddings.embed_query(all_splits[0].page_content)
# vector_2 = embeddings.embed_query(all_splits[1].page_content)

url = os.getenv("QDRANT_URL")
client = QdrantClient(url=url)

if not client.collection_exists("test"):
   client.create_collection(
      collection_name="test",
      vectors_config=VectorParams(size=768, distance=Distance.COSINE)
   )
   
vector_store = QdrantVectorStore(
    client=client,
    collection_name="test",
    embedding=embeddings,
)


# ids = vector_store.add_documents(documents=all_splits)

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 1},
)

user_input = "What's the Nike's end goal?"

results = retriever.batch(
    [
        user_input
    ],
)

context = [doc[0].page_content for doc in results]

get_answer(context, user_input)