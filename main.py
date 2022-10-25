# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

try:
    f1 = open('data.txt', 'r')
    data1 = ['31', '12', '1900']
    while True:
        data = f1.readline().split("-")
        print(data)
        if data[0] == '':
            break
        if int(data[0]) < int(data1[0]):
            data1[0] = data[0]
        if int(data[1]) < int(data1[1]):
            data1[1] = data[1]

    f1.close()
    print(data1[0], " - ", data1[1])
except IOError:
    print(IOError.with_traceback())