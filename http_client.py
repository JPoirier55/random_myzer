import logging
import requests

logger = logging.getLogger()
logger.setLevel("INFO")


class HttpClient:
    def get(self, url):
        headers = {"Accept": "application/json"}
        data = requests.get(url, headers=headers)
        if data.status_code != 200:
            logger.error('Error')
            return ''
        else:
            return data.text

