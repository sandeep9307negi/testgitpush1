import pymongo

client = pymongo.MongoClient("mongodb+srv://sandeep:Mech0422@cluster0.pstrh.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name":"Himanshu",
    "email":"dhf243.5456@gmail.com",
    "surname":"Nautiyal"
}

db1=client['mongodb_revisio']
coll=db1['test']
coll.insert_one(d)
