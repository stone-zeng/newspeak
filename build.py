import json
import random

INPUT_FILE  = 'data.txt'
OUTPUT_FILE = 'docs/data.js'
CHAR_RANGE  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='

def split(a, n):
    k, m = divmod(len(a), n)
    return [a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)]

with open(INPUT_FILE, 'r') as fp:
    lines = [l[:-1] for l in fp.readlines() if len(l) > 1 and l[0] != '#']

lines = list(set(lines))
random.shuffle(lines)
data = split(lines, len(CHAR_RANGE))

encryption = {c: i for i, c in zip(data, CHAR_RANGE)}
decryption = {}

for i, c in zip(data, CHAR_RANGE):
    for s in i:
        decryption[s] = c

export_data = {
    'encryption': encryption,
    'decryption': decryption,
}

with open(OUTPUT_FILE, 'w') as fp:
    json_str = json.dumps(export_data, ensure_ascii=False, separators=(',', ':'))
    # json_str = json.dumps(export_data, ensure_ascii=False, indent=2)
    fp.write(f'const data={json_str};')
