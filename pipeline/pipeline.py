import sys
import pandas as pd

month = int(sys.argv[1])


df = pd.DataFrame({"A":[1,2],"B":[3,4]})
print(df)

print("arguments", sys.argv)
print(f"hello pipeline, month {month}")