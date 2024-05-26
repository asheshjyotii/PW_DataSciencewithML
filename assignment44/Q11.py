import numpy as np
import pandas as pd

# a) The first Series should contain random numbers ranging from 10 to 50.
series1 = pd.Series(np.random.randint(10, 51, size=50))

# b) The second Series should contain random numbers ranging from 100 to 1000.
series2 = pd.Series(np.random.randint(100, 1001, size=50))

# c) Create a DataFrame by joining these Series by column, and, change the names of the columns to 'col1', 'col2', etc
df = pd.DataFrame({'col1': series1, 'col2': series2})
print(df)
'''
Output:
$ python3 Q11.py
    col1  col2
0     43   806
1     45   164
2     21   280
3     20   639
4     37   948
5     15   920
6     20   628
7     26   797
8     32   555
9     48   679
10    22   991
11    34   242
12    26   356
13    15   712
14    32   200
15    43   811
16    27   512
17    21   963
18    48   252
19    16   708
20    35   975
21    21   205
22    13   379
23    15   507
24    50   111
25    39   972
26    14   283
27    31   261
28    12   345
29    35   135
30    48   884
31    26   904
32    13   121
33    28   365
34    35   780
35    28   938
36    50   647
37    40   900
38    40   873
39    49   117
40    40   288
41    28   231
42    36   478
43    48   375
44    39   154
45    20   784
46    31   354
47    39   570
48    20   679
49    40   492
asheshjyoti@ubuntu:~/house/asheshjyoti/workspace/Learning/Python_and_machineLearning_guided/PW_DataSciencewithML/assignment44 ‹master›
'''