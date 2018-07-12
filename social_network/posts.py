from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp if timestamp else datetime.now()
        self.timestring = self.timestamp.strftime("%A, %b %d, %Y")
        self.user = None

    def set_user(self, user):
        self.user = user
    

class TextPost(Post):
    
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        head = '@{} {}: "{}"'.format(self.user.first_name, self.user.last_name, self.text)
        return head + '\n\t{}'.format(self.timestring)
        
        

class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        head = '@{} {}: "{}"'.format(self.user.first_name, self.user.last_name, self.text)
        return head + '\n\t{}\n\t{}'.format(self.image_url, self.timestring)


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        head = '@{} Checked In: "{}"'.format(self.user.first_name, self.text)
        return head + '\n\t{}, {}\n\t{}'.format(self.latitude, self.longitude, self.timestring)
