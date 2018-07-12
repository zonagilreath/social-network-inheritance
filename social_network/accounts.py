
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.following = []
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def get_timeline(self):
        unordered_timeline =  [post for user in self.following for post in user.posts]
        return sorted(unordered_timeline, key=lambda x: x.timestamp, reverse=True)
        

    def follow(self, other):
        self.following.append(other)
