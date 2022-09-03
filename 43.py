# lst1 = ["toyota", "bmw", "benz", "chevrolet", "sony"]
# lst2 = ["samsung", "apple", "sony", "bmw", "ford"]
# eshterak = []
#
# for brand in lst1 :
#     if brand in lst2 :
#         eshterak.append(brand)
#
# print(eshterak)
# ---------------------------------------------
# lst = []
# for i in range(10):
#     if i % 2 == 0 :
#         lst.append(i)
# print(lst)
# ---------------------------------------------
# lst = [ i for i in range(10) if i % 2 == 0 ]
# print(lst)
# ---------------------------------------------
lst1 = ["toyota", "bmw", "benz", "chevrolet", "sony"]
lst2 = ["samsung", "apple", "sony", "bmw", "ford"]
eshterak = [ brand for brand in lst1 if brand in lst2 ]
print(eshterak)
