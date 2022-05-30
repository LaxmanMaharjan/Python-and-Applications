from database import connect,db
connect()

class Post(db.Document):
    title = db.StringField(required=True, unique=True)
    content = db.StringField(required=True)

    def __repr__(self):
        return f"<Post: {self.title}>"

    def toJson(self):
        return {
                "id":self.id,
                "title":self.title,
                "content":self.content
                }

# creating object in collection
# post = Post(title="The Batman",content="They think i'm hiding in the shadows but i'm the shadows.")
# post.save()

# post1 = Post(title="Jon Snow",content="King in the North.")
# post1.save()

# Read
posts = Post.objects.all()
print(posts)
# print(posts[0].toJson())
# print(Post.objects.count())

# Update 
# post = Post.objects(title__icontains="batman").first()
# print(post.toJson())
# post.update(title="The batman")
# print(post.toJson())
# post = Post.objects(title__icontains="batman").first().update(title='The Batman')

# Delete
# post = Post.objects(title__icontains="batman").first()
# post.delete()
