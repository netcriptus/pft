from redis import StrictRedis

pi_string = open('pi_hex_1b.txt', 'r').read().strip()

redis = StrictRedis('redis')

print('Indexing pi')
total = len(pi_string)

for index, char in enumerate(pi_string):
    print(f'{index}/{total}\t - {index/total * 100:.2f}% indexed')
    redis.rpush(char, index)
print('Pi indexed')
