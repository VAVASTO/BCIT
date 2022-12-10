from random import sample

def gen_random(num_count, begin, end):
    return sample(range(begin,end), num_count)

print(gen_random(2,1,5))