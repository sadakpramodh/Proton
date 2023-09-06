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
        



    

