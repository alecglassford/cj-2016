from os import makedirs, path

import requests

URL_ENDPOINT = 'https://www.whitehouse.gov/briefing-room/press-briefings'
MAX_PAGE_NUM = 162
INDEX_PAGES_DIR = 'index-pages'
makedirs(INDEX_PAGES_DIR, exist_ok=True)

for pagenum in range(0, MAX_PAGE_NUM):
    resp = requests.get(URL_ENDPOINT, params={'page': pagenum})
    print("Downloaded", resp.url)

    fname = path.join(INDEX_PAGES_DIR, '{}.html'.format(pagenum))
    print("Saving to", fname)
    with open(fname, "w") as wf:
        wf.write(resp.text)
