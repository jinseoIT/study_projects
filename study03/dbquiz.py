from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# db - 매트릭스 평점 가져오기
movieInfo = db.movies.find_one({'title':'매트릭스'},{'_id':False})
m_star = movieInfo['star']
print(m_star)

# db - 매트릭의 평점과 같은 평점의 영화 제목들을 가져오기
movieList = list(db.movies.find({'star': m_star }, {'_id':False}))

for moive in movieList:
    print(moive['title'])

# db - 매트릭스 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})


