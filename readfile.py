import os

def readFile(fileName):
    """
    First line as a header. All lines have same number of items. 

    @param fileName: str
    @return []
    """

    #read file
    file = open(fileName, "r", encoding='utf8') #https://docs.python.org/3.8/library/functions.html#open

    #get header from first line
    header = file.readline().replace("\n", "").split("\t")

    #iterate lines
    items = []
    for i, line in enumerate(file):
        if i>0:
            if line:
                #convert line to dictionary
                item = {}
                values = line.replace("\n", "").split("\t")
                for i, value in enumerate(values):
                    item[header[i]] = value
                
                items.append(item)
    
    return items