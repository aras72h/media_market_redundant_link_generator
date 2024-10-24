import json
import sys
from urllib.request import urlopen, HTTPError


def main():
    # Check for correct usage
    if len(sys.argv) != 3:
        print("Usage: main.py [NETWORK ID] [DATE(yyyy-mm-dd)]")
        sys.exit(1)
    # Store network id and date
    network_id = sys.argv[1]
    date = sys.argv[2]
    # Generate url for playlist
    redundant_url = f"http://mediamarketstreamer2.irib.ir/redundant/{network_id}/{date}/playlist.json"
    # Read json response using python magic
    try:
        response = urlopen(redundant_url)
        data_json = json.loads(response.read())
        # Generate url that contains a video
        url = f"http://mediamarketstreamer2.irib.ir/redundant/{network_id}/{date}/"
        for video_info in data_json:
           print(url + video_info["file"])
        # Count files
        files_count, false_exist_count = 0, 0
        for video_file in data_json:
            # Count number of non-existent files
            if video_file["exist"] == False:
                false_exist_count += 1
            files_count += 1
        print(f"Number of files: {files_count}")
        print(f"Number of false exists: {false_exist_count}")
    # Handle http errors
    except HTTPError as err:
        print(err)
    
    
main()
