class User:
    def __init__(self,name,email,id):
        self.name=name
        self.email=email
        self.id=id

    def __str__(self):
        return f"user(name = {self.name},email = {self.email}, id = {self.id})"

git_user = User("priya" , "jayapriyatalabattula14" , 1)
print(git_user)