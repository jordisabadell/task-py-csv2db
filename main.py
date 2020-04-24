import os
import pymongo
from readfile import readFile

inputDir = 'in/'

#insert items to database
myclient = pymongo.MongoClient("mongodb://localhost:32769/")
mydb = myclient["mydatabase"]
mycol = mydb["items"]

# 1) iterate CSV files
# 2) convert data files to array of dictionaries
# 3) insert items of array into database
files = os.listdir(inputDir) #https://docs.python.org/3.8/library/os.html?highlight=listdir#os.listdir
for file in files:
    if file.endswith('.csv'):
        items = readFile(inputDir + file)
        mycol.insert_many(items)
