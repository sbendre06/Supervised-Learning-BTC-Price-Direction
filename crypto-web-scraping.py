"""
https://www.gem.wiki/Category:Crypto_mining_in_the_United_States
"Crypto mining in the United States"

Spreadsheet columns:
- Title
- Background
- Power Usage (MW)
- Owner
- Parent
- Location
- Coordinates
- References
- URL

@author: sohan
"""

import os
from bs4 import BeautifulSoup
import time                            # one second sleep in between requests to avoid being blocked
from urllib.request import urlopen
import pandas as pd

fl = []
address = "https://www.gem.wiki/Category:Crypto_mining_in_the_United_States"

avoid = ['/Category:Crypto_mining_in_the_United_States',
         '/Main_Page',
         '/Help:Quick_guide_to_editing',
         '/GEM_Wiki_Style_Manual']

page = urlopen(address)
soup = BeautifulSoup(page, 'html.parser')


for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.startswith('/'):
        # cleaning
        if href and href.startswith('/Category') and href not in avoid:
            avoid.append(href)
        if href and href.startswith('/Special') and href not in avoid:
            avoid.append(href)
        if href and href.startswith('/Global_Energy_Monitor') and href not in avoid:
            avoid.append(href)
        if href and href.startswith('/w') and href not in avoid:
            avoid.append(href)
        
        full_link = "https://www.gem.wiki" + href
        if full_link not in fl and href not in avoid:
            fl.append(full_link)

# print("Total facility pages found:", len(fl))

data = []

def extract_bullets(key, bullets):
    for li in bullets:
        text = li.get_text(" ", strip=True)
        if text.lower().startswith(key.lower()):
            parts = text.split(":", 1)
            if len(parts) > 1:
                return parts[1].strip()
    return ""


for facility in fl:
    try:
        page = urlopen(facility)
        soup = BeautifulSoup(page, 'html.parser')
    except:
        continue

    # Main header
    title = soup.find('h1').get_text(strip=True)


    """ Description
    title_tag = soup.find('h1')
    title = title_tag.get_text(strip=True) if title_tag else ""

    raw_description_test = []
    if title_tag:
        for sibling in title_tag.next_siblings:
            if sibling.name == 'h2' and 'Location' in sibling.get_text():
                break
            if hasattr(sibling, 'get_text'):
                raw_description_test.append(sibling.get_text(" ", strip=True))

    description = " ".join(raw_description_test).strip() """
    

    # Background
    background = ""
    background_header = soup.find('span', string='Background')
    if background_header:
        background_parts = []
        for sibling in background_header.parent.next_siblings:
            if sibling.name == 'h2':
                break
            if sibling.name == 'p':
                background_parts.append(sibling.get_text(" ", strip=True))
        background = " ".join(background_parts).strip()
    

    # Project Details
    project_details_header = soup.find('span', string='Project Details')
    details_bullets = []
    if project_details_header:
        for sibling in project_details_header.parent.next_siblings:
            if sibling.name == 'h2':
                break
            if sibling.name in ['ul', 'ol']:
                details_bullets.extend(sibling.find_all('li'))

    power = extract_bullets("Power usage (MW)", details_bullets)
    owner = extract_bullets("Owner", details_bullets)
    parent = extract_bullets("Parent", details_bullets)
    location = extract_bullets("Location", details_bullets)
    coords = extract_bullets("Coordinates", details_bullets)


    # References
    references = []
    refs_wrap = soup.find("div", class_="mw-references-wrap")
    if refs_wrap:
        for li in refs_wrap.find_all("li", limit=3):
            cite = li.find("cite")
            if cite:
                link = cite.find("a", class_="external text")
                if link:
                    url = link.get("href")
                    text = link.get_text(" ", strip=True)
                    references.append(f"{text} ({url})")
                else:
                    references.append(cite.get_text(" ", strip=True))

    reference_1 = references[0] if len(references) > 0 else ""
    reference_2 = references[1] if len(references) > 1 else ""
    reference_3 = references[2] if len(references) > 2 else ""
    

    data.append({
        'Title': title,
        'Background': background,
        'Power Usage': power,
        'Owner': owner,
        'Parent': parent,
        'Location': location,
        'Coordinates': coords,
        'Reference #1': reference_1,
        'Reference #2': reference_2,
        'Reference #3': reference_3,
        'URL': facility
    })
    
    time.sleep(1)  # delay

df = pd.DataFrame(data)
df.to_excel("crypto-facilities.xlsx", index=False, engine='openpyxl')
