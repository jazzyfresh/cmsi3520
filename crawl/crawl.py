import mechanicalsoup
import redis
# start link
# for each link:
#   mark link as visited (use map)
#   parse html for links
#   add links to queue

def scrape_links(link, browser):

    #download html for link url
    print(link)
    browser.open(link)

    #find a tags
    a_tags = browser.page.find_all("a")
    #get hrefs
    hrefs = [ a.get("href") for a in a_tags ]

    #concat domain + href = url
    wikipedia_domain = "https://en.wikipedia.org"
    new_links = []
    for href in hrefs:
        if href and href.startswith("/wiki/"):
            ## TODO: more filtering of links
            new_links.append(wikipedia_domain + href)

    return new_links



## MAIN WEB CRAWL LOOP ##

# Initialize Redis connection
r = redis.Redis()

# Initialize links queue w/ site root
start_url = "https://en.wikipedia.org/wiki/Redis"
r.rpush("links", start_url)

# Initialize headless browser
browser = mechanicalsoup.StatefulBrowser()

# Start crawl
while link := r.lpop("links"):
    r.hset("visited", link, 1)
    new_links = scrape_links(link, browser)
    r.rpush("links", *new_links)


