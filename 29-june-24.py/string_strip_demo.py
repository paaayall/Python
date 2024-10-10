x = "     hello      "
print(x)
print("length of original string:", len(x))
result = x.strip()
print(result)
print("length of thr string after removing leading and traling saces",len(result))

x= "*************Hiiiii**************"
print("x =", x)
result = x.strip("*")
print("x after removing all leading and traling")
print(result)