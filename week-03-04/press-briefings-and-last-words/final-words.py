import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import requests

INDEX_URL = 'http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html'
NO_LAST_STATEMENT_URL = 'http://www.tdcj.state.tx.us/death_row/dr_info/no_last_statement.html'
religion_pattern = re.compile(r'god|jesus|christ|muhammad|allah|islam|creator|maker|heaven|religio|better\W*place', flags=re.IGNORECASE)
last_statement_pattern = re.compile(r'last\W*statement\W*:', flags=re.IGNORECASE)
offender_pattern = re.compile(r'offender\W*:', flags=re.IGNORECASE)
count = 0

def is_last_statement_heading(tag):
    return tag.name == 'p' and last_statement_pattern.search(tag.text)

def is_offender_heading(tag):
    return tag.name == 'p' and offender_pattern.search(tag.text)

def print_if_no_religion(url):
    if url == NO_LAST_STATEMENT_URL:
        return
    last_statement_page = requests.get(url).text
    soup = BeautifulSoup(last_statement_page, 'lxml')
    last_statement_heading = soup.find(is_last_statement_heading)
    if last_statement_heading:
        grafs = last_statement_heading.find_next_siblings('p')
    else:
        print('could not find last statement on', url)
        return
    for graf in grafs:
        if religion_pattern.search(graf.text):
            return
    offender_heading = soup.find(is_offender_heading)
    if offender_heading:
        print(offender_heading.find_next_sibling('p').text)
        global count # sloppy af
        count += 1
    else:
        print('could not find offender name on', url)

if __name__ == '__main__':
    index_page = requests.get(INDEX_URL).text
    soup = BeautifulSoup(index_page, 'lxml')
    links = soup.find_all('a')
    last_statement_urls = [urljoin(INDEX_URL, link.attrs['href']) for link in links
                                if 'last' in link.text.lower()]
    assert(len(last_statement_urls) == 537)

    for url in last_statement_urls:
        print_if_no_religion(url)

    print('total:', count)
    # I'm getting total: 238
