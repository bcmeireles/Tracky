import requests
from bs4 import BeautifulSoup

def trackCORREOSEXPRESS(trackingID=""):
    headers = {
        'authority': 's.correosexpress.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'JSESSIONID=1M7wFJ1N1xPGxVRuObRquywfZBYYmVFDcPClz-l7.seguimientosincp-cex-85cc88884-kt9p9; msg_cookie_CEX=true; google_analytics_cookie_CEX=true; _ga=GA1.2.2142291334.1697558640; _gid=GA1.2.571325835.1697558640; _ga_XRPY2P6K3B=GS1.2.1697558639.1.1.1697558686.0.0.0',
        'origin': 'https://s.correosexpress.com',
        'referer': 'https://s.correosexpress.com/SeguimientoSinCP/search;jsessionid=HXHc0hv8iRxbHe1HTaSyHvSElOU_fDe0bRq2tUjM.seguimientosincp-cex-85cc88884-jxxfk',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
    }

    data = {
        'shippingNumber': trackingID,
        'errorCode': '2',
    }

    url = 'https://s.correosexpress.com/SeguimientoSinCP/search'

    response = requests.post(url, headers=headers, data=data)

    soup = BeautifulSoup(response.content, 'html.parser')

    first_tr = soup.find('tbody').find('tr')
    td_elements = first_tr.find_all('td')

    statusOG = td_elements[2].text

    _, date, time = td_elements[0].text.split(" ")

    if "ENTREGADO" in statusOG:
        status = "delivered"
    elif "ADMITIDO" in statusOG or "EN REPARTO" in statusOG:
        status = "confirmed"
    else:
        status = "in transit"

    return {
        "requestStatus": "success",
        "lastUpdateDate": date,
        "lastUpdateTime": time,
        "status": status,
        "description": statusOG,
        "location": td_elements[1].text
    }

if __name__ == "__main__":
    print(trackCORREOSEXPRESS())