import requests

def trackUPS(trackingID=''):
    url = 'https://webapis.ups.com/track/api/Track/GetStatus?loc=pt_PT'

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json',
        'cookie': 'X-CSRF-TOKEN=CfDJ8Jcj9GhlwkdBikuRYzfhrpJG1tFM3nDb1plqhmyNGXqqXQ3QTvvT-yUGxp9pcp-ZV0vcuG9eo5kGKMcWAzWDV1CXrNzlN3gBlSJWsJssg1Nyw-tZt_Ke50sD0ycqHKxELGlRdB9DqXrWnnLFBf2H-AY; AKA_A2=A; bm_sz=493E23DFDBC114D83A3B0C3BE6E09017~YAAQFaVx1LVluPaKAQAAKMKEJBX/Qy7sJbOXEcixR//L7UByPVkKdjQYQ68ED/TEkhdaePjb15N/2FLcys52hbOAogHhkNCIJNAd9OgJhr07Tc4abS8Wo8NnXedbWIyxBuJwVqAsZ2nvmRE92ZsbFvuJygdk+YUjJLOgGq/Gl1nAxKjtdKyg3ciVp2BUNtzdpuQXyD6mh/PmCWSXWh3lDVUghyFH63BI9YmD8p+E6FtoK/+u47x7Q3R/T28uxkLk+RTgryuMQr2yqlfv58I+gFymsWYNQVw5kpTWj0vzjjI=~4605240~3552326; PIM-SESSION-ID=fefKpU5xooXb9LEB; _abck=A756151AE40E0BFE2A68357C0C39BCF5~0~YAAQFaVx1LlluPaKAQAAasWEJAotRV7ApE4w84YiJdp8OX/TBSOBJcqQS9o8uYWaghrJK0+7rprI6fBqYgMQENQ5vNbI++YIJrPZmqdwse9kYDRHgrVBPvbL8Pt9UKDTDl6jZnFDoHaorU8jLE2t8ydJTcD9fsAsAYHGKKP+gtefo2ntIDq7vawqdMoKklaNvLsfBaimpEXbChtmYNXrcxYmKmbXHtrbX8eJnmTk9zhkCo/7UkcTVkFW4IfEyRkhF+WVKdcUDgA9TDYfxOcAQw180rQJcVs7UyBM1WwH7A7AnqPNCOgkpQZ6M0KJIOj+Q7zhj92Qw/Q7d5gvwF0+45eODp3/9Bvs8dKEs2b8oyOy3+awfFswyWm4bQa26vvLnsb3SIJsC1O+ttQ7b1cNCAt9prnI~-1~-1~1697128245; st_cur_page=st_track; at_check=true; AMCVS_036784BD57A8BB277F000101%40AdobeOrg=1; s_vnum=1698796800386%26vn%3D1; s_invisit=true; dayssincevisit_s=First%20Visit; s_cc=true; _fbp=fb.1.1697124767439.1909180231; _gcl_au=1.1.359598990.1697124767; mboxEdgeCluster=37; aam_cms=segments%3D25426334; aam_uuid=20530293630107161303309256526316832124; _ga=GA1.1.1425312669.1697124768; aap_cms=Global~BusinessRTG; HASSEENNOTICE=TRUE; s_fid=7522A652C1848819-1F4689A1E9E92B41; CONSENTMGR=consent:true%7Cts:1697125564798; com.ups.ims.lasso.sDataLassoFeb19=78d31cb6aeb1436e827953bf6df72e49:uRUjc5FEPAH4InljNvOz9TAU2ZCPdrrtXmpOhJBp5ws=; bm_mi=A364C9AFA773EE4D1BD7C36500D60A43~YAAQZrwvF8AQXxaLAQAA7zqVJBUDmOISwW3GzKW2PXrTh/1N/52hUAmNeN9/1G5fIRqatifk6bbnFAP2ToS1TzxiDjuS9cRWrp0Wh2RPJvVxkK/bRz+URMepfwaMvGH63c5fFTGav6BMJ3D/4L5ecLghTT4lNteKpR+WwoItdOSexjy36dvLi135QnSzxhkrdO5G6f1Tz4LDRnG/SdiRq1AxIwGdwHKwhKNCMvZa285d4AgJRh2wsnOCEiC8FcKywxfaAMJPUGHxjFx6Jttc1aOq5XND1stT+UzYsIBw4wD3Dj2iPlkDEGoauRyd0lXijTfu1u81omrczUzl3w==~1',
        'origin': 'https://www.ups.com',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'x-xsrf-token': 'CfDJ8Jcj9GhlwkdBikuRYzfhrpJKCxsNG5AyaGEMKq0dVjqDq8Ix2776o__MVmMtj8_6G-vF_5UOW14Fz7aOCd0VWyW2PY4pbl9Vcd9Lp60roG2-IkDdW-orUsKw8o2poS_6ew4B4jMqvtM-DEgloQSyFu8'
    }

    data = {
        'Locale': 'pt_PT',
        'TrackingNumber': [f'{trackingID}'],
        'Requester': 'sbn',
        'returnToValue': ''
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        orderData = response.json()['trackDetails'][0]
        orderProgress = orderData['shipmentProgressActivities'][0]

        status = orderData['packageStatus']
        
        if status == "ENTREGUE":
            status = "delivered"
        elif "O expedidor criou uma etiqueta" in status:
            status = "waiting"
        else:
            #"Saiu para Entrega" in status or ("Chegou " in status and "Instala" in status)
            status = "intransit"

        return {
            "requestStatus": "success",
            "lastUpdateDate": orderProgress['date'],
            "lastUpdateTime": orderProgress['time'],
            "status": status,
            "description": orderProgress['activityScan'],
            "location": orderProgress['location'],
            "leftAt": orderData['leftAt'],
            "progress": orderData['progressBarPercentage']
        }
    
    else:
        return {
            "requestStatus": "error",
            "message": response.text
        }
        
if __name__ == "__main__":
    print(trackUPS())