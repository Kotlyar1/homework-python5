with open('myfile.txt', 'w') as file:
    file.write('aaabbccxc')

with open('myfile.txt', 'r') as file:
    string = file.read()

def comp(data):
    count = 1
    i = 0
    get = ''
    if data == '':
        return ''
    for i in range(len(data) - 1):
        if data[i+1] == data[i]:
            count += 1
        else:
            get += str(count) + data[i]
            count = 1
        data[i] == data[i-1]
    get += str(count) + data[-1]

    return get
print(comp(string))

with open('myfile.txt', 'a') as file:
    file.write(f'{comp(string)}\n')

with open('myfile.txt', 'r') as file:
    string = file.read()

def decomp(data):
    count = 1
    get = ''
    if data == '':
        return ''
    for i in range(len(data) - 1):
        if data[i].isdigit():
            for item in range(0,int(data[i])):
                get += data[i+1]
                count += 1
    return get
print(decomp(string))

with open('myfile.txt', 'a') as file:
    file.write(f'{decomp(string)}\n')