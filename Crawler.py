from BokCrawler import BokCrawler

class Crawler:
    def __init__(self):
        self.bokCrawler = BokCrawler()
        self.books = []

    def craw(self, keywords):
        self.books = self.bokCrawler.craw(keywords)
        return self.books

    def download(self, bookLink):
        return self.bokCrawler.download(bookLink) 