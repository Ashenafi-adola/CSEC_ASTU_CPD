n, m = map(int, input().split())
pr = 'b'
for i in range(1, n+1):
    if i%2 != 0:
        print('#'*m)
    else:
        if pr == 'b':
            print('.'*(m-1)+'#')
            pr = 'f'
        else:
            print('#'+'.'*(m-1))
            pr = 'b'