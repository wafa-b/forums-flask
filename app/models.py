import datetime
class Member:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.id = 0
        self.posts = []


    def __str__(self):
        return  "Name: " + self.name + "\n" +"Age: " + str(self.age)

class Post:
    def __init__(self,title,contente,member_id=0):
        self.title = title
        self.contente = contente
        self.id = 0
        self.member_id = member_id
        self.date = datetime.datetime.now()

    def __str__(self):
        return "Title: " +self.title + "\n"+ "Contente: "+ self.contente + "\n" + str(self.date)
