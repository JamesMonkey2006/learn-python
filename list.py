my_list=(list(range(100)))
other_list = [1,2,3,4,5]

def print_list(words, l):
    print("value of", words)
    print('size:', len(l))
    print(l)

print_list('My list', my_list)
print_list("Other list", other_list)