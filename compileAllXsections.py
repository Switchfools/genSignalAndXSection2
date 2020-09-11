import pandas as pd

inputData = pd.read_csv('input.csv')

allData = pd.DataFrame()

for index, row in inputData.iterrows():

    print("Retrieving: n1={}, n2={}, n3={} and j0 = {}".format(row['n1'], row['n2'], row['n3'], row['j0']))

    temp = pd.read_csv('./results/xSection/n1_{}_n2_{}_n3_{}_j0_{}/xsection.dat'.format(row['n1'], row['n2'], row['n3'], row['j0']))

    allData = pd.concat([allData,temp])

    allData.to_csv('./results/xSection/allResults.csv', index=False)

print(allData)
