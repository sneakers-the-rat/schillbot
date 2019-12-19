import requests
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
import json
import os

base_dir = './schill_text'

base_url = 'https://president.uoregon.edu'
page_urls = ['https://president.uoregon.edu/updates']
page_urls.extend(
    ["https://president.uoregon.edu/updates?page={}".format(i) for i in range(1,11)]
)

# get pages and soup
toc_pages = [bs(requests.get(p).content, 'lxml') for p in page_urls]
post_text = []

for tp in tqdm(toc_pages, position=0):

    post_urls = tp.find(class_="view-content").find_all('a')
    post_urls = [p['href'] for p in post_urls]
    post_urls = [base_url + p for p in post_urls if p.startswith('/') and not p.endswith('.pdf')]
    post_pages = [bs(requests.get(p).content, 'lxml') for p in post_urls]

    for pp in tqdm(post_pages, position=1):
        text = pp.find("article").find(class_="field-item").text
        post_text.append(text)
        if text.startswith('June 30, 2015'):
            break
        #title = pp.find(property="og:title")['content']
        #post_text.append((title, text))

with open(os.path.join(base_dir, 'pres_updates.json'), 'w') as out:
    json.dump(post_text, out)

with open(os.path.join(base_dir, 'pres_updates.json'), 'r') as out:
    post_text = json.load(out)

# get remarks
remarks_url = 'https://president.uoregon.edu/remarks'
remarks_urls = bs(requests.get(remarks_url).content, 'lxml')
remarks_urls = remarks_urls.find(class_='field-item').find_all('a')
remarks_urls = [r['href'] for r in remarks_urls]
for i, r in enumerate(remarks_urls):
    if r.startswith('/'):
        remarks_urls[i] = base_url + r

remarks = [bs(requests.get(url).content, 'lxml') for url in remarks_urls]

remarks_text = []
for rr in tqdm(remarks, position=1):
    text = rr.find("article").find(class_="field-item").text
    #title = rr.find(property="og:title")['content']
    remarks_text.append(text)

with open(os.path.join(base_dir, 'remarks.json'), 'w') as out:
    json.dump(remarks_text, out)

combined_texts = []
combined_texts.extend(post_text)
combined_texts.extend(remarks_text)

combined_texts = [c.replace('\u00a0', ' ') for c in combined_texts]
combined_texts = [c.replace('\n', ' ') for c in combined_texts]

# kill multiple spaces
combined_texts = [' '.join(c.split()) for c in combined_texts]

with open(os.path.join(base_dir, 'schill.json'), 'w') as out:
    json.dump(combined_texts, out)

