from database import db, connect
connect()

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    age = db.IntField()

    def __repr__(self):
        return f"<User: {self.username}>"

    def toJson(self):
        return {
                "id":self.id,
                "username":self.username,
                "age":self.age
                }

class Comment(db.EmbeddedDocument):
    content = db.StringField(required=True)
    
    def __repr__(self):
        return f"<Comment: {self.content}>"

    def toJson(self):
        return {
                "id":self.id,
                "content":self.content
                }

class Post1(db.Document):
    title = db.StringField(required=True, unique=True)
    content = db.StringField(required=True)
    user = db.ReferenceField(User)
    comments = db.ListField(db.EmbeddedDocumentField(Comment))

    def __repr__(self):
        return f"<Post: {self.title}>"

    def toJson(self):
        return {
                "id":self.id,
                "title":self.title,
                "content":self.content,
                "user":self.user,
                "comments":self.comments
                }

# user = User(username="LaxmanMaharjan", age=23)
# user.save()
comment = Comment(content="great one")
user = User.objects.all()[0]
post = Post1(title="The Batman", content="I'm Vengeance.",user=user,comments=[comment])
post.save()

