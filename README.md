# IS4

TIMETABLE app\
\
Настройка расписания вводится в массивы в конце кода.\
Рандома в алгоритме нет\
\
В коде советую не пытаться разобраться))\
Алгоритмом предусмотрено что лекции проводятся одновременно у всех групп у которых они есть.\
Так же если предмет не получается добавить, (например если нет преподавателей которые его ведут) то он просто не добавится в расписание и об этом не выведется информация.\
Программа в конце вывода выводит словарь с расписанием, после которого выводится\
sumgroups_tt  (сумма занятий в неделю каждой группы по составленному расписанию)\
{'MI': 13, 'TK': 13, 'TTP1': 13, 'TTP2': 13}\
sumgroups_exp  (сумма занятий в неделю каждой группы по еслы бы все занятия из входных данных получилось добавить в расписание)\
{'MI': 13, 'TK': 13, 'TTP1': 13, 'TTP2': 13}\
\
\
Тестовый набор данных для расписания:\
\
Это предметы:\
disciplines = {\
    'A lecture': 1,\
    'E lecture': 1,\
    'A1': 1,\
    'A2': 1,\
    'A3': 1,\
    'B': 1,\
    'C': 1,\
    'E1': 1,\
    'E2': 1,\
    'D1': 1,\
    'F1': 1,\
    'G1': 1,\
    'H1': 1,\
    'D2': 1,\
    'F2': 1,\
    'G2': 1,\
    'H2': 1,\
    'D3': 1,\
    'F3': 1,\
    'G3': 1,\
    'H3': 1,\
    'D4': 1,\
    'F4': 1,\
    'G4': 1,\
    'H4': 1,\
}\
\
Это преподаватели, и какие предметы они ведут:\
teachers = {\
    'A A': ['A1', 'A2', 'A3', 'A lecture'],\
    'B B': ['A1', 'A2', 'A3'],\
    'C C': ['B'],\
    'D D': ['C', 'E1', 'E2'],\
    'E E': ['D1', 'D2', 'D3', 'D4'],\
    'F F': ['F1', 'F2', 'F3', 'F4'],\
    'G G': ['G1', 'G2', 'G3', 'G4'],\
    'H H': ['H1', 'H2', 'H3', 'H4'],\
    'J J': ['E lecture', 'E1', 'E2'],\
}\
\
Это группы и какие предметы у них есть:\
groups = {\
    'TTP1': ['A1', 'A2', 'A3', 'A lecture', 'B', 'C', 'E lecture', 'E1', 'E2', 'D1', 'D2', 'D3', 'D4'],\
    'TTP2': ['A1', 'A2', 'A3', 'A lecture', 'B', 'C', 'E lecture', 'E1', 'E2', 'F1', 'F2', 'F3', 'F4'],\
    'TK': ['A1', 'A2', 'A3', 'A lecture', 'B', 'C', 'E lecture', 'E1', 'E2', 'G1', 'G2', 'G3', 'G4'],\
    'MI': ['A1', 'A2', 'A3', 'A lecture', 'B', 'C', 'E lecture', 'E1', 'E2', 'H1', 'H2', 'H3', 'H4'],\
}\
\
Это кабинеты, и их вместительность:\
rooms = {\
    306: 3,\
    307: 3,\
    308: 3,\
    309: 3,\
    310: 3,\
    311: 3,\
    312: 3,\
    42: 50,\
    43: 50,\
}\
\
Это студенты и к каким группам они принадлежат:\
students = {\
    'yarik': 'TTP1',\
    'yegor': 'TTP1',\
    'sanya': 'TTP1',\
    'merk': 'TTP2',\
    'holivets': 'TTP2',\
    'mykhailov': 'TTP2',\
    'dima': 'TK',\
    'stas': 'TK',\
    'danya': 'TK',\
    'nikolya': 'MI',\
    'oleg': 'MI',\
    'selim': 'MI',\
}\
