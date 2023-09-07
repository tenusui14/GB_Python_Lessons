mess = "345868543"
# res = ""
# for i in range(len(mess)):
#     if mess[i] == mess [-i - 1]:
#         res += mess[i]
# if res == mess:
#     print("palindrom")
# else: print("net")



def pal(a):
    if(len(a) == 1):
        return True
    if a[0] == a[-1]:
        return pal(a[1:-1])
    else: return False

if pal(mess) == False:
    print("net")
else: print("palindr")
