import chromadb
import uuid
from app.services.embedding_service import EmbeddingService


class VectorService:

    client = chromadb.PersistentClient(
        path="data/chroma"
    )

    collection = client.get_or_create_collection(
        name="documents"
    )


    @staticmethod
    def search(query, top_k=3):

        query_embedding = EmbeddingService.create_embeddings(
            [query]
        )[0]


        results = VectorService.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )


        docs = results["documents"][0]
        metas = results["metadatas"][0] if results.get("metadatas") else [{}] * len(docs)
        
        return [{"content": d, "metadata": m} for d, m in zip(docs, metas)]


    @staticmethod
    def add_documents(chunks):

        texts = [
            chunk.page_content
            for chunk in chunks
        ]
        
        metadatas = [
            chunk.metadata
            for chunk in chunks
        ]

        embeddings = EmbeddingService.create_embeddings(
            texts
        )


        ids = [
            str(uuid.uuid4())
            for _ in range(len(texts))
        ]


        VectorService.collection.add(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )


        print(
            f"Added {len(texts)} chunks to ChromaDB"
        )