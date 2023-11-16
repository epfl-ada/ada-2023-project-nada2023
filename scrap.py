import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import time

def scrape_movie_data(movie_id, movie_name, index,Wiki_ID,Freebase_ID, csv_size=100):
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
                        data.append({'tconst':movie_id,'Wiki_ID':Wiki_ID,'Freebase_ID':Freebase_ID,'movie': movie_name, 'country': country, 'gross': gross})
            print(f"Scraped: {movie_name} ({index})")
            return data, index
        else:
            return [], index

def scrap(path):
    name_id_o = pd.read_csv(path)
    name_id = name_id_o
    all_data = []
    csv_size = 1000
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = []
        for index, row in name_id.iterrows():
            future = executor.submit(scrape_movie_data, row['tconst'], row['Name'], index,row['Wiki_ID'],row['Freebase_ID'])
            futures.append(future)
            if (index + 1) % csv_size == 0 or (index + 1) == len(name_id_o):
                for future in futures:
                    data, idx = future.result()
                    all_data.extend(data)
                    if (idx + 1) % csv_size == 0 or (idx + 1) == len(name_id_o):
                        df = pd.DataFrame(all_data)
                        df.to_csv(f'gross_{idx+1}.csv')
                        all_data = []
                        print(f"Saved: gross_{idx+1}.csv")
                futures = []

            time.sleep(0.01)  # Rate limiting
        

def merge():
    df = pd.DataFrame(columns=["tconst","Wiki_ID","Freebase_ID","movie","country","gross"])
    for i in range(1, 44):
        df = pd.concat([df, pd.read_csv(f'gross_{i}000.csv')])
    df = pd.concat([df, pd.read_csv(f'gross_43561.csv')])
    df.to_csv('gross_merged.csv')


def clean(gross_data):
    df = gross_data.copy()
    df["gross"] = df["gross"].str.replace('$', '').replace(',', '', regex=True)
    df["gross"] = pd.to_numeric(df["gross"], errors='coerce')
    df = df.dropna(subset=['gross'])
    return df