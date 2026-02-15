import pandas as pd

Family = {
"Name":["Dido","Douce","Don", "Exau"],
"Age": [23,20,15,13],
"Place":["first","second","tird","Last"],
"School":["IUEA/Uganda", "UNIGOM","Mont Carmel","Chemin de perfection"]
}


#for i in Family:
i = pd.DataFrame(Family)
print(i)

#You can statement bellow to also display Family
#fm = pd.DataFrame(Family)
#print(fm["Name"])
