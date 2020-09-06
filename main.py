import pandas as pd
import os

data = pd.read_csv('input.csv')

for index, row in data.iterrows():
    if row['ranXSec'] == 0:
        print("calculating xsections for: n1={}, n2={}, n3={}, j0= {}".format(row['n1'], row['n2'], row['n3'], row['j0']))

        os.system('./xSection/calcXSection.sh {} {} {} {}'.format(row['n1'], row['n2'], row['n3'], row['j0']))

        data.at[index,'ranXSec'] = 1

        data.to_csv('input.csv',index=False)

    else:
        print("already calculated xsections for: n1={}, n2={}, n3={}, j0= {}".format(row['n1'], row['n2'], row['n3'], row['j0']))
