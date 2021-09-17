import requests


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")
        return f"Read {len(response.content)} from {url}"


def download_all_sites(sites):
    res = []
    with requests.Session() as session:
        for url in sites:
            res.append(download_site(url, session))
    return res
