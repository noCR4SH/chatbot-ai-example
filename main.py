from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import DirectoryLoader
from langchain.chat_models import ChatOpenAI
import gradio as gr
import constants
import os

# Set OpenAI API Key to environment variable
os.environ["OPENAI_API_KEY"] = constants.APIKEY

#Initialize LLM
llm = ChatOpenAI(temperature=0.6, model_name="gpt-3.5-turbo")

#initialize documents loader. You can add multiple loaders for different file formats
pdf_loader = DirectoryLoader("data/pdf/", glob="*.pdf")

#add loaders to documents list
loaders = [pdf_loader]
documents = []
for loader in loaders:
    documents.extend(loader.load())

print("Loaded " + str(len(documents)) + " documents")

# Split content from loaded documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
documents = text_splitter.split_documents(documents)

print("Split into " + str(len(documents)) + " chunks")

#Initialize OpenAI Embeddings. OpenAI’s text embeddings measure the relatedness of text strings.
#An embedding is a vector (list) of floating point numbers. The distance between two vectors measures their relatedness. Small distances suggest high relatedness and large distances suggest low relatedness.
embeddings = OpenAIEmbeddings()
#Initialize vector database
vectorstore = Chroma.from_documents(documents, embeddings)

#Initialize Conversational Retrieval Chain
qa = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vectorstore.as_retriever(), return_source_documents=True, verbose=True)

#Initialize chat history
# chat_history = []
def chatbot(query, chat_history):
    # Convert chat history to list of tuples
    chat_history_tuples = []
    for message in chat_history:
        chat_history_tuples.append((message[0], message[1]))

    # Get result from QA Chain
    result = qa({"question": query, "chat_history": chat_history_tuples})

    return result["answer"]

# Initialize Gradio Chat Interface
chat = gr.ChatInterface(
    fn=chatbot,
    title="Future Collars AI",
    description="Ask a question about Future Collars",
    undo_btn=None
)

# Launch the app. Set share to True if you want to share your app publicly
chat.launch(share=False)