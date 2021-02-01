class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "사용자 {} 나이 {}".format(self.name,self.age)

user1 = User("백재원",24)

print(user1)
