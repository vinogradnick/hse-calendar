class Student:
    def __init__(self, email, course, minor):
        self.email = email
        self.course = course
        self.minor = minor

class Page:
    def __init__(self, page_name, ws, is_minor = False):
        self.page_name = page_name
        self.ws = ws
        self.is_minor = is_minor

