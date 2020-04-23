import os
import pymongo
from csv2db_readfile import readFile

inputDir = 'in/'

#insert items to database
myclient = pymongo.MongoClient("mongodb://localhost:32768/")
mydb = myclient["mydatabase"]
mycol = mydb["items"]

# 1) iterate CSV files
# 2) convert data to array of dictionaries
# 3) insert into database
files = os.listdir(inputDir) #https://docs.python.org/3.8/library/os.html?highlight=listdir#os.listdir
for file in files:
    if file.endswith('.csv'):
        items = readFile(inputDir + file)

        for item in items:
            mycol.insert_one(item)