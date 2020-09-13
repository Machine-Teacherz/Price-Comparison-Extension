class Product():
    def __init__(self, title, price, link, website):
        self.title = title
        self.price = price
        self.link = link
        self.website = website

    def __repr__(self):
        return f'\nProduct Title: {self.title}\nProduct Price: ${self.price}\nProduct Link: {self.link}\n'