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
        if href and filter(href):
            ## TODO: more filtering of links
            new_links.append(wikipedia_domain + href)

    return new_links


def filter(href):
    return (
        href.startswith("/wiki/") and
        "Help:" not in href and
        "Special:" not in href and
        "Wikipedia:" not in href and
        "Portal:" not in href and
        "Category:" not in href and
        href != "/wiki/Main_Page"
    )

## TESTS ##
# print("/wiki/Main_Page", filter("/wiki/Main_Page"))
# print("/wiki/Wikipedia:General_disclaimer", filter("/wiki/Wikipedia:General_disclaimer"))
# print("/wiki/Portal:Current_events", filter("/wiki/Portal:Current_events"))
# print("/wiki/Category:Wikipedia_contents", filter("/wiki/Category:Wikipedia_contents"))
# print("/wiki/Special:Random", filter("/wiki/Special:Random"))
# exit()

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


