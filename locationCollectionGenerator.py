import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["location"]
mycol = mydb["location"]

for x in range(500000):
    mydict = { 
        "timestamp" : random_date("1/1/2019 1:30 PM", "5/10/2020 4:50 AM", random.random()),
        "tag_id" : random.randint(1, 30),
        "net_id" : random.randint(1, 6),
        "zone_id" : random.randint(1, 3),
        "x" : random.randint(-100, 100),
        "y" : random.randint(-100, 100),
        "z" : random.randint(0, 90),
        "quality" : random.randint(1, 3)
  
      }


    x = mycol.insert_one(mydict)