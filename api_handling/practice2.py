import requests

def fetch_data():
    url = "https://api.freeapi.app/api/v1/public/youtube/videos"
    res = requests.get(url)
    data = res.json()
    
    
    if data.get("success") and "data" in data:
        videos = data["data"]
        if isinstance(videos, list):  # Check if videos is a list
            for video in videos:
                if isinstance(video, dict):  # Check if each video is a dictionary
                    print(f"Name: {video.get('name', 'N/A')} \n Time: {video.get('time', 'N/A')}")
        else:
            print("Videos data is not in the expected format")
    else:
        raise Exception("Failed to fetch data from API")

def main():
    try:
        fetch_data()
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()