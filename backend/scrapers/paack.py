import requests, re
from bs4 import BeautifulSoup

def trackPaack(trackingID='', postalCode=''):

    url = f"https://mydeliveries.paack.app/tracking/order?tracking_number={trackingID}&postal_code={postalCode}"

    response = requests.get(url)

    if "Order not found. Incorrect order number or postal code." in response.text:
        return {
            "requestStatus": "error",
            "message": "Order not found. Incorrect order number or postal code."
        }

    soup = BeautifulSoup(response.content, 'html.parser')

    estimatePattern = re.compile(r'(.*\btypography typography--h6\b.*\border-alert__heading\b.*)')
    statusPattern = re.compile('typography typography--h5 typography--navy-blue-800')
    descriptionPattern = re.compile('typography typography--body1 typography--navy-blue-800')

    return {
        "requestStatus": "success",
        "status": soup.find(class_=statusPattern).get_text(),
        "description": soup.find(class_=descriptionPattern).get_text(),
        "estimated": soup.find(class_=estimatePattern).get_text() 
    }

if __name__ == "__main__":
    print(trackPaack())