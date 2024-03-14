import requests

def trackCTT(trackingID=""):
    url = "https://appserver.ctt.pt/CustomerArea/screenservices/DF_TrackTrace_CW/TrackTrace/TT_AssociatedJoinedDeliveries/DataActionGetJoinedDeliveries"

    headers = {
        "accept": "application/json",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "content-type": "application/json; charset=UTF-8",
        "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-csrftoken": "T6C+9iB49TLra4jEsMeSckDMNhQ="
    }

    referrer = f"https://appserver.ctt.pt/CustomerArea/PublicArea_Detail?IsFromPublicArea=true&ObjectCodeInput={trackingID}&SearchInput={trackingID}"

    payload = {"versionInfo":{"moduleVersion":"Lfi4CZHO8aTWwwzRiqo1rg","apiVersion":"nCR2VKVqPnK7LRNWISTmZg"},"viewName":"CustomerArea.PublicArea_Detail","screenData":{"variables":{"ObjectsLastEvent2":{"List":[],"EmptyListItem":{"ObjectCode":"","ObjectImageURL":"","ObjectSenderImageURL":"","ObjectSenderImageUrlSmall":"","RelabelObjectCode":"","ObjectName":"","IsTracked":False,"Found":False,"CustomsPurposes":False,"Sender":"","SenderCountryCode":"","Recipient":"","RecipientCountryCode":"","RecipientAddress":"","RecipientPostalCodeAndTown":"","RecipientTimeSlot":"","UserEmailMatch":False,"UserSenderMatch":False,"UserPhoneMatches":False,"IsLocker":False,"LockerName":"","CreationDate":"1900-01-01T00:00:00","ClearanceDate":"1900-01-01T00:00:00","DeliveryTimeSlot":"","DeliveryDeadlineEnd":"1900-01-01T00:00:00","DeliveryDeadlineDayAndMonthForStories":"","CTTObject":False,"CarrierID":0,"CarrierLogoURL":"","ContractNumber":"","ClientNumber":"","FollowObject_Status":0,"ClientContractCompanyName":"","SenderLogo":"0","IsOpenStory":False,"ShipmentProduct":"","ClientReference":"","LastEvent":{"DateTime":"1900-01-01T00:00:00","DateMonthText":"","State":"","StateId":0,"Event":"","EventCode":"","EventColorType":0,"Local":"","Situation":"","Reason":"","Progress":0,"PointCode":"","ReceptorName":"","LockerName":"","WithdrawalDate":"1900-01-01","WithdrawalDateMonthText":"","TypeOfTimelineEvent":0},"JoinedDeliveries":{"JoinedDeliveryId":"","IsPrincipalCode":False},"RelatedObjects":{"List":[],"EmptyListItem":{"backObjectId":"","ers":"","originalBackObjectId":"","originalErsnObj":"","originalReturnObjectId":"","return":"","originalReturnObjectd":""}}}},"IsMobile":True,"_isMobileInDataFetchStatus":1,"ObjectCode":trackingID,"_objectCodeInDataFetchStatus":1,"ShowBlock":False,"_showBlockInDataFetchStatus":1}}}

    response = requests.post(url, headers=headers, json=payload, cookies={"CookieName": "cookie_value"})

    if response.status_code == 200:
        # print(response.json()['data']['ObjectsLastEvent_FromService']['List'][0])
        if response.json()['data']:
            orderData = response.json()['data']['ObjectsLastEvent_FromService']['List'][0]['LastEvent']

            date, time = orderData['DateTime'].split('T')
            time = time[:-1]

            status = orderData['State']

            if status == "Entregue":
                status = "delivered"
            
            elif status in ['Em entrega', 'Em distribuição', 'Em trânsito']:
                status = 'intransit'

            elif status in ['Aguarda entrada nos CTT', 'Aceite']:
                status = 'waiting'
            

            return {
                "requestStatus": "success",
                "lastUpdateDate": date,
                "lastUpdateTime": time,
                "status": status,
                "description": orderData['Event'],
                "location": orderData['Local'],
                "reason":  orderData['Reason'],
                "receptorName": orderData['ReceptorName'],
                "progress": orderData['Progress']
            }
    
        else:
            return {
                "requestStatus": "error",
                "message": "invalid_tracking"
            }
    else:
        return {
            "requestStatus": "error",
            "message": response.text
        }

if __name__ == "__main__":
    print(trackCTT())