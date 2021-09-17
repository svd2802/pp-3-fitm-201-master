from concurrent.futures import ThreadPoolExecutor
import requests
import threading
import time


thread_local = threading.local()


def long_session_init():
    time.sleep(1)
    return requests.Session()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = long_session_init()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session:
        with session.get(url) as response:
            #print(f"Read {len(response.content)} from {url}")
            return f"Read {len(response.content)} from {url}"


def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=20) as executor:
        res = executor.map(download_site, sites)
        return list(res)
