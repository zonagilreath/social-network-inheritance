# Rmotrgram

Today we're going to build a clone of a social network (really similar to the blue bird one, but keep it a secret).

As any other social network we're going to have different types of `Post`s. All these different types of Posts should inherit from the parent `Post` class:

* `TextPost`: Just a simple text post. Should be constructed as `TextPost(text="Post Text")`.
* `PicturePost`: A post containing text and the URL of a picture: Should be constructed as `PicturePost(text="Post Text", image_url="imgur.com/OAWTSJu")`.
* `CheckInPost`: A post containing text and coordinates of the user's position. Should be constructed as `CheckInPost(text="Post Text", latitude="40.741895", longitude="-73.989308")`.

Rmotrgram also has users. A user is a simple class that can be created as: `User(first_name="John", last_name="Smith", email="johnsmith@rmotr.com")`. 

## Creating posts

Posts are going to be created and then assigned a user. Once we have our user and post created, we're going to use the `add_post` method from the user class. `add_post` should add the post to the user's list of posts, and assign that user to the post. Example, to create a text post for our user John, we'll do something like:

```python
john = User("John", "Lennon", "john@rmotr.com")
text_post = TextPost("All you need is love!")
text_post.user == None  # Important! Since the post has no user yet, the user attribute should be None.

john.add_post(text_post)

text_post.user == john  # Important!
len(john.posts)
>>> 1
```

As you can see from our previous example, a post is created without a user. It's an "orphan" we might say. By default when a post is created it's user attribute is `None`. But once we add that post to a user using `add_post()`, the post's user attribute should be updated, and the post should be added to the user's list of posts.

## Following users

Users will be able to follow other users. The `follow` method is super simple:

```python
john = User("John", "Lennon", "john@rmotr.com")
paul = User("Paul", "McCartney", "paul@rmotr.com")

john.follow(paul)
print(john.following)
>>> [<User: "Paul McCartney">]
```

## A user's timeline

This should be almost exactly like twitter. A user will have a timeline, that's just a list of posts created by other users that we're following, sorted by datetime (most recent first).

```python
john = User("John", "Lennon", "john@rmotr.com")
paul = User("Paul", "McCartney", "paul@rmotr.com")
george = User("George", "Harrison", "george@rmotr.com")

john.follow(paul)
john.follow(george)

paul.add_post(TextPost("Post 1"))
george.add_post(TextPost("Post 2"))
paul.add_post(TextPost("Post 3"))

print(john.following)
>>>[[<User: "Paul McCartney">], [<User: "George Harrison">]] # John is following Paul and George

print(john.get_timeline())
>>> [<TextPost: Post 3>, <TextPost: Post 2>, <TextPost: Post 1> 
```

**Important**: A user's timeline should only include posts from the users they are following.

## Reading Posts

Finally, one of the most interesting use cases of this project is going to be realted to the "visual representation" of the posts. It's a great example of [Polymorphism](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)). The concept is simple. If I try to print different types of posts, I'm going to get different representations. Example:


```python
john = User("John", "Lennon", "john@rmotr.com")
text_post_1 = TextPost("All you need is love!")
picture_post_2 = PicturePost("Check my new submarine.", image_url='imgur.com/submarine.jpg')
checkin_post_3 = CheckInPost("At Abbey Road Studios", latitude="19.111", longitude="-9.2222")
john.add_post(text_post_1)
john.add_post(picture_post_2)
john.add_post(checkin_post_3)

print(text_post_1)
"""
John Lennon: "All you need is love!"
  Friday, Feb 03, 2017
"""

print(picture_post_2)
"""
John Lennon: "Check my new guitar"
  Pic URL: imgur.com/guitar.png
  Friday, Feb 03, 2017
"""

print(checkin_post_3)
"""
John Checked In: "At Abbey Road Studios"
  19.111, -9.2222
  Friday, Feb 03, 2017
"""
```
**(check tests to see more examples)**
