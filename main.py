class Collection():
    def __init__(self):
        self.collection_name = "Коллекция"
        self.pictures = {}
        self.price = 0



class Author():
    author_name = ""
    dates = ""
    style = ""
    def __init__(self,author_name, dates, style):
        self.author_name = author_name
        self.dates = dates
        self.style = style

class Frame():
    frame_matherial = ""
    frame_color = ""
    frame_price = 0
    def __init__(self, frame_matherial, frame_color, frame_price):
        self.frame_matherial = frame_matherial
        self.frame_color = frame_color
        self.frame_price = frame_price

class Matherials():
    canvas = ""
    paints = ""
    def __init__(self, canvas, paints):
        self.canvas = canvas
        self.paints = paints


class Picture():
    name = ""
    author = Author( None, None, None )
    genre = ""

    frame = Frame(None, None, None)
    matherials = Matherials(None, None)
    price = 0
    def __init__(self, name, author, genre, frame, matherials, price):
        self.name = name
        self.author = author
        self.genre = genre
        self.frame = frame
        self.matherials = matherials
        self.price = price
