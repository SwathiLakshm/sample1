import time
import random
import matplotlib.pyplot as plt

# -----------------------------
# 1. NAIVE SEARCH
# -----------------------------
def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    count = 0
    positions = []

    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            positions.append(i)
            count += 1

    return count


# -----------------------------
# 2. KMP ALGORITHM
# -----------------------------
def compute_lps(pattern):
    lps = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    return lps


def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0
    count = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            count += 1
            j = lps[j - 1]

        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return count


# -----------------------------
# 3. RABIN-KARP
# -----------------------------
def rabin_karp(text, pattern, d=256, q=101):
    n, m = len(text), len(pattern)
    h = pow(d, m-1) % q
    p = t = 0
    count = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i+m] == pattern:
                count += 1

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i+m])) % q
            if t < 0:
                t += q

    return count


# -----------------------------
# 4. BOYER-MOORE (simple version)
# -----------------------------
def boyer_moore(text, pattern):
    n, m = len(text), len(pattern)
    last = {}

    for i in range(m):
        last[pattern[i]] = i

    count = 0
    i = 0

    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            count += 1
            i += m
        else:
            skip = max(1, j - last.get(text[i + j], -1))
            i += skip

    return count


# -----------------------------
# MAIN PROGRAM
# -----------------------------
text = input("Enter text document: ")
pattern = input("Enter pattern to search: ")

algorithms = ["Naive", "KMP", "Rabin-Karp", "Boyer-Moore"]
times = []
matches = []

# Naive
start = time.time()
matches.append(naive_search(text, pattern))
times.append((time.time() - start) * 1000)

# KMP
start = time.time()
matches.append(kmp_search(text, pattern))
times.append((time.time() - start) * 1000)

# Rabin-Karp
start = time.time()
matches.append(rabin_karp(text, pattern))
times.append((time.time() - start) * 1000)

# Boyer-Moore
start = time.time()
matches.append(boyer_moore(text, pattern))
times.append((time.time() - start) * 1000)


# -----------------------------
# PRINT RESULTS
# -----------------------------
print("\nRESULTS TABLE")
for i in range(4):
    print(algorithms[i], "=> Matches:", matches[i], ", Time:", times[i], "ms")


# -----------------------------
# GRAPH 1: EXECUTION TIME
# -----------------------------
plt.figure()
plt.bar(algorithms, times)
plt.title("Algorithm Time Comparison (ms)")
plt.ylabel("Time (ms)")
plt.xlabel("Algorithms")
plt.show()


# -----------------------------
# GRAPH 2: MATCHES FOUND
# -----------------------------
plt.figure()
plt.bar(algorithms, matches)
plt.title("Matches Found Comparison")
plt.ylabel("Number of Matches")
plt.xlabel("Algorithms")
plt.show()