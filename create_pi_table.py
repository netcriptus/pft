import json

pi_string = open('pi_hex_1b.txt', 'r').read().strip()

print('Indexing pi')
pi_table = {symbol: [] for symbol in ['0', '1', '2', '3', '4', '5', '6', '7',
                                      '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']}
total = len(pi_string[2:])

for index, char in enumerate(pi_string[2:]):
    print(f'{index/total * 100:.2f}% indexed')
    pi_table[char].append(index)
print('Pi indexed')

with open('indexed_pi_table.json', 'w') as f:
    f.write(json.dumps(pi_table))
