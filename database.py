from pypdf import PdfReader
import os
base_dir = os.getcwd()
folder_path = os.path.join(base_dir, "data")

"""
Create initializer functions for each type of file
Search files for a specified term, and return relative information
"""
class database:
    def __init__(self):
        self.files = os.listdir(folder_path)
        self.fp = os.path.join(folder_path, self.files[0])
        self.reader = PdfReader(self.fp)
        print(len(self.reader.pages))
        self.page = self.reader.pages[142]
        print(self.page.extract_text())
    
db = database()