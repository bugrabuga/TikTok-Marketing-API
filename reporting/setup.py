#!/usr/bin/python
# Author: Ahmet Bugra Buga
# coding=utf-8
########################################################################################################################
# Library                                                                                                              #
########################################################################################################################
import pandas as pd
import json
import requests
import json
import requests
import datetime as dt


from six import string_types
from six.moves.urllib.parse import urlencode, urlunparse


########################################################################################################################
# Access Token                                                                                                         #
########################################################################################################################

PATH = '/open_api/v1.2/oauth2/access_token/'

def build_url(path, query=""):
    # type: (str, str) -> str
    """
    :param path: Request path
    :param query: Querystring
    :return: Request URL
    """

    schema, netloc = "https", "business-api.tiktok.com"

    return urlunparse((schema, netloc, path, "", query, ""))

def get_access_token(json_str):
    # type: (str) -> dict
    """
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
    secret = 'YOUR_CLIENT_SECRET'
    app_id = 'YOUR_APP_ID'
    auth_code = 'YOUR_AUTH_CODE'

    # Args in JSON format
    my_args = "{\"secret\": \"%s\", \"app_id\": \"%s\", \"auth_code\": \"%s\"}" % (secret, app_id, auth_code)
    print(get_access_token(my_args))


########################################################################################################################
# Get Data                                                                                                             #
########################################################################################################################


PATH = '/open_api/v1.2/reports/integrated/get/'  # Basic Reports End Points

advertiser_list = []

def get_data(access_token ,advertiser, date_from, date_to):
    '''
    :param access_token: ACCESS_TOKEN
    :param advertiser: Your advertiser id list
    :param date_from: since date
    :param date_to: until date
    :return: dataframe
    '''
    url = 'https://business-api.tiktok.com{}'.format(PATH)
    headers = {
        'Access-Token': access_token
    }
    rsp = requests.get(url, headers=headers,
                       json={
                           "metrics": ['spend', 'impressions', 'reach', 'conversion', 'adgroup_name', 'campaign_name',
                                       'video_watched_2s', 'video_watched_6s', 'video_play_actions', 'clicks', 'reach'],
                           "data_level": "AUCTION_ADGROUP",
                           "start_date": date_from,
                           "end_date": date_to,
                           "advertiser_id": advertiser,
                           "service_type": 'AUCTION',
                           "lifetime": False,
                           "report_type": 'BASIC',
                           "dimensions": ["adgroup_id", 'stat_time_day']})
    a = rsp.json()['data']['list']
    dataframe = pd.json_normalize(a)

    return dataframe



if __name__ == '__main__':
    access_token = 'YOUR_ACCESS_TOKEN'
    dataframe_list = []
    dataframe = pd.DataFrame()

    for advertiser in advertiser_list:
        df = get_data(access_token=access_token,advertiser=advertiser, date_from=dt.datetime.today().replace(day=1).strftime("%Y-%m-%d"), date_to=dt.datetime.today().strftime('%Y-%m-%d')) # Month to date
        dataframe_list.append(df)

    data = pd.concat(dataframe_list)








