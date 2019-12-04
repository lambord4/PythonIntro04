# Flag of Britain

```python
rows = 11
cols = 11

for i in range(rows):
    print(i, end='\t')
    for _ in range(cols):
        print('* ', end='')
    print()

print()

for i in range(rows):
    print(i, end='\t')
    for j in range(cols):
        if i == 0 or j == 0 or i == rows-1 or j == cols-1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()

for i in range(rows):
    print(i, end='\t')
    for j in range(cols):
        if (i == 0 or j == 0 or i == rows-1 or j == cols-1
                or i == j or i == cols - j -1
                or i == rows // 2 or j == cols // 2):
            print('* ', end='')
        else:
            print('  ', end='')
    print()
```

вывод

```
0	* * * * * * * * * * * 
1	* * * * * * * * * * * 
2	* * * * * * * * * * * 
3	* * * * * * * * * * * 
4	* * * * * * * * * * * 
5	* * * * * * * * * * * 
6	* * * * * * * * * * * 
7	* * * * * * * * * * * 
8	* * * * * * * * * * * 
9	* * * * * * * * * * * 
10	* * * * * * * * * * * 

0	* * * * * * * * * * * 
1	*                   * 
2	*                   * 
3	*                   * 
4	*                   * 
5	*                   * 
6	*                   * 
7	*                   * 
8	*                   * 
9	*                   * 
10	* * * * * * * * * * * 

0	* * * * * * * * * * * 
1	* *       *       * * 
2	*   *     *     *   * 
3	*     *   *   *     * 
4	*       * * *       * 
5	* * * * * * * * * * * 
6	*       * * *       * 
7	*     *   *   *     * 
8	*   *     *     *   * 
9	* *       *       * * 
10	* * * * * * * * * * * 
```

# Multiply table
```python
val1 = 2

for val2 in range(2, 10):
    print(val1, 'x', val2, '=', val1*val2)
print()


for val1 in range(2, 10, 4):
    for val2 in range(2, 10):
        print('{v11:<2} x  {v12:<2} = {s1:<6}'
              '{v21:<2} x  {v22:<2} = {s2:<6}'
              '{v31:<2} x  {v32:<2} = {s3:<6}'
              '{v41:<2} x  {v42:<2} = {s4:<6}'.format(
                v11=val1, v12=val2, s1=val1 * val2,
                v21=val1+1, v22=val2, s2=(val1+1) * val2,
                v31=val1+2, v32=val2, s3=(val1+2) * val2,
                v41=val1+3, v42=val2, s4=(val1+3) * val2)
        )
    print()
    print()
print()


# Pythagorean table
for val1 in range(1, 10):
    for val2 in range(1, 10):
        if val1 == 1 and val2 == 1:
            print('', end='    ')
            continue
        if val1 == 1:
            print(val2, end='   ')
            continue

        print('{:<4}'.format(val1*val2), end='')
    print()
print()
print()
```
вывод

```
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18

2  x  2  = 4     3  x  2  = 6     4  x  2  = 8     5  x  2  = 10    
2  x  3  = 6     3  x  3  = 9     4  x  3  = 12    5  x  3  = 15    
2  x  4  = 8     3  x  4  = 12    4  x  4  = 16    5  x  4  = 20    
2  x  5  = 10    3  x  5  = 15    4  x  5  = 20    5  x  5  = 25    
2  x  6  = 12    3  x  6  = 18    4  x  6  = 24    5  x  6  = 30    
2  x  7  = 14    3  x  7  = 21    4  x  7  = 28    5  x  7  = 35    
2  x  8  = 16    3  x  8  = 24    4  x  8  = 32    5  x  8  = 40    
2  x  9  = 18    3  x  9  = 27    4  x  9  = 36    5  x  9  = 45    


6  x  2  = 12    7  x  2  = 14    8  x  2  = 16    9  x  2  = 18    
6  x  3  = 18    7  x  3  = 21    8  x  3  = 24    9  x  3  = 27    
6  x  4  = 24    7  x  4  = 28    8  x  4  = 32    9  x  4  = 36    
6  x  5  = 30    7  x  5  = 35    8  x  5  = 40    9  x  5  = 45    
6  x  6  = 36    7  x  6  = 42    8  x  6  = 48    9  x  6  = 54    
6  x  7  = 42    7  x  7  = 49    8  x  7  = 56    9  x  7  = 63    
6  x  8  = 48    7  x  8  = 56    8  x  8  = 64    9  x  8  = 72    
6  x  9  = 54    7  x  9  = 63    8  x  9  = 72    9  x  9  = 81    



    2   3   4   5   6   7   8   9   
2   4   6   8   10  12  14  16  18  
3   6   9   12  15  18  21  24  27  
4   8   12  16  20  24  28  32  36  
5   10  15  20  25  30  35  40  45  
6   12  18  24  30  36  42  48  54  
7   14  21  28  35  42  49  56  63  
8   16  24  32  40  48  56  64  72  
9   18  27  36  45  54  63  72  81  
```