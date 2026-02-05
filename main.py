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
            font=("Arial", 14),
            relief="ridge",
            width=30,
            height=6
        )
        self.label.pack(expand=True, padx=10)

        self.label.drop_target_register(DND_FILES)
        self.label.dnd_bind("<<Drop>>", self.drop)

        self.copy_button = tk.Button(self, text="Copy ",font=("Arial", 20), height=3, width=10, command=self.copy_to_clipboard)

    def copy_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(FinalText)
        self.update()
        self.copy_button.config(text="Copied")

    def drop(self, event):
        global FinalText
        FinalText = ""
        self.copy_button.config(text="Copy")

        file_path = event.data.strip("{}")

        if not file_path.lower().endswith(".pdf"):
            messagebox.showerror("Error", "Only PDF files are allowed.")
            return

        reader = PdfReader(file_path)
        lastPage = False
        for pageNum in range(len(reader.pages)):
            page = reader.pages[pageNum]
            if lastPage:
                break
            if "100. " in page.extract_text():
                lastPage = True
            
            if pageNum == 0:
                pass
            else:
                toRemove = ["Copyright ©", "Test "]
                page_text = "\n".join(
                    line for line in page.extract_text().splitlines()
                    if not any(p in line for p in toRemove)
                )

                FinalText += page_text

        file_name = os.path.basename(file_path)
        self.label.config(text=file_name)
        self.copy_button.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
