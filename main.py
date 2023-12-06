from urllib.request import urlopen 
import json 


def main():
    # Store network id and date
    network_id = 700
    date = "2023-12-05"
    # Generate url for playlist
    redundant_url = f"http://mediamarketstreamer2.irib.ir/redundant/{network_id}/{date}/playlist.json"
    # Read json response using python magic
    response = urlopen(redundant_url)
    data_json = json.loads(response.read())
    # Generate url that contains a video
    url = f"http://mediamarketstreamer2.irib.ir/redundant/{network_id}/{date}/"
    for video_info in data_json:
       print(url + video_info["file"])
    # Count all files
    files_count, false_exist_count = 0, 0
    for _ in data_json:
        files_count += 1
    print(f"Number of files: {files_count}")
    # Count number of non-existent files
    for video_file in data_json:
        if video_file["exist"] == False:
            false_exist_count += 1
    print(f"Number of false exists: {false_exist_count}")
    
    
main()