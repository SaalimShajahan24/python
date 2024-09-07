class sem3:
   def __init__(self,name):
     self.name=name
   def duties(self):
      print('Attendance')

def display_representative_details(rep):
    print(f"Name: {rep.name}")
    rep.duties()

clrep=sem3("Sivanand")
plrep=sem3("Merin")

display_representative_details(clrep)
display_representative_details(plrep)