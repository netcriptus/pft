import sys
from redis import StrictRedis

redis = StrictRedis('redis')

pi_string = open('pi_hex_1b.txt', 'r').read().strip()

sending_file_path = '../../Desktop/Screenshot 2020-05-04 at 09.33.39.png'
# sending_file_path = sys.argv[1]

send_file = open(sending_file_path, 'rb').read().strip()
hex_file = send_file.hex()


def sequence_in_pi(sequence):
    first_char_indexes = redis.lrange(sequence[0], 0, -1)
    length = len(sequence)
    for index in first_char_indexes:
        if sequence in pi_string[index:index+length+1]:
            return index
    return None


def find_biggest_chunk(hex_string):
    index = sequence_in_pi(hex_string)
    if index is not None:
        return index, len(hex_string), ''

    lower_bound = 0
    upper_bound = len(hex_string)
    pivot = upper_bound // 2

    while pivot != lower_bound or pivot != lower_bound:
        index = sequence_in_pi(hex_string[:pivot])
        print(f'{lower_bound}, {pivot}, {upper_bound}')
        print(f'Index: {index}\n')
        if index is not None:
            lower_bound = pivot
            pivot += (upper_bound - pivot) // 2
        else:
            upper_bound = pivot
            pivot = (pivot - lower_bound) // 2
    chunk = hex_string[:pivot]
    return index, len(chunk), hex_string[pivot:]


chunks = []

while hex_file:
    index, length, hex_file = find_biggest_chunk(hex_file)
    chunks.append((index, length))

print(f'writing {len(chunks)} chunks to disk')
with open('send_file.pft', 'wb') as f:
    for chunk in chunks:
        f.write(str(chunk))
