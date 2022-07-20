import os
import shutil

fro = "D:/Nitish"
to = "D:/Nitish/documents"

niti = os.listdir(fro)
#print(niti)

for img in niti :
    root,ext = os.path.splitext(img)
    if ext == "":
        continue
    
    if ext in [".docx" , ".pdf"]:
        
        path1 = fro + "/" + img
        path2 = to + "/" + img
        
        if os.path.exists(to):
            print("moving")
            shutil.move(path1 , path2)
        else:
            os.mkdir("D:/Nitish/documents")
            shutil.move(path1 , path2)