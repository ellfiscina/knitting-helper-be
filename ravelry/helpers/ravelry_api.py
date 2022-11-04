from django.conf import settings
import requests


def search_yarn(url):
    response = requests.get(url, auth=(
        settings.RAVELRY_USERNAME, settings.RAVELRY_PASSWORD))
    return response.json()
