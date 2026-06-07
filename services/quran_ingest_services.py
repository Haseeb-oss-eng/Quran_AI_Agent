
class QuranIngestService:
    def __init__(self,database_repo:class,file:class,embedding:class)
    self.repo = database_repo
    self.df_data = self.file.read_file()
    self.embedding_df = embedding.embedding_encode(self.df_data)
    self.repo.insert_data(self.embedding_df)
    self.is_successful = self.repo.table_length > 0