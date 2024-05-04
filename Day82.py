# Day 82 of 100 days of coding challenge
# Program to count the occurance of alphabets A and M in a text file
def AMCount():
    f = open("story.txt")
    data = f.read()
    print("File content is : ")
    print(data)
    print()
    a = 0
    m = 0
    for i in range(len(data)):
        if data[i] in 'Aa':
            a += 1
        elif data[i] in 'Mm':
            m += 1

    print("A occurs",a,"times")
    print("M occurs",m,"times")


AMCount()

