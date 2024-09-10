import json
db = {'UserList':[{'UserID':1234,'Name':'hogehoge'},{'UserID':5678,'Name':'yumyum'}]}
list = db['UserList']
db = json.dumps(db)
user = {}
userList = []
for k in list:
    UserID = str(k['UserID'])
    Name = str(k['Name'].encode('utf-8'))
    user['id'] = UserID
    user['name'] = Name
    data = json.dumps(user)
    userList.append(data)
print(db)
print(userList)
