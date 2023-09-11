import chainlit as cl
import config
import Flows.InitFlowManager as IFM

@cl.on_chat_start
async def init():
    files = None
    # Wait for the user to upload a file
    while files == None:
        files = await cl.AskFileMessage(
            content="Please upload a PDF, Word, Excel, or CSV file to begin!", \
            accept=config.ACCEPTED_MIME_TYPES,  \
            max_size_mb=config.MAX_SIZE_MB, \
            max_files=config.MAX_FILES
        ).send()

    for file in files:
        msg = cl.Message(content=f"Processing `{file.name}`...")
        await msg.send()
        file_path = IFM.store_files(file)
        file_reader = IFM.select_reader(file_path)
        # Create a Chroma vector store


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
        



    

