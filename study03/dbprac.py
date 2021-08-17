from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert / find / update / delete

# insert  - 저장
doc = {'name':'smith','age':30}
db.users.insert_one(doc)

# find  - 찾기(id값을 제외)
#same_ages = list(db.users.find({'age':21},{'_id':False}))
#for person in same_ages:
#    print(person)

# find_one  - 한개 찾기
#user = db.users.find_one({'name':'bobby'})
#print(user['age'])

# update  -  수정
#db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# update_many  - 다중 수정
#db.users.update_many({'name':'bobby'},{'$set':{'age':19}})


# delete - 삭제
#db.users.delete_one({'name':'bobby'})

# delete - 다중 삭제
#db.users.delete_many({'name':'bobby'})



