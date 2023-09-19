import numpy as np
import pandas as pd

data = {'name': ['Kim', 'Lee', 'Park'],
        'score1': [100, 90, 70],
        'score2': [80,70,90]}
df = pd.DataFrame(data)

"""
   name  score1  score2
0   Kim     100      80
1   Lee      90      70
2  Park      70      90
"""

df = pd.DataFrame(df, columns = ['score1', 'name', 'score2'])

"""
   score1  name  score2
0     100   Kim      80
1      90   Lee      70
2      70  Park      90
"""

df1 = pd.DataFrame(data, columns = ['name', 'score1', 'score2'],
                   index = ['a','b','c'])

"""
   name  score1  score2
a   Kim     100      80
b   Lee      90      70
c  Park      70      90
"""

# print(df1.name)
"""
a     Kim
b     Lee
c    Park
"""

df1 = pd.DataFrame(data, columns = ['name', 'score1', 'score2'],
                   index = ['a','b','c']) 
"""
   name  score1  score2
a   Kim     100      80
b   Lee      90      70
c  Park      70      90
"""

#print(df1[['name', 'score1']])

"""
   name  score1
a   Kim     100
b   Lee      90
c  Park      70
"""

df1 = pd.DataFrame(data, columns = ['name', 'score1', 'score2'],
                   index = ['a','b','c'])

"""
   name  score1  score2
a   Kim     100      80
b   Lee      90      70
c  Park      70      90
"""

# print(df1.iloc[1,:])

"""
name      Lee
score1     90
score2     70
Name: b, dtype: object
"""

df1['score3'] = [30,40,50]

"""
   name  score1  score2  score3
a   Kim     100      80      30
b   Lee      90      70      40
c  Park      70      90      50
"""

data2 = pd.Series(['60','70'], index=['b','c'])
df1['score4'] = data2

"""
   name  score1  score2  score3 score4
a   Kim     100      80      30    NaN
b   Lee      90      70      40     60
c  Park      70      90      50     70
"""

del df1['score3']

"""
   name  score1  score2 score4
a   Kim     100      80    NaN
b   Lee      90      70     60
c  Park      70      90     70
"""

df1.loc['d',:] = ['Choi',80,80, np.nan]

"""
   name  score1  score2 score4
a   Kim   100.0    80.0    NaN
b   Lee    90.0    70.0     60
c  Park    70.0    90.0     70
d  Choi    80.0    80.0    NaN
"""