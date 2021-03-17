class UrlPage:
    def __init__(self, urlPage = "", indexPost = int):
        self.urlPage = urlPage
        self.indexPost = indexPost

    def info(self) -> None:
        return "URL: "+ self.urlPage +" | index: "+ str(self.indexPost)
