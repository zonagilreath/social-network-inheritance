from factories import (UserFactory, TextPostFactory, PicturePostFactory,
                             CheckInPostFactory)


def test_post_default_user():
    post = TextPostFactory()
    assert post.user == None

def test_post_set_user():
    user = UserFactory()
    post = TextPostFactory()
    post.set_user(user)
    assert post.user == user

def test_post_string_representation():
    user = UserFactory(first_name='Kevin', last_name='Watson')
    post1 = TextPostFactory()
    post2 = PicturePostFactory()
    post3 = CheckInPostFactory()

    post1.set_user(user)
    post2.set_user(user)
    post3.set_user(user)

    assert str(post1) == '@Kevin Watson: "Sample post text"\n\tTuesday, Jan 10, 2017'

    assert str(post2) == '@Kevin Watson: "Sample post text"\n\thttp://fake-domain.com/images/sample.jpg\n\tTuesday, Jan 10, 2017'

    assert str(post3) == '@Kevin Checked In: "Sample post text"\n\t-34.603722, -58.381592\n\tTuesday, Jan 10, 2017'
