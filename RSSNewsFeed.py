import feedparser
#Created by DukeMactavish
#Requires feedparser package install with command "pip install feedparser"
#wheel package maybe required for installing feedparser completely, install using "pip install wheel" before installing feedparser
def printer(entry):
    #print('Published Date: ',entry.published_parsed)
    try:
        print('Published Date: ', entry.published)
        print('Title :',entry.title)
        print('Summary:',entry.summary)
        print('Link:',entry.link)
        print('**********')
        print("")
    except AttributeError:
        print('Title :',entry.title)
        print('Link:', entry.link)
        print('**********')
        print("")

def feed(links):
    print('1.TIME World')
    print('2.BBC News')
    print('3.The New York Times')
    print('4.Al Jazeera News')
    print('5.Yahoo News')
    print('6.CNN')
    print('7.Washington Post')
    print('8.CNBC World News')
    print('9.NDTV World news')
    print('10.Reuters')
    print('11.Times of India')
    print('12.The Guardian')
    print('13.ANI News')
    n=(int(input('Enter Choice: ')))-1
    NewsFeed = feedparser.parse(links[n])

    print('Number of RSS posts :', len(NewsFeed.entries))
    for i in range(0,len(NewsFeed.entries)):
        printer(NewsFeed.entries[i])

def search(links):
    query=input("Enter search term: ")
    k=False
    for i in range(0,len(links)):
        NewsFeed = feedparser.parse(links[i])
        try:
            for j in range(0,len(NewsFeed.entries)):
                isPresent=query.lower() in NewsFeed.entries[j].title.lower()
                isThere=query.lower() in NewsFeed.entries[j].summary.lower()
                if isPresent==True or isThere==True:
                    k=True
                    printer(NewsFeed.entries[j])
        except:
            for j in range(0,len(NewsFeed.entries)):
                isPresent=query.lower() in NewsFeed.entries[j].title.lower()
                if isPresent:
                    k=True
                    printer(NewsFeed.entries[j])
    if k==False:
        print("No Info Found")




if __name__ == '__main__':
    feedlink=[]
    feedlink.append("https://feeds.feedburner.com/time/world ")
    feedlink.append("http://feeds.bbci.co.uk/news/world/rss.xml")
    feedlink.append("https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml")
    feedlink.append("https://www.aljazeera.com/xml/rss/all.xml")
    feedlink.append("https://www.yahoo.com/news/rss/world")
    feedlink.append("http://rss.cnn.com/rss/edition_world.rss")
    feedlink.append("http://feeds.washingtonpost.com/rss/world")
    feedlink.append("https://www.cnbc.com/id/100727362/device/rss/rss.html")
    feedlink.append("https://feeds.feedburner.com/ndtvnews-world-news")
    feedlink.append("http://feeds.reuters.com/Reuters/worldNews")
    feedlink.append("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
    feedlink.append("https://www.theguardian.com/world/rss")
    feedlink.append("https://aninews.in/rss/feed/category/world.xml")
    mode=input("Enter S for search mode or F for Feed mode ")
    if mode=='S' or mode=='s':
        search(feedlink)
    elif mode=='F' or mode=='f':
        feed(feedlink)
