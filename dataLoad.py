from pptx import Presentation
import threading
import pymupdf
import os

base_dir = os.getcwd()
class loadData:
    def getPresText(self, file_path):
        prs = Presentation(file_path)
        text = []

        for slide in prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    text.append(shape.text)

        return "\n".join(text)

    def getPDFtxt(self, file_path):
        doc = pymupdf.open(file_path)
        allText = ""
        for page in doc:
            allText += page.get_text()
        return allText
    
    def loadPowerP(self):
        ls = os.listdir("data/ppSlides")
        ppText = [] 
        for file in ls:
            fp = os.path.join(base_dir, 'data/ppSlides', file)
            txt = self.getPresText(fp)
            ppText.append({"File": file, "Content": txt})
        return ppText
    
    def loadPDF(self):
        ls = os.listdir("data/studyGuides")
        pdftxt = []
        for file in ls:
            print("File:", file)
            fp = os.path.join(base_dir, 'data/studyGuides', file)
            txt = self.getPDFtxt(fp)
            pdftxt.append({"File": file, "Content": txt})
        return pdftxt

    def loadAll(self):
        results = [None, None]
        
        threads = [
            threading.Thread(
                target=lambda: results.__setitem__(0, self.loadPowerP())
            ),
            threading.Thread(
                target=lambda: results.__setitem__(1, self.loadPDF())
            )
        ]
        
        # Start all threads
        for t in threads:
            t.start()

        # Wait for all to finish
        for t in threads:
            t.join()
            
        ppt = results[0]
        pdf = results[1]
        
        return ppt, pdf
        
ld = loadData()
data = ld.loadAll()



# print(p.getPDFtxt("data/studyGuides/ISP152 Study Guide 2025.pdf"))




# print(extract_text_from_pptx("data/ppSlides/ISP152 - Topic 1 slides.pptx"))