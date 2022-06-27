# TikTok-Marketing-API <img src="https://www.freepnglogos.com/uploads/tik-tok-logo-png/tik-tok-tiktok-logo-app-trend-1.png" width="65" height="75" />


# Overview
-------------------------------------------

**The TikTok's API For Business allows you to directly interact with the TikTok Ads Manager platform for automated ad management and analysis. Typical use cases include:**
<br/>
* Get customized ad performance data
* Create and manage ads in bulk
* Automated ad optimization

-------------------------------------------
# Documentation

See the [pages](https://ads.tiktok.com/marketing_api/docs?id=1702715749213185) folder for more detailed instructions and additional documentation.

-------------------------------------------
# Procedure

1. Step: Before you can use TikTok's API For Business, you need to sign up at the TikTok For Business Developers portal. Go to the TikTok For Business Developers [homepage](https://ads.tiktok.com/marketing_api/homepage)
2. Step: Before you can create an app and start development, you need to create a TikTok ad account and register as a developer. Log in to TikTok For Business Developers portal, and click Become a Developer on the top right. Select the user type that best describes your company, and click Next to move to the next step.
- Technology Company
- Direct Advertiser
- Agency
3. Step: Log in to TikTok For Business Developers portal and navigate to My Apps. Click Create an App. Specify a descriptive name for your application. Watch the [video](https://ads.tiktok.com/marketing_api/docs?id=1702716474845185) for detailed information
4. Step: After your developer application is approved, you (the developer) need to get authorization from the advertiser to manage their accounts. On TikTok Marketing API portal, navigate to My Apps, and click the app that you want to request authorization for. In the Basic Information section, find the advertiser authorization URL. Send the URL to your advertiser so that they can approve the authorization. The advertiser enters the authorization URL in the browser. They will then be navigated to a list of permissions that you selected when creating your developer application. The advertiser reviews the permissions, agrees to the Platform Service Agreement, and clicks Confirm. The advertiser will then be redirected to the redirect URL that you specified when creating the developer application. The authentication code is appended to the redirect URL. The advertiser locates the authentication code (auth_code) value in the URL, and sends it back to you. In the example above, it's **1234c21d2db289199737bcb8c006c23aaf000a1e** With the auth_code, you can make a POST request to the /oauth2/access_token/ endpoint to get a long-term access token. You also need to supply the app_id and secret of your developer application in the request. 
5. Step: After you get auth_code from the advertiser, you can use it to generate a long-term access token.
The auth_code is valid for 1 hour and can be used only once. After the auth_code expires, you need to start over and perform the authorization steps again. You make a POST request to the /oauth2/access_token/ endpoint to get a long-term access token. In the response, the list of advertiser IDs that this token can access, as well as the permission scope of this access token, will also be included. A long-term access token does not expire, but it'll become invalid if the advertiser cancels the authorization. An invalid access token cannot be renewed or refreshed. With the access token, you can access the endpoints according to the permissions that are granted by the advertiser, not the permissions that you apply for when creating your developer application. To get a complete list of advertiser accounts that can be accessed with the access token, use the /oauth2/advertiser/get/ endpoint.

## Request
- ### Request Address: https://business-api.tiktok.com/open_api/v1.2/oauth2/access_token/
- ### Request Method: **POST**
- ### Header

| Field  | Data Type | Description |
| ------------- | ------------- | ------------- |
| Content-Type  | string  | Request message type. Accepted format: "application/json" |

-----------------------------------------------
### Request Parameters
| Field  | Data Type | Description |
| ------------- | ------------- | ------------- |
| app_id  | number  | The App ID applied by the developer. It can be found in the Basic Information section for you app under [My Apps](https://ads.tiktok.com/marketing_api/login?callbackUrl=https%3A%2F%2Fads.tiktok.com%2Fmarketing_api%2Fapps%2F%3Frid%3Dc4gk8kcrgos&rid=4ryksx7mexd). |
| auth_code | string | Authorization code provided once the callback is complete. It is valid for 1 hour and can only be used once. For more details see [Authorization](https://ads.tiktok.com/marketing_api/docs?id=1701890912382977) |
| secret | string | The private key of the developer's App. It can be found in the Basic Information section for you app under [My Apps](https://ads.tiktok.com/marketing_api/login?callbackUrl=https%3A%2F%2Fads.tiktok.com%2Fmarketing_api%2Fapps%2F%3Frid%3Dc4gk8kcrgos&rid=4ryksx7mexd). |

-----------------------------------------------
# Request Example
```python
# coding=utf-8
import json
import requests
from six import string_types
from six.moves.urllib.parse import urlencode, urlunparse

PATH = "/open_api/v1.2/oauth2/access_token/"

def build_url(path, query=""):
    # type: (str, str) -> str
    """
    Build request URL
    :param path: Request path
    :param query: Querystring
    :return: Request URL
    """
    scheme, netloc = "https", "business-api.tiktok.com"
    return urlunparse((scheme, netloc, path, "", query, ""))

def post(json_str):
    # type: (str) -> dict
    """
    Send POST request
    :param json_str: Args in JSON format
    :return: Response in JSON format
    """
    url = build_url(PATH)
    args = json.loads(json_str)
    headers = {
        "Content-Type": "application/json",
    }
    rsp = requests.post(url, headers=headers, json=args)
    return rsp.json()

if __name__ == '__main__':
    secret = SECRET
    app_id = APP_ID
    auth_code = AUTH_CODE

    # Args in JSON format
    my_args = "{\"secret\": \"%s\", \"app_id\": \"%s\", \"auth_code\": \"%s\"}" % (secret, app_id, auth_code)
    print(post(my_args))

```

----------------------------------------------
# Response
```json

HTTPS/1.1 200 OK
{
  "message": "OK",
  "code": 0,
  "data": {
    "access_token": "xxxxxxxxxxxxx",
    "scope": [
      4
    ],
    "advertiser_ids": [
      1234,
      1234
    ]
  },
  "request_id": "2020042715295501023125104093250"
}

```

---------------------------------------------------
# Reporting Endpoints

| Type  | Data Type | Description |
| ------------- | ------------- | ------------- |
| Reporting  | /reports/integrated/get/  | Run an integrated report to get data about ad spend and performance, audience data, playable ads, or DSA. To run a synchronous report, make a GET request. To run an asynchronous report, make a POST request. For details, see Synchronous reports and Asynchronous reports. |
| Reporting | /reports/task/check/ | Check the status of an asynchronous report task. |
| Reporting | /reports/task/download/ | Download the data of an asynchronous report. |


