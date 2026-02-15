import pandas as pd

StudentScore = {
"Student" : ["Dido","Anna","Mark"],
"Score" : [80,90,75]
}

ss = pd.DataFrame(StudentScore)
print(ss)
