class Product():
    def __init__(self, title, price, link, website):
        self.title = title[:70]
        self.price = price
        self.link = link
        self.website = website

    def __repr__(self):
        return f'{self.title}\n |Price: ${self.price}\n'