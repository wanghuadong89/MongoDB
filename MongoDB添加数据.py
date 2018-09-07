import pymongo
from pymongo import MongoClient
conn=MongoClient('localhost',27017)
db=conn.whd
collection=db.per
# collection.insert({'name':'lucy','age':20,'sex':0})
collection.insert([{'name':'ll','age':28,'sex':1},{'name':'leilei','age':30,'sex':0}])
conn.close()
