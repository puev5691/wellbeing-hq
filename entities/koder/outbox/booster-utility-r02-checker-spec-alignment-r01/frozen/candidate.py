def runs(s):
    result = []
    i = 0

    while i < len(s):
        j = i + 1
        while j < len(s) and s[j] == s[i]:
            j += 1

        for start in range(i, j, 3):
            result.append((s[i], min(3, j - start)))

        i = j

    return result
