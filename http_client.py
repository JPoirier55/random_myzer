import logging
import requests
# import backoff
import urllib.parse

logger = logging.getLogger()
logger.setLevel("INFO")


class HttpClient:

    # @backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_time=60, logger=logger)
    def get(self, url):
        headers = {"Accept": "application/json"}
        # encoded_url = urllib.parse.quote(url)
        # print(encoded_url)
        data = requests.get(url, headers=headers)
        if data.status_code != 200:
            logger.error('Error')
            return ''
        else:
            return data.text
