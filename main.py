from urllib.request import urlopen 
import json 


def main():
    network_id = 700
    date = "2023-12-05"
    redundant_url = f"http://mediamarketstreamer2.irib.ir/redundant/{network_id}/{date}/playlist.json"
    response = urlopen(redundant_url)
    data_json = json.loads(response.read())
    
    url = f"http://mediamarketstreamer2.irib.ir/redundant/{network_id}/{date}/"
    for video_info in data_json:
        print(url + video_info["file"])

main()