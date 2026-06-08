class ContextBuilder:

    def build(self,retrieval):

        context = ""

        for _, row in retrieval:
            context+=(
                f"{row['surah_name']} "
                f"{row['verse_no']} "
                f"{row['verse_text']}\n"
            ) 

        return context