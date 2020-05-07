# Import CSV file to Mongodb

Given a CSV file (delimited by tabulates) it imports the data to a Mongodb collection. File requires a first line with header.

## Arguments

| Parameter      | Type                        | Description                                  | Required | Default value   |
|----------------|-----------------------------|----------------------------------------------|----------|-----------------|
| --help (or -h) | Show help message and exit. |                                              |          |                 |
| --inputfolder  | String                      | Input folder name.                           | True     |                 |
| --mongoclient  | String                      | Mongo client name (i.e: 'localhost:27017/'). | True     | localhost:27017 |
| --mongodb      | String                      | Mongo database name (i.e: 'mydatabase').     | True     | mydatabase      |
| --mongocol     | String                      | Mongo collection name (i.e: 'myitems').      | True     | myitems         |

## Example

### Call

>py main.py --inputfolder example/ --mongoclient localhost:27017 --mongodb mydatabase --mongocol myitems

## MongoDB Docker

>docker container run -d -p 27017:27017 mongo

## Next steps

- Add possibility to indicate CSV delimiter by call parameter.
