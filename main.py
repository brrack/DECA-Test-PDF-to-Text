import tkinter as tk
from tkinter import messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from pypdf import PdfReader
import os

FinalText = ""

class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        self.title("DECA Test Reader")
        self.geometry("400x250")
        self.resizable(False, False)

        self.label = tk.Label(
            self,
            text="Drag Test PDF Here",
            font=("Arial", 18),
            relief="ridge",
            width=30,
            height=6
        )
        self.label.pack(expand=True, padx=10)

        self.label.drop_target_register(DND_FILES)
        self.label.dnd_bind("<<Drop>>", self.drop)

        self.copy_button = tk.Button(self, text="Copy Questions",font=("Arial", 23), height=3, width=13, command=lambda:self.copy_to_clipboard(FinalText, "questions"))
        self.copy_answers_button = tk.Button(self, text="Copy Answers ",font=("Arial", 23), height=3, width=13, command=lambda:self.copy_to_clipboard(AnswersText, "answers"))

    def copy_to_clipboard(self, copytext, type):
        self.clipboard_clear()
        self.clipboard_append(copytext)
        self.update()
        if type == "questions":
            self.copy_button.config(text="Copied Questions")
            self.copy_answers_button.config(text="Copy Answers")
        elif type == "answers":
            self.copy_answers_button.config(text="Copied Answers")
            self.copy_button.config(text="Copy Questions")

    def drop(self, event):
        global FinalText
        FinalText = ""
        global AnswersText
        AnswersText = ""
        self.copy_button.config(text="Copy Questions")
        self.copy_answers_button.config(text="Copy Answers")

        file_path = event.data.strip("{}")

        if not file_path.lower().endswith(".pdf"):
            messagebox.showerror("Error", "Only PDF files are allowed.")
            return

        reader = PdfReader(file_path)
        lastPage = False
        skipPage = False
        toRemove = ["Copyright ©", "Test "]
        for pageNum in range(len(reader.pages)):        #GET ANSWERS
            page = reader.pages[pageNum]
            if lastPage:
                if "1. " not in page.extract_text() and skipPage:
                    skipPage = False
                    pass
                else:
                    answers_text = "\n".join(
                        line for line in page.extract_text().splitlines()
                        if not any(p in line for p in toRemove))
                    AnswersText += answers_text
            else:
                if "100. " in page.extract_text():
                    lastPage = True
                    skipPage = True
            
                if pageNum == 0:
                    pass
                else:
                    page_text = "\n".join(
                        line for line in page.extract_text().splitlines()
                        if not any(p in line for p in toRemove))
                    
                    FinalText += page_text

        file_name = os.path.basename(file_path)
        self.label.config(text=file_name)
        self.copy_button.pack(side=tk.LEFT, pady=5)
        self.copy_answers_button.pack(side=tk.RIGHT)

if __name__ == "__main__":
    app = App()
    app.mainloop()