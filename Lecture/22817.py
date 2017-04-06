
from bs4 import BeautifulSoup
import urllib.request # in order to be able to request the URL

def searchForArticles(soup):
    #ask user for a search term to filter articles by
    searchTerm = input("What articles do you want to search for? ")
    #article info is stored in the table
    tableTag = soup.find("table")
    #find all of the link tags that contain the article titles
    storyLinkTags = tableTag.find_all(class_="storylink")
    for storyLinkTag in storyLinkTags:
        articleTitle = storyLinkTag.string
        #only print out the articles containing the search term
        if searchTerm.lower() in articleTitle.lower():
            print("Found! Article title:", articleTitle)
            print("\tArticle URL", storyLinkTag["href"])

def main():
    #request the web page we want to parse from its url
    url = "http://bcf.usc.edu/~parke/py/news.html"
    page = urllib.request.urlopen(url)

    #make soup
    soup = BeautifulSoup(page.read(), "html.parser")
    # print(soup.prettify())

    # #loop through the tags in the soup
    # for tag in soup: #will print the outermost loop
    #     print("A tag in the soup: ", tag)

    # #get tags by their names
    # print("The first link tag ", soup.a)
    # print("The first table", soup.table)

    # # use a for loop to print tag names
    # for tag in soup:
    #     print("The name of a tag:", tag.name)

    # tableTag = soup.table
    # # get information about the table tag
    # print("the name of the tag is", tableTag.name)
    # print("The table's attributes: ", tableTag.attrs) #this will return a dictionary
    # #attributeDictionary = tableTag.attrs #alternate way to do it
    # tableBGColor = tableTag["bgcolor"]
    # print("The Table's background color: ", tableBGColor)

    # tableTag = soup.find("table")
    # #print("Found a table tag:", tableTag)
    # tableRows = tableTag.find_all("tr", class_="athing") #this is a list of tr tags
    # #now table Rows also have to have the class attribute value = athing
    # for tableRow in tableRows:
    #     print("This is a table row", tableRow)

    # #find all the link tags that contain the article titles
    # tableTag = soup.find("table")
    # storyLinkTags = tableTag.find_all(class_="storylink")
    # for storyLinkTag in storyLinkTags:
    #     #print("Story link tag:", storyLinkTag) #the .string will print just the text in between the tags
    #     print("Story link tag:", storyLinkTag.string)
    #     print("Article URL", storyLinkTag["href"])
    searchForArticles(soup)

main()


