

def order_of_mag(n):
    return n * 10

if __name__ == '__main__':
    result = order_of_mag(6)
    print(result)


# prob need to install pandas first

# import pandas as pd

# eth_df = pd.read_csv('https://raw.githubusercontent.com/mjplacroix/lambda_project_1/master/ETH_master_dataset_features.csv')
# eth_df.shape

# # splitting into train (1315), validate (165), and test (165)
# train = eth_df[eth_df['Date(UTC)'] < '2019-03-01']
# val  = eth_df[eth_df['Date(UTC)'] >= '2019-03-01']
# test = val[val['Date(UTC)'] > '2019-08-15']
# val = val[val['Date(UTC)'] <= '2019-08-15']
# train.shape, val.shape, test.shape

# # dropping datetime column
# train = train.drop(['Date(UTC)'], axis=1)
# val = val.drop(['Date(UTC)'], axis=1)
# test = test.drop(['Date(UTC)'], axis=1)

# train.head()