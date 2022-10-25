import numpy as np


KeyWords=["auto","break","case","char","levelst","leveltinue","default","do",
	"double","else","enum","extern","float","for","goto","if",
	"int","long","register","return","short","signed","sizeof","stastic",
	"struct","switch","typedef","union","unsigned","void","volatile","while"]


def main():
    path = input("file path: ")
    level = input("level of stastic (from 1 to 4): ")
    with open(path) as f:  
        code = [line.strip("\n") for line in f.readlines()]
    KeyWords_len = 32
    cnt = 0
    count = np.zeros(KeyWords_len, dtype=int)
    for lines in range(len(code)):
        str = code[lines]
        for i in range(KeyWords_len):
            while 1:
                if str.find(KeyWords[i]) != -1:
                    if str.find("//") != -1:
                        break
                    else:
                        pos = str.find(KeyWords[i])
                        count[i]+=1
                        str = str[pos+len(KeyWords[i]):len(str)]
                else:
                    break

    for i in range(KeyWords_len):
        if count[i] != 0:
            cnt += count[i]

    num = [25, 2, 6, 15, 9]
    x = [0, 0, -1]
    struc = np.zeros(count[num[0]], dtype=int)
    dir = ["else if", "if", "else"]
    for lines in range(len(code)):
        str = code[lines]
        while 1:
            if str.find(KeyWords[num[1]]) != -1:
                if str.find("//") != -1:
                    break
                else:
                    struc[x[0]] += 1
                    break
            if str.find(KeyWords[num[2]]) != -1:
                if str.find("//") != -1:
                    break
                else:
                    x[0]+=1
                    break
            if str.find(dir[1]) != -1:
                if str.find("//") != -1:
                    break
                else:
                    x[1]+=1
                    break
            else:
                break

    divide = np.zeros(x[1], dtype=int)
    s1 = 0
    s2 = 0
    for lines in range(len(code)):
        str = code[lines]
        while 1:
            if str.find(dir[0]) != -1:
                if str.find("//") != -1:
                    break
                else:
                    divide[x[2]]+=1
                    break
            if str.find(KeyWords[num[3]]) != -1:
                if str.find("//") != -1:
                    break
                else:
                    x[2]+=1
                    break
            else:
                break

    for m in range(x[1]):
        if divide[m] == 0:
            s2+=1
        else:
            s1+=1

    if int(level) >= 1:
        print("KeyWords_len num is: ", cnt)
        for j in range(KeyWords_len):
            if count[j] != 0:
                print(KeyWords[j], " num: ", count[j])
    if int(level) >= 2:
        if count[num[0]] != count[num[2]]:
            print("wrong structure")
        else:
            print("The number of switch structure is:",count[num[0]])
        for k in range(count[num[0]]):
            print("switch ", k+1 ," number of case is: ", struc[k])
    if int(level) >= 3:
        print("the number of if-else: ", s2)
    if int(level) >= 4:
        print("the number of if-else if-else: ",s1)
        default: print("wrong")


if __name__ == '__main__':
    main()