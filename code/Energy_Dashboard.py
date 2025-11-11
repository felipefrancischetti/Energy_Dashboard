print("""
      Energy Dashboard project - v1 from November 2025
        -----------------------------------------------
        Created by Felipe Rigone Francischetti
      
      Please refer to the README.md file for more information.
      """)

# %%
# Libraries installation

import requests
import os
from pathlib import Path
from tqdm import tqdm

# %%
# Creating a folder to store the data
#os.mkdir("data")

# %%
# Function for downloading the .csv files

def download_csv(url_temp,
                 years,
                 dest_dir = "data",
                 overwrite = False,
                 show_progress = True
                 ):
    """
    Args:
        url_temp (str): URL with {year} placeholder
        years (iterable): iterable of years
        dest_dir (str): target directory to save files (created if missing)
        overwrite (bool): whether to overwrite existing files (default = False --> skip)
        show progress (bool): show tqdm progress bar if available
    """

    folder = Path(dest_dir)
    folder.mkdir(parents = True, exist_ok = True)

    for year in tqdm(years):
        url = url_temp.format(year = year)
        file_name = f"BALANCO_ENERGIA_SUBSISTEMA_{year}.csv"
        file_path = os.path.join(folder, file_name)

        print(f"Downloading {file_name}...")

        try:
            response = requests.get(url)

            with open(file_path, "wb"):
                print(f"Successfully downloaded {file_name} to {file_path}")

        except Exception as e:
            print(f"Error downloading {file_name}: {e}")

    return response

# %%
# Downloading the dataset from ONS
url = "https://ons-aws-prod-opendata.s3.amazonaws.com/dataset/balanco_energia_subsistema_ho/BALANCO_ENERGIA_SUBSISTEMA_{year}.csv"
years = range(2000, 2025)
response = download_csv(url, years)

for r in response:
    print(r)
print ("Download process finished")