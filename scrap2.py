import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import time

def scrape_movie_data(movie_id, movie_name, index, csv_size=100):
    url = 'https://www.boxofficemojo.com/title/' + movie_id+"/"
    with requests.Session() as session:
        response = session.get(url, allow_redirects=False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            region_tables = soup.select('table.a-bordered.a-horizontal-stripes.a-size-base-plus')
            data = []
            for table in region_tables:
                rows = table.find_all('tr')
                ths = rows[0].find_all('th')
                gross_index = 2
                for j,th in enumerate(ths):
                    if "gross" in th.text.lower():
                        gross_index = j  # Skip header row
                for row in rows:
                    cells = row.find_all('td')
                    if len(cells) > 1:
                        country = cells[0].text.strip()
                        gross = cells[gross_index].text.strip()
                        data.append({'movie': movie_name, 'country': country, 'gross': gross})
            print(f"Scraped: {movie_name} ({index})")
            return data, index
        else:
            return [], index

def scrap():
    name_id_o = pd.read_csv('name_id_original.csv')
    name_id = name_id_o
    all_data = []
    csv_size = 1000
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for index, row in name_id.iterrows():
            future = executor.submit(scrape_movie_data, row['tconst'], row['Name'], index)
            futures.append(future)
            if (index + 1) % csv_size == 0 or (index + 1) == len(name_id_o):
                for future in futures:
                    data, idx = future.result()
                    all_data.extend(data)
                    if (idx + 1) % csv_size == 0 or (idx + 1) == len(name_id_o):
                        df = pd.DataFrame(all_data)
                        df.to_csv(f'Scraped_originalTitle/gross_{idx}.csv')
                        all_data = []
                        print(f"Saved: gross_{idx}.csv")
                futures = []

            time.sleep(0.01)  # Rate limiting
        

def merge():
    df = pd.DataFrame(columns=['movie','country', 'gross'])
    for i in range(0, 44):
        df = pd.concat([df, pd.read_csv(f'Scrap/gross_{i}999.csv')])
    df = pd.concat([df, pd.read_csv(f'Scrap/gross_final.csv')])
    df.to_csv('Scrap/gross_merged.csv')


def merge2():
    df = pd.DataFrame(columns=['movie','country', 'gross'])
    df = pd.concat([df, pd.read_csv(f'Scraped_originalTitle/gross_999.csv')])
    df = pd.concat([df, pd.read_csv(f'Scraped_originalTitle/gross_1999.csv')])
    df = pd.concat([df, pd.read_csv(f'Scraped_originalTitle/gross_2995.csv')])
    df.to_csv('Scraped_originalTitle/gross_merged.csv')

def merge3():
    df1 = pd.read_csv('Scraped_originalTitle/gross_merged.csv')
    df2 = pd.read_csv('Scrap/gross_merged.csv')
    df = pd.concat([df1, df2])
    df.to_csv('gross_merged.csv')
    