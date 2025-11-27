# Задание 2: Создать funnel.csv с визитами, в которых были покупки

purchases = {}
with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            user_id, category = line.split('\t')
            purchases[user_id] = category

with open('visit_log.csv', 'r', encoding='utf-8') as visit_file, \
     open('funnel.csv', 'w', encoding='utf-8') as funnel_file:

    funnel_file.write('user_id,source,category\n')
    header = visit_file.readline()
    for line in visit_file:
        line = line.strip()
        if line:
            user_id, source = line.split(',')
            if user_id in purchases:
                category = purchases[user_id]
                funnel_file.write(f'{user_id},{source},{category}\n')

print("Содержимое funnel.csv:")
with open('funnel.csv', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i >= 4:
            break
        print(line.strip())
