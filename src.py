# используется для сортировки
from operator import itemgetter
 
class Include:
    """Библиотека"""
    def __init__(self, id, name, popularity, lang_id):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.lang_id = lang_id
 
class Lang:
    """Язык программирования"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class LangInclude:
    """
    'Библиотеки языка' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, lang_id, include_id):
        self.lang_id = lang_id
        self.include_id = include_id
 
# Языки
lang = [
    Lang(1, 'C++'),
    Lang(2, 'C'),
    Lang(3, 'Python'),
 
    Lang(11, 'C++(другой)'),
    Lang(22, 'C(другой)'),
    Lang(33, 'Python(другой)'),
]
 
# Библиотеки
include = [
    Include(1, 'iostream', 95, 1),
    Include(2, 'stddef.h', 89, 2),
    Include(3, 'numpy', 67, 3),
    Include(4, 'math.h', 79, 1),
    Include(5, 'algorithm', 50, 1),
]
 
lang_include = [
    LangInclude(1,1),
    LangInclude(2,2),
    LangInclude(3,3),
    LangInclude(1,4),
    LangInclude(1,5),
 
    LangInclude(11,1),
    LangInclude(22,2),
    LangInclude(33,3),
    LangInclude(11,4),
    LangInclude(11,5),
]
 
def main():
    """Основная функция"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [(inc.name, inc.popularity, l.name) 
        for l in lang
        for inc in include 
        if inc.lang_id==l.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(l.name, li.lang_id, li.include_id) 
        for l in lang 
        for li in lang_include 
        if l.id==li.lang_id]

    
    many_to_many = [(inc.name, inc.popularity, lang_name) 
        for lang_name, lang_id, include_id in many_to_many_temp
        for inc in include 
        if inc.id==include_id]
    

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(1))
    print(res_11)
    
    print('\nЗадание А2')
    res_12_unsorted = []

    for li in lang:

        l_include = list(filter(lambda i: i[2]==li.name, one_to_many))
      
        if len(l_include) > 0:
          
            res_12_unsorted.append((li.name, len(l_include)))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)
 
    print('\nЗадание А3')
    res_13 = {}

    for inc in include:
        if 'm' in inc.name:
 
            d_emps = list(filter(lambda i: i[0]==inc.name, many_to_many))

            d_emps_names = [x for _,_,x in d_emps]
        
            res_13[inc.name] = d_emps_names
 
    print(res_13)
 
if __name__ == '__main__':
    main()
