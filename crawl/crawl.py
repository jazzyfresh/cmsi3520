import mechanicalsoup
# start link
# for each link:
#   mark link as visited (use map)
#   parse html for links
#   add links to queue

def scrape_links(link):

    #download html for link url
    browser = mechanicalsoup.StatefulBrowser()
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

# Initialize links queue w/ site root
start_url = "https://en.wikipedia.org/wiki/Redis"
links.append(start_url)
visited = {}

# Start crawl
for link in links:
    visited[link] = True
    new_links = scrape_links(link)
    links.extend(new_links)


