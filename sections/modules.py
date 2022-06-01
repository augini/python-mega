import os
import pandas
import time

while True:
   if os.path.exists("./files/temps_today.csv"):
      data = pandas.read_csv("./files/temps_today.csv")
      print(data.mean()["st2"])
   else:
      print("File does not exist. Sucker")
   time.sleep(10)