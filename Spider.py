from BokSpider import BokSpider

class Spider:
    def __init__(self):
        self.bokSpider = BokSpider()
        self.books = []

    def craw(self, keywords):
        self.books = self.bokSpider.craw(keywords)
        return self.books

    def download(self, bookLink):
        return self.bokSpider.download(bookLink) 
