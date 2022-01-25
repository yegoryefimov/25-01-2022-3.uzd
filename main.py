text = input ("Ievadi tekstu: ")
def deleteCombo(text): #deklerējam funkciju, argumentu - text
  if text.count ("abc")>0: #pārbaudām vai ir kaut viena kombo "abc"
   text = text.replace("abc", "") #aizvietojam "abc" ar ""
  else: #pretējā gadījumā
    text = "Meklējamā kombinācija netika atrasta!" #aizvietojam tekstu ar paziņojumu
  return text #aizgriežam vērtību text