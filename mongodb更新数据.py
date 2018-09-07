from pymongo import MongoClient
conn=MongoClient('localhost',27017)
db=conn.whd
collection=db.per
# collection.update({'name':'lucy'},{'$set':{'age':50}})
# collection.update({'name':'lucy'},{'$set':{'age':60}})
collection.update({'age':20},{'$set':{'name':'hhh'}},upsert=True)
collection.update({'age':20},{'$set':{'name':'kkk'}},multi=True)
conn.close()