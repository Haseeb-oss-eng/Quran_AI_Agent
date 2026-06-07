class QuranIngestService:

    def __init__(
        self,
        repository,
        reader,
        embedder
    ):
        self.repository = repository
        self.reader = reader
        self.embedder = embedder

    def ingest(self):

        df = self.reader.read_file()

        df["embedding"] = self.embedder.encode_batch(
            df["Arabic Text"].tolist()
        )

        self.repository.insert_data(df)

        return self.repository.table_length > 0