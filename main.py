import os
import pymongo
import argparse
from readfile import readFile

#ARGUMENTS
parser = argparse.ArgumentParser(description='Given a CSV file (delimited by tabulates) it imports the data to a Mongodb collection. File requires a first line with header.')
parser.add_argument('--inputfolder', dest='input_folder', 
    help='Input folder name.', type=str, required=True)
parser.add_argument('--mongoclient', dest='mongo_client', 
    help='Mongo client name (like \'localhost:32769/\').', type=str, required=True)
parser.add_argument('--mongodb', dest='mongo_db', 
    help='Mongo database name (like \'mydatabase\').', type=str, required=True)
parser.add_argument('--mongocol', dest='mongo_col', 
    help='Mongo collection name (like \'items\').', type=str, required=True)

args = parser.parse_args()
inputFolderName = args.input_folder
mongoClient = args.mongo_client
mongoDb = args.mongo_db
mongoCol = args.mongo_col

#insert items to database
myclient = pymongo.MongoClient("mongodb://" + mongoClient)
mydb = myclient[mongoDb]
mycol = mydb[mongoCol]

# 1) iterate CSV files
# 2) convert data files to array of dictionaries
# 3) insert items of array into database
files = os.listdir(inputFolderName) #https://docs.python.org/3.8/library/os.html?highlight=listdir#os.listdir
for file in files:
    if file.endswith('.csv'):
        items = readFile(inputFolderName + file)
        mycol.insert_many(items)

print("Done.")