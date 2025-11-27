# Задание 1: Перевести содержимое purchase_log.txt в словарь purchases

purchases = {}

with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            user_id, category = line.split('\t')
            purchases[user_id] = category


for i, (user_id, category) in enumerate(purchases.items()):
    if i >= 2:
        break
    print(f"{user_id} '{category}'")
