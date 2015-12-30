import csv


def d_load(file_path, d):
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter = '|')
        
        for k, v in reader:
            l = []
            t = ""
            n = 0
            #print('List is: '+ str(l))
            #print('K is: ' + k)
            #print('V is: ' + v)
            #print('Length of V is: ' + str(len(v)))
            for c in v:
                if c != ',':
                    t += c
                elif c == ',':
                    l.append(t)
                    t = ""
            l.append(t)
            #print(l)
            d[k] = l
            #print(d)


d = {}

d_load('tables/test.csv', d)
print(d)
for i in d:
    print(i)
    print(d[i])