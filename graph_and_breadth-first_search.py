 
from collections import deque

graph={}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def person_is_seller(name):
  return name[-1] == 'm'


def search(name):
  search_queue = deque()                            # cоздание новой очереди
  search_queue += graph['you']                      # все соседи добавляются в очередь списка
  searched = []                                     # этот массив используется для отслеживания уже проверенных людей
  while search_queue:                               # пока очередь не пуста
    person = search_queue.popleft()                 # из очереди извлекается первый человек
    if not person in searched:                      # человек проверяется только в том случае, если он не проверялся ранее
      if person_is_seller(person):                  # проверяем, является ли этот человек продацом манго
        print(person + ' is a mango seller!')        # да, это продавец манго
        return True
      else:
        search_queue += graph[person]               # нет, не является; все друзья этого человека добавляются в очередь поиска
        searched.append(person)                     # человек помечается как уже проверенный
  return False                                      # если выполнение дошло до этой строки, значит в очереди нет продавца манго

search('you')
