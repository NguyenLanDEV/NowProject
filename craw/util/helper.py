def splitUrl(url):
    urls = url.split('/')
    return urls[len(urls)-1]


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]