import chainlit as cl
import Readers.read_documents as reader

def store_files(file):
    # Save the file in temp location
    file_path = f"tmp\{file.name}"
    with open(file_path, "wb") as f:
        f.write(file.content)
        f.close()
        # print(file_path)
        # print(file.name)
        # print(file.content)
    return file_path

def select_reader(file_path):
    # load the pdf from the temp location and process the contents
    # load the pdf from the temp location and process the contents
    mime_type = reader.guess_type(file_path)
    if mime_type == "application/pdf":
        check_password = reader.PDFReader.check_password(file_path)
        if check_password:
            return "currently we are not supporting the password protected file :("
        else:
            return reader.PDFReader(file_path)
        
    if mime_type == "image/jpeg" or mime_type == "image/png":
            


            
loader = PyPDFLoader(file_path)

# Split the text into chunks
# texts = text_splitter.split_text(text)


pages = loader.load_and_split(text_splitter=text_splitter)

# Create a metadata for each chunk

metadatas = [{"source": f"{page.metadata['page']}-pl"} for page in pages]
texts = [page.page_content for page in pages]


# Create a Chroma vector store

embeddings = OpenAIEmbeddings()
docsearch = await cl.make_async(Chroma.from_texts)(
    texts, embeddings, metadatas=metadatas
)
# Create a chain that uses the Chroma vector store
chain = RetrievalQAWithSourcesChain.from_chain_type(
    ChatOpenAI(temperature=0, streaming=True),
    chain_type="stuff",
    retriever=docsearch.as_retriever(),
)

# Save the metadata and texts in the user session
cl.user_session.set("metadatas", metadatas)
cl.user_session.set("texts", texts)

# Let the user know that the system is ready
msg.content = f"Processing `{file.name}` done. You can now ask questions!"
await msg.update()

cl.user_session.set("chain", chain)
