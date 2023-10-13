import requests
import json

def trackYunexpress(trackingID='CT108157302DE'):
    url = "https://services.yuntrack.com/Track/Query"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Authorization": "Nebula token:undefined",
        "Sec-Fetch-Site": "same-site",
        "Accept-Language": "en-GB,en;q=0.9",
        "Accept-Encoding": "json",
        "Sec-Fetch-Mode": "cors",
        "Host": "services.yuntrack.com",
        "Origin": "https://www.yuntrack.com",
        "Content-Length": "66",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Referer": "https://www.yuntrack.com",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Cookie": "acw_tc=0bc1599816972233517897541e3eaf0d1836ec2b6f640ae87a17798ae5439a",
    }

    data = {
        "NumberList": [f"{trackingID}"],
        "CaptchaVerification": "",
        "Year": 0
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:

        orderData = response.json()['ResultList'][0]
        orderProgress = orderData['TrackInfo']['LastTrackEvent']
        date, time = orderProgress['ProcessDate'].split('T')

        return {
            "requestStatus": "success",
            "lastUpdateDate": date,
            "lastUpdateTime": time,
            "status": orderData['TrackData']['TrackStatus'],
            "description": orderProgress['ProcessContent'],
            "location": orderProgress['ProcessLocation']
        }
    
    else:
        return {
            "requestStatus": "error",
            "message": response.text
        }
    
if __name__ == "__main__":
    print(trackYunexpress())