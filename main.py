import os
import shutil
import tkinter as tk
from tkinter import messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from pypdf import PdfReader

oldFirstPage = "Business Management and Administration Cluster Exam INSTRUCTIONS:  This is a timed, comprehensive exam for the occupational area identified above.  Do not open this booklet until instructed to do so by the testing monitor.  You will have _____ minutes to complete all questions. CAUTION:  Posting these materials on a website is a copyright violation. This comprehensive exam was developed by the MBAResearch Center exclusively for DECA’s 2016-2017 Competitive Events Program. Items have been randomly selected from the MBAResearch Test-Item Bank and represent a variety of instructional areas.  Performance indicators for this exam are at the prerequisite, career-sustaining, and specialist levels. A descriptive test key, including question sources and answer rationale, has been provided the DECA chartered association advisor.   Copyright © 2017 by Marketing & Business Administration Research and Curriculum Center®, Columbus, Ohio (dba MBAResearch). Each individual test item contained herein is the exclusive property of MBAResearch. Items are licensed to DECA only for use as configured within this exam, in its entirety. Use of individual items for any purpose other than as specifically authorized is prohibited. Possession of this exam, without written authorization, under any other circumstances is a copyright violation. Posting to inter- or intranet sites is specifically forbidden unless written permission is obtained prior to posting. Report violations to DECA at 703.860.5000 and MBAResearch at 800.448.0398. Permission for reprinting is granted to DECA chartered associations authorized by DECA Inc. DECA Inc. will impose sanctions on chapters and chartered associations for violations of this policy up to and including disqualification of competitors and chapters from further participation. Competency-Based Competitive Events *Written Exam*for District/Regional Use Test Number 1144 Booklet Number _____ "
newFirstPage = "SAMPLE  EXAMBUSINESS MANAGEMENT +  ADMINISTRATION CAREER CLUSTERTHE BUSINESS MANAGEMENT + ADMINISTRATION CAREER CLUSTER EXAM IS USED FOR THE FOLLOWING EVENTS:BUSINESS LAW AND ETHICS TEAM DECISION MAKING BL TDMHUMAN RESOURCES MANAGEMENT SERIES HRMThese test questions were developed by the MBA Research Center. Items have been randomly selected from the MBA Research Center’sTest-Item Bank and represent a variety of instructional areas. Performance indicators for these test questions are at the prerequisite, career-sustaining, and specialist levels. A descriptive test key, including question sources and answer rationale, has been provided.Copyright © 2019 by MBA Research and Curriculum Center®, Columbus, Ohio. Each individual test item contained herein is the exclusive propertyof MBA Research Center. Items are licensed only for use as conﬁgured within this exam, in its entirety. Use of individual items for any purposeother than as speciﬁcally authorized in writing by MBA Research Center is prohibited.Posted online March 2019 by DECA Inc."

class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        self.title("DECA Test Reader")
        self.geometry("400x200")
        self.resizable(False, False)

        self.label = tk.Label(
            self,
            text="Drag Test PDF Here",
            font=("Arial", 14),
            relief="ridge",
            width=30,
            height=6
        )
        self.label.pack(expand=True, padx=10, pady=10)

        self.label.drop_target_register(DND_FILES)
        self.label.dnd_bind("<<Drop>>", self.drop)

    def drop(self, event):
        file_path = event.data.strip("{}")
        reader = PdfReader(file_path)
        
        RawText = ""
        for pageNum in range(len(reader.pages)):
            page = reader.pages[pageNum]
            RawText += page.extract_text()
            
        for char in RawText:
            if char != "1":
                char = char.replace(char, "", 1)
            else:
                break
            
        if (reader.pages[0]).extract_text() == newFirstPage:
            print("fsdklfj")
        else:
            print('sad')

        if not file_path.lower().endswith(".pdf"):
            messagebox.showerror("Error", "Only PDF files are allowed.")
            return

if __name__ == "__main__":
    app = App()
    app.mainloop()