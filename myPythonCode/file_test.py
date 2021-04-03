f=open("count_log.txt", "w", encoding="utf-8")
for i in range(1, 11) :
    data="%d번째 줄이다.\n"%i
    f.write(data)
f.close()

with open("./myPythonCode/dream.txt", 'r') as my_file :
    i=0
    while 1:
        line=my_file.readline()
        if not line :
            break
        print(str(i)+" === "+line.replace("\n", ""))
        i=i+1