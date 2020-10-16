import pymongo
import random
import time

def str_time_prop(start, end, format, prop):
    
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["location"]
mycol = mydb["location"]


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["location"]
mycol = mydb["locationWalk"]

for y in range(10000):
    date = random_date("1/1/2019 1:30 PM", "5/10/2020 4:50 AM", random.random())

    for x in range(20):
        mydict = { 
            "timestamp" : date,
            "tag_id1" : random.randint(1, 30),
            "tag_id2" : random.randint(31, 60),
            "distance" : random.randint(0, 100),
            "quality" : random.randint(1, 3)

          }


        x = mycol.insert_one(mydict)