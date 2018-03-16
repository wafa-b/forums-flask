import datetime
class Member:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.id = 0
        self.posts = []


    def __str__(self):
        return  "Name: " + self.name + "\n" +"Age: " + str(self.age)

    def __dict__(self):
        return {
            "id":self.id,
            "name":self.name,
            "age":self.age,
            "posts":self.posts,

    }

class Post:
    def __init__(self,title,content,member_id=0):
        self.title = title
        self.content = content
        self.id = 0
        self.member_id = member_id
        self.date = datetime.datetime.now()

    def __str__(self):
         return "Title: " +self.title + "\n"+ "Contente: "+ self.content + "\n" + str(self.date)

    def __dict__(self):
        return {
            "id":self.id,
            "title":self.title,
            "content":self.content,
            "member_id":self.member_id,
        }
