boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) != len(girls):
    print('=8<0=85, :B>-B> <>65B >AB0BLAO 157 ?0@K!')
else:
    boys_sorted = sorted(boys)
    girls_sorted = sorted(girls)

    print('450;L=K5 ?0@K:')
    for boy, girl in zip(boys_sorted, girls_sorted):
        print(f'{boy} 8 {girl}')
