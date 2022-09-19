scores = {
    "hendese": 18,
    "farsi": 8,
    "zaban": 16,
    "amar va ehtemal": 14,
    "hesaban": 19
}

for k, v in scores.items():
    if v >= 10:
        print(k, ":", v, ": Passed")

    else:
        print(k, ":", v, ": Failed")

print()
moadel = sum(scores.values()) / len(scores)
print("Moadel :", moadel)
