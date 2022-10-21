# def f1(txt):
#     words = txt.split()
#     lengths = [ len(i) for i in words ]
#
#     for i in words :
#         if len(i) == max(lengths):
#             print(i)
#
# f1("Python is a good programming language")

# def f2(txt):
#     words = txt.split()
#     words.sort(key=len)
#     print(words[-1])
#
#
# f2("Python is a good programming language")

def f3(txt):
    words = txt.split()
    print(max(words, key=len))


f3("Python is a good programming language")
