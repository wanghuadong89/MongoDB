from pymongo import MongoClient
conn=MongoClient('localhost',27017)
db=conn.whd
collection=db.per
# collection.remove({'name':'kkk'})
collection.remove({'age':20})
conn.close()