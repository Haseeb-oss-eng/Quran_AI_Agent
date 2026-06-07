import pandas as pd
import os

class QuranReader:
    def __init__(self):
        self.data = "data/processed/quran_structured_.csv"

    def read_file(self):
           return pd.read_csv(self.data) 
