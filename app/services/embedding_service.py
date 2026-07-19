from sentence_transformers import SentenceTransformer


class EmbeddingService:

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    @staticmethod
    def create_embeddings(texts):
        """
        Convert text chunks into vector embeddings
        """

        embeddings = EmbeddingService.model.encode(
            texts,
            show_progress_bar=True
        )

        return embeddings.tolist()