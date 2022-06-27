#!/usr/bin/python
# Author: Ahmet Bugra Buga
# coding=utf-8

########################################################################################################################
# Library                                                                                                              #
########################################################################################################################
import pandas as pd
import json
import requests
from six import string_types
import json
import requests
from six.moves.urllib.parse import urlencode, urlunparse

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)


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

