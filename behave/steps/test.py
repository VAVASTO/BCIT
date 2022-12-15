from behave import given, when, then
import sys

sys.path.append('../')

from sort import *

def get_list(inp):
    inp_int = []
    now_str = ""
    for i in inp:
        if (i != ',' and i != ' ' and i != '[' and i != ']'):
            now_str += i
        elif (i != ' ' and i != '['):
            inp_int.append(int(now_str))
            now_str = ""
        else:
            now_str = ""
    return inp_int


@when(u'I sort data {inp}')
def step_impl(context, inp):
    inp_list = get_list(inp)
    print(u'STEP: When I sort data {}'.format(inp_list))
    context.result = abs_sort(inp_list)


@then(u'I get result {out}')
def step_impl(context, out):
    out_list = get_list(out)
    print(u'STEP: Then I get result {}'.format(out))
    assert context.result == out_list, 'Expected {}, got {}'.format(out, context.result)


@when(u'I lambda sort data {inp}')
def step_impl(context, inp):
    inp_list = get_list(inp)
    print(u'STEP: When I sort data {}'.format(inp_list))
    context.result = abs_sort_lambda(inp_list)


@then(u'I lambda get result {out}')
def step_impl(context, out):
    out_list = get_list(out)
    print(u'STEP: Then I get result {}'.format(out))
    assert context.result == out_list, 'Expected {}, got {}'.format(out, context.result)