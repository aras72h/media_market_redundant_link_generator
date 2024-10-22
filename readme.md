# Playlist Video Extractor

This Python script extracts video file URLs from a media server, based on a given network ID and date. It fetches a JSON playlist from the specified network, counts the total number of files, and identifies how many files do not exist.

## Requirements
- Python 3.x
- Internet connection

## Usage

```bash
python main.py [NETWORK ID] [DATE(yyyy-mm-dd)]
```

### Example

```bash
python main.py network123 2024-10-22
```

This will generate a list of video URLs for the specified network and date and will display the number of files and non-existent files.

## Error Handling
The script handles HTTP errors and prints the error message if the playlist URL is invalid or inaccessible.

## Output
1. List of video file URLs.
2. Number of files in the playlist.
3. Number of non-existent files.
