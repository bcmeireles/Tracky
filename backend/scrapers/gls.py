import requests, re
from bs4 import BeautifulSoup

def trackGLS(trackingID='37604864173'):
    url = f"https://www.gls-portugal.pt/wp-content/plugins/trackin-gls/inc/tracking_code.php?language=en&codigo_in={trackingID}"

    response = requests.get(url).json()

    if response['exitCode'] == 'E999':
        return {
            "requestStatus": "error",
            "message": response['exitMessage']
        }

    soup = BeautifulSoup(response['data']['parcel_current'], 'html.parser')

    # estimatePattern = re.compile(r'(.*\btypography typography--h6\b.*\border-alert__heading\b.*)')
    # statusPattern = re.compile('typography typography--h5 typography--navy-blue-800')
    # descriptionPattern = re.compile('typography typography--body1 typography--navy-blue-800')

    # return {
    #     "requestStatus": "success",
    #     "status": soup.find(class_=statusPattern).get_text(),
    #     "description": soup.find(class_=descriptionPattern).get_text(),
    #     "estimated": soup.find(class_=estimatePattern).get_text() 
    # }

    # Find all rows in the table

    status = soup.find_all('p')[3].text

    infos = soup.select('table tbody tr')[0].find_all('td')
    infos = [x.text for x in infos]
    date, time, description, location = infos

    return {
        "requestStatus": "success",
        "status": status,
        "description": description,
        "location": location,
        "lastUpdateDate": date,
        "lastUpdateTime": time
    }

if __name__ == "__main__":
    print(trackGLS())