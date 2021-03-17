from urlPage import UrlPage

def getPageFromFile(file):
    # PAGE_FILE = "listUrlPage.txt"
    pageFile = open(file,"r")
    lines = pageFile.readlines()
    pageFile.close()

    i = 0
    n = len(lines)
    page = []

    while i < n:
        newPage = UrlPage(lines[i].strip(), int(lines[i+1].strip()))
        print(newPage.info())
        page.append(newPage)
        i=i+2

    return page
