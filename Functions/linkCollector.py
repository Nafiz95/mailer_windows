def getLinks(respond):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(respond, 'lxml')
    links = soup.select('.rc .r a')

    link_storage = []

    for link in links:
        temp = link.get('href')
        if len(temp) > 1:
            link_storage.append(temp)

    if len(link_storage) > 0:
        return link_storage
    else:
        return -1