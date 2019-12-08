
s = 'Thanks to the flexibility of Python such and the powerful such ecosystem of packages, the Azure CLI supports features such '
ch = 'ch'

idx = -1
cnt = 0
while True:
    idx = s.find(ch, idx+1)
    if idx < 0:
        break
    cnt += 1

print(cnt)
