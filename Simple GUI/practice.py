strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
final = []
temp = []

strs.sort(key = lambda x: sorted(x))

for i in range(len(strs)):
    if i + 1 >= len(strs):
        temp.append(strs[i])
        final.append(temp)
        break
    if sorted(strs[i]) != sorted(strs[i+1]):
        temp.append(strs[i])
        final.append(temp)
        temp = []
    else:
        temp.append(strs[i])

print(final)