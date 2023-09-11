import os

class TextSplitter:
    def __init__(self, text):
        self.text = text
        self.metadata = {}

    def context_aware_split(self):
        pages = loader.load_and_split(text_splitter=text_splitter)
        # Create a metadata for each chunk

        metadatas = [{"source": f"{page.metadata['page']}-pl"} for page in pages]
        texts = [page.page_content for page in pages]

        return [metadatas, texts]
    




