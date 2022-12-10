goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
 ]

def field(items, *args):

    assert len(args) > 0
    if len(args) == 1:
        for i in items:        
            yield i[args[0]]

    else:
        for i in items:
            yield {key:i[key] for key in args}


ans = [i for i in field(goods, 'title', 'color')]
print(ans)
#print(field(goods, 'title'))