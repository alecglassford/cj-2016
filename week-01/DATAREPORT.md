# Comparing Data Portals

## [data.gov](https://www.data.gov/)

The interface is pretty pleasant to navigate, but there's a lot more stuff on the website than just raw data (e.g. links to blog posts, tweets) which was both interesting at moments but also made it harder to find what I wanted to. Also, it was a bit of a bummer that data was in so many different formats, but I suppose that's not all too surprising. The presentation of data was not super consistent either: sometimes there would be direct links to data files, but some links just went to other web pages which then linked to the data files.

## [opendatanetwork.com](http://www.opendatanetwork.com/)

Really straightforward and simple navigation. I like the splash pages for each dataset that have info about columns. I also quite like the "browse by region" feature. Even though it isn't presenting raw data, it's a simple enough feature that it's fun and informative to use; browsing the basic demographic data of different locations offers some insight.

## [data.cityofpaloalto.org](http://data.cityofpaloalto.org/home)

I'm impressed by just how much (apparently pretty recently updated?) data is available for such a small city. There are some cool, weird datasets like [a list of uncashed checks](http://data.cityofpaloalto.org/dataviews/75037/list-of-palo-alto-uncashed-checks/) and [photos of graffiti removal](http://data.cityofpaloalto.org/dataviews/94481/palo-alto-311-graffiti-removal/) that I thought were cool. The site's pretty bare bones though; for example, I wish there was a bit more description of the uncashed dataset: are these checks written by the Palo Alto government to all these people or checks written to P.A. by these people? Probably a naive question, but some context would be nice.

# [fec.gov/data](http://www.fec.gov/data/DataCatalog.do?format=html)

I like that this is just so entirely straightforward. It did timeout on me at one point while I was browsing, which was sad. I really like this presidential candidate who is near the top of the alphabetically sorted list of [candidate summaries](http://www.fec.gov/data/CandidateSummary.do?format=html):

![presidential candidate "A$$, Dat Phat"](images/dat-phat.png "A$$, Dat Phat")

## [data.gov.uk](https://data.gov.uk/)

The organization is similar to data.gov in a lot of ways, and, also similarly, there was an overwhelming variety of data formats available, some of which were fairly unhelpful/annoyihng HTML splash pages.

# Finding Giancarlo Esposito's Stop-and-Frisk Record

I would download the CSV for 2012 (assuming the incident happened within 2 months before the byline of the [article](http://www.thewrap.com/tv/article/breaking-bads-giancarlo-esposito-and-healing-power-gus-fring-44131/?page=0,1)) and then loop through the rows, printing the ones that match these criteria (as best as we can determine from the article/info online):

* datestop = between April 14, 2012 and June 14, 2012
* inout = outside
* pf_drwep (physical force used by officer = weapon drawn) = True
* sex, race, age, height, weight, hair color, etc = matching Esposito's info as can be determined from his Wikipedia/IMDB with some wiggle room (e.g. allow 6 inch window around his actual height)
* all the weapons found fields = False
* If we can figure out what play he was working on, then we can sort by location …

… Otherwise, we can print the results from the other filtering, and check each of the locations on Google Maps to see if any are near a theater.
