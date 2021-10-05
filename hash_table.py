
# хэш-таблица для хранения проголосовавших избирателей
voted ={}
def chec_voter(name):
    if voted.get(name):
        print('kick them out!')
    else:
        voted[name] = True
        print('let them vote!')

chec_voter('tom')
chec_voter('mike')
chec_voter('mike')


# кэширование данных на сервере
cache = {}
def get_page(url):
    if cache.get(url):
        return(cache[url])                      # врвзращаются кэшированные данные
    else:
        data = 'get_data_from_server(url)'
        cache[url] = data                       # данные сначала сохраняются в кэше
        return data