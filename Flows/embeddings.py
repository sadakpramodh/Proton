
class Embeddings:
    def __init__(self) -> None:
        pass

    def create_embeddings(self, texts):
        embeddings = OpenAIEmbeddings()
        docsearch = await cl.make_async(Chroma.from_texts)(
            texts, embeddings, metadatas=metadatas
        )