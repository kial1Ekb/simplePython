word = 'testt'

length = len(word) 
mid_index = length // 2

if length % 2 == 0:
    print(word[mid_index - 1 : mid_index + 1])
else:
    print(word[mid_index])