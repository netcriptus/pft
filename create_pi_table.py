from redis import StrictRedis

pi_string = open('pi_hex_1b.txt', 'r').read().strip()

redis = StrictRedis('redis')

print('Indexing pi')
total = len(pi_string)


def init_pi_table():
    return {char: [] for char in ['0', '1', '2', '3', '4', '5', '6', '7', '8',
                                  '9', 'a', 'b', 'c', 'd', 'e', 'f', '.']}


def save_pi_table(table):
    for key, values in table.items():
        if values:
            redis.sadd(key, *values)


pi_table = init_pi_table()

for offset in range(100):
    start = 10_000_000 * offset
    end = 10_000_000 * (offset + 1)
    for index, char in enumerate(pi_string[start:end]):
        print(f'{(index+start)/total * 100:.2f}% indexed')
        pi_table[char].append(index + start)
    print('\nconsolidating index...')
    save_pi_table(pi_table)
    pi_table = init_pi_table()
    print('index saved\n')

for index, char in enumerate(pi_string[end:]):
    print(f'{(index+end)/total * 100:.2f}% indexed')
    pi_table[char].append(index + end)

print('\nconsolidating index...')
save_pi_table(pi_table)
print('index saved\n')

print('Pi indexed')
