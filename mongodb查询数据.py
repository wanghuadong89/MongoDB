
from pymongo import MongoClient
from bson.objectid import ObjectId

import pymongo

conn=MongoClient('localhost',27017)
db=conn.whd
collection=db.per
# data=collection.find()
# print(data)
# for i in data:
#     print(i)
# data=collection.find({'name':'leilei'})
# data=collection.find({'age':{'$gt':30}}).count()
# print(data)

# for i in data:
#     print(i)
# data=collection.find().sort('age',pymongo.ASCENDING)
data=collection.find().sort('age',pymongo.DESCENDING)
for i in data:
    print(i)
conn.close()