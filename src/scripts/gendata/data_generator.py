import numpy as np
import pandas as pd

#Creating Variables
data_real_state = pd.DataFrame()

# set random seed
np.random.seed(0)

data_real_state['n_dorms'] = np.random.poisson(2, 100000)

data_real_state['n_bathrooms'] = np.random.randint(1, 5, 100000)

data_real_state['n_suites'] = np.random.poisson(1, 100000)

data_real_state['area'] = np.random.normal(50, 15, 100000)

# 1 - apartment, 0 - house
data_real_state['real_state_type'] = np.random.randint(2, size=100000)

data_real_state['age'] = np.random.uniform(0, 45, 100000)

# creating true_price using weighted sum + bayesian error
data_real_state['true_price'] = 1500 + (200 * data_real_state['n_dorms'] +
                                50 * data_real_state['n_bathrooms'] +
                                15 * data_real_state['n_suites'] +
                                5 * data_real_state['area'] +
                                100 * data_real_state['real_state_type'] +
                                (-30) * data_real_state['age'] +
                                np.random.normal(0, 5)
                                )
# creating price using price + variation
data_real_state['price'] = (((np.random.normal(0, 0.1, 100000) + 1) *
                            data_real_state['true_price']))

# creating target using following rule: if price>true_price 1 else 0
data_real_state.loc[data_real_state['price'] > data_real_state['true_price'],
                                              'target'] = 1

data_real_state.target = data_real_state.target.fillna(1)

# print the first 5 lines
print(data_real_state.head())

# export data
output_path = '../../../data/generate/'
data_real_state.to_excel(output_path + 'generated_data.xlsx', index=False)
