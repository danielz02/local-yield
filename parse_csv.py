import os
import io
import csv
import json
from tqdm import tqdm

f_names = os.listdir(path="./raw/")
f_csv = io.open("yields.csv", "w", newline="")
csv_writer = csv.writer(f_csv, delimiter=",")

csv_writer.writerow([
    "Year", "FIPS", "Lat", "Lng", "City", "County",
     "State", "Crop Type", "Yield Average", "Planting Date",
     "Harvest Date", "Tillage"
])

is_written = set()
for f_name in tqdm(f_names):
    with io.open(os.path.join("./raw/", f_name)) as f:
        try:
            j = json.load(f)
            for report in j["harvestReports"]:
                year = report["reportYear"]
                fips = report["fipsCode"]
                lat = report["latitude"]
                lng = report["longitude"]
                city = report["city"]
                county = report["county"]
                state = report["state"]
                crop_type = report["cropName"]
                yield_avg = report["performanceValueAvg"]
                plant_date = report["plantingDate"]
                harvest_date = report["harvestDate"]
                tillage_practice = report["tillageSystem"]
                if f"{year}{lat}{lng}" in is_written:
                    continue
                csv_writer.writerow([
                    year, fips, lat, lng, city, county,
                    state, crop_type, yield_avg, plant_date,
                    harvest_date, tillage_practice
                ])
                is_written.update(f"{year}{lat}{lng}")
        except json.decoder.JSONDecodeError:
            with io.open("error.log", "a") as f_error:
                f_error.writelines([f"{f_name}\n"])

print("Check error.log for the zip code corresponding to the\
      file caused decode error")
f_csv.close()
