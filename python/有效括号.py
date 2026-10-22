s = "()[]{}"

dic = {"[":"]","(":")","{":"}"}
pare_list = []
if len(s)%2 == 1:
    print("false")

for i in range(len(s)):
    if len(pare_list) != 0 and pare_list[-1] in dic and dic[pare_list[-1]] == s[i]:
        pare_list.pop()
    else:
        pare_list.append(s[i])

print(len(pare_list) == 0)
