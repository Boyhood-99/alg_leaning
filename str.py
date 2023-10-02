
def replacespace(s:str):
    res = s.replace(' ', '%20')
    return res

print(replacespace('w a s dfg'))
def word_reverse(s: str) -> str:
    s= s.strip()
    s = s[::-1]
    res = ' '.join([word[::-1] for word in s.split()])
    # res = s.split(' ').__reversed__()
    return res
# print(word_reverse('w a s dfg'))
def k_reverse(s:str, k)->str:

    l = len(s)
    s = s[::-1]
    tail = s[-k:]
    head = s[:l-k]
    res = ''.join([head[::-1], tail[::-1]])
    return res
# print(k_reverse('affsvdfgf', 5))
a = [1,2,3]
b = a[:2]
b[0] = 2
# print(a, b)
print(a.pop(), a.pop(0))