def print_result(function_to_decorate): 
    def the_wrapper(*args, **kwargs):
        data = function_to_decorate(*args, **kwargs)
        if (type(data) == list):
            for i in data:
                print(i)
        elif(type(data) == dict):
            for i in data:
                print(f"{i} = {data[i]}")
        else:
            print(data)
        return(data)
    return the_wrapper



@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()