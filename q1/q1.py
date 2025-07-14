import csv
import random
import re
import time

import requests
from bs4 import BeautifulSoup

import config

MIN_INTERVAL = 1.0

def fetch(url: str) -> requests.Response:
    """Fetch a URL with randomized delay and rotating headers."""
    time.sleep(random.uniform(0.5, 1.5) * MIN_INTERVAL)
    headers = random.choice(config.headers_list)
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp

def parse_event(block) -> dict[str, int] | None:
    """Parse a single event block, returning {'name', 'price'} or None."""
    # 取 <h3> 裡的賽事名稱
    h3 = block.find('h3', class_='sc-abd1d3fa-5 kxfKRH')
    if not h3:
        return None
    name = h3.get_text(strip=True).split()[0]
    print(name)

    # 取價格 DIV，並抽出純數字
    price_div = block.find('div', class_='sc-abd1d3fa-10 kdizhO')
    if not price_div:
        return None
    digits = re.sub(r'[^\d]', '', price_div.get_text(strip=True))
    if not digits:
        return None

    return {'name': name, 'price': int(digits)}

def scrape_events() -> list[dict[str, int]]:
    """Scrape all events across configured tabs, filtering duplicates."""
    seen: set[str] = set()
    results: list[dict[str, int]] = []
    base_url = 'https://asiayo.com/zh-tw/package/sport-activities/'

    for main_tab, sub_tab in config.tab_pairs:
        url = f"{base_url}?mainTab={main_tab}&subTab={sub_tab}"
        print(url)
        resp = fetch(url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        blocks = soup.select('div.sc-abd1d3fa-4.earOKD')

        for blk in blocks:
            event = parse_event(blk)
            if not event:
                continue
            # 去掉重複的
            if event['name'] in seen:
                continue
            seen.add(event['name'])
            results.append(event)

    return results

def write_csv(filename: str, data: list[dict[str, int]]):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['賽事名稱', '每人最低價'])
        for row in data:
            writer.writerow([row['name'], row['price']])

def main():
    events = scrape_events()
    for e in events:
        print(e)
    write_csv('activity.csv', events)

if __name__ == '__main__':
    main()