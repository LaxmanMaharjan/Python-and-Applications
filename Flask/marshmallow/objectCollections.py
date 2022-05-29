from user import User, UserSchema

user1 = User("laxman","laxman@python.org")
user2 = User("laxmi","laxmi@python.org")
users = [user1,user2]

serialized_data = UserSchema(many=True).dump(users)
print(serialized_data,type(serialized_data))

for data in serialized_data:
    print(type(data))
