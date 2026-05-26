import time

def function(txt, pat, m, n):

    for i in range(m - n + 1):

        if txt[i:n+i] == pat:
            return i

    return -1


txt = input("Enter a text : ")
pat = input("Enter a pattern : ")

stime = time.time()

result = function(txt, pat, len(txt), len(pat))

etime = time.time()

print("Pattern found at index:", result)

print("Execution Time:", (etime - stime) * 1000, "milliseconds")