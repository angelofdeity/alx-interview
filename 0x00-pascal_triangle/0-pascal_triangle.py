def pascal_triangle(n):
    pascal_t = []
    for i in range(1, n + 1):
        if i == 1:
            pascal_t.append([1])
        elif i == 2:
            pascal_t.append([1, 1])
        else:
            prev = pascal_t[i - 2]
            new = [1]
            for j in range(len(prev) - 1):
                new.append(prev[j] + prev[j + 1])
            new.append(1)
            pascal_t.append(new)
    return pascal_t
