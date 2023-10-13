import requests

def trackCTT(trackingID=""):
    url = "https://appserver.ctt.pt/CustomerArea/screenservices/CustomerArea/CustomerArea/PublicArea_Detail/DataActionGetObjectEventsByInputObjectCode"

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

    payload = {
        "versionInfo": {
            "moduleVersion": "fHzQul8d4fprogzPJA75zA",
            "apiVersion": "7xkSp+Ya4qhcHfQtlYx7Bw"
        },
        "viewName": "CustomerArea.PublicArea_Detail",
        "screenData": {
            "variables": {
                "ObjectEvents": {
                    "ObjectCode": "",
                    "ObjectImageURL": "",
                    "ObjectSenderImageUrl": "",
                    "ObjectSenderImageUrlSmall": "",
                    "RelabelObjectCode": "",
                    "ObjectName": "",
                    "IsTracked": False,
                    "Found": False,
                    "CustomsPurposes": False,
                    "Sender": "",
                    "SenderCountryCode": "",
                    "Recipient": "",
                    "RecipientCountryCode": "",
                    "RecipientAddress": "",
                    "RecipientPostalCodeAndTown": "",
                    "RecipientTimeSlot": "",
                    "UserEmailMatch": False,
                    "UserSenderMatch": False,
                    "UserPhoneMatches": False,
                    "IsLocker": False,
                    "LockerName": "",
                    "IsDeliveryPoint": False,
                    "CreationDate": "1900-01-01T00:00:00",
                    "ClearanceDate": "1900-01-01T00:00:00",
                    "DeliveryTimeSlot": "",
                    "DeliveryDeadlineEnd": "1900-01-01T00:00:00",
                    "DeliveryDeadlineDayAndMonthForStories": "",
                    "CTTObject": False,
                    "CarrierID": 0,
                    "CarrierLogoURL": "",
                    "ContractNumber": "",
                    "ClientNumber": "",
                    "FollowObject_Status": 0,
                    "ClientContractCompanyName": "",
                    "SenderLogo": "0",
                    "IsOpenStory": False,
                    "ShipmentProduct": "",
                    "ClientReference": "",
                    "Events": {
                        "List": [],
                        "EmptyListItem": {
                            "DateTime": "1900-01-01T00:00:00",
                            "DateMonthText": "",
                            "State": "",
                            "StateId": 0,
                            "Event": "",
                            "EventCode": "",
                            "EventColorType": 0,
                            "Local": "",
                            "Situation": "",
                            "Reason": "",
                            "Progress": 0,
                            "PointCode": "",
                            "ReceptorName": "",
                            "LockerName": "",
                            "WithdrawalDate": "1900-01-01",
                            "WithdrawalDateMonthText": "",
                            "TypeOfTimelineEvent": 0
                        }
                    },
                    "SpecialServices": {
                        "List": [],
                        "EmptyListItem": {
                            "Description": "",
                            "Value": "",
                            "SepId": "",
                            "IsPaymentOnDestination": False
                        }
                    },
                    "JoinedDeliveries": {
                        "JoinedDeliveryId": "",
                        "IsPrincipalCode": False
                    },
                    "RelatedObjects": {
                        "List": [],
                        "EmptyListItem": {
                            "backObjectId": "",
                            "ers": "",
                            "originalBackObjectId": "",
                            "originalErsnObj": "",
                            "originalReturnObjectId": "",
                            "return": "",
                            "originalReturnObjectd": ""
                        }
                    }
                },
                "IsPopupVisible": False,
                "PopupObjectNumber": "",
                "PopupObjectName": "",
                "IsTracked": False,
                "ShowS10Code": False,
                "IsClickedLocal": False,
                "PaymentOnDeliveryList": "",
                "ObjectsLength": -1,
                "ShowMenu": False,
                "DisableButton": False,
                "DisableButton_Save": False,
                "BreadCrumbPathTemporary": {
                    "List": [],
                    "EmptyListItem": 0
                },
                "BreadCrumbPath": {
                    "List": [],
                    "EmptyListItem": 0
                },
                "ObjectCreationDate": "1900-01-01T00:00:00",
                "IsFromHistory": False,
                "IsResizingListenerRunning": False,
                "HasAssociatedObjects": False,
                "UnfollowAllClicked": False,
                "IsAddedToHistory": False,
                "DisableEditNameIcon": False,
                "WindowWidth": 1245,
                "InputVar": trackingID,
                "ObjectsToSearch": trackingID,
                "LoadingPageDone": False,
                "HideWhileOnReadyIsCharging": False,
                "HasBackServices": False,
                "IsToShowInstallBanner": False,
                "StoreName": "",
                "ObjectCodeInput": trackingID,
                "_objectCodeInputInDataFetchStatus": 1,
                "SearchInput": trackingID,
                "_searchInputInDataFetchStatus": 1,
                "IsFromPublicArea": True,
                "_isFromPublicAreaInDataFetchStatus": 1
            }
        },
        "clientVariables": {
            "ClientDomain": "",
            "NewAddressId": "0",
            "IsNewAddress": False,
            "LastURL": "",
            "PostMessageToLogin": False,
            "ShowUndoToastMessage": False,
            "AddressId": "0",
            "DeletedLockerId": "0",
            "IsUserCard": False,
            "ShowPaymentToastMessage": False,
            "IsFromPublicArea": False,
            "AddingLockerId": "0",
            "ClientVarGoToDetail_CA": "",
            "Username": "",
            "ObjectDetail": "",
            "IsDeletingAddress": False,
            "SubstituteLockerId": "0",
            "SelectedAmountToCharge": "0",
            "RequestedMoneyTransactionInternalRef": "0"
        }
    }

    response = requests.post(url, headers=headers, json=payload, cookies={"CookieName": "cookie_value"})

    if response.status_code == 200:
        if response.json()['data']['ObjectEventsFromQuery']['Found']:
            orderData = response.json()['data']['ObjectEventsFromQuery']['Events']['List'][0]

            date, time = orderData['DateTime'].split('T')
            time = time[:-1]

            return {
                "requestStatus": "success",
                "lastUpdateDate": date,
                "lastUpdateTime": time,
                "status": orderData['State'],
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