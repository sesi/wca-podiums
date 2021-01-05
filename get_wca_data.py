import requests
import zipfile

url = "https://www.worldcubeassociation.org/results/misc/WCA_export.tsv.zip"
zip_path = "data/"
zip_filename = "WCA_export.zip"
extract_path = "data/"
extract_filename = "WCA_export"

#Download 
r = requests.get(url, stream=True)

try: 
    r.raise_for_status()
except requests.exceptions.HTTPError:
    raise 
    
with open(zip_path+zip_filename, 'wb') as f: 
    f.write(r.content)
            
#Extract 
with zipfile.ZipFile(zip_path+zip_filename, 'r') as zip_ref:
    zip_ref.extractall(extract_path + extract_filename)  

print("Zip file extracted: {}{}".format(extract_path, extract_filename))