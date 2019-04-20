import numpy as np
import pandas as pd

#Creating Variables
data_real_state = pd.DataFrame()

# set random seed
np.random.seed(0)

data_real_state['n_dorms'] = (np.random.poisson(4, 100000)//2)

data_real_state['n_suites'] = data_real_state.n_dorms.apply(lambda x:
                                    np.random.randint(x + 1) if x !=0 else 0)

data_real_state['n_bathrooms'] = data_real_state.n_suites.apply(lambda x:
                                    x + 1 + np.random.randint(2) if x != 0
                                    else np.random.randint(1, 2))

# n_dorms == 0 -> n_bathrooms == 1
data_real_state.loc[data_real_state.n_dorms == 0, 'n_bathrooms'] = 1

# 1 - apartment, 0 - house
#supposing apartments are likely to have less bedrooms
data_real_state['real_state_type'] = data_real_state.n_dorms.apply(lambda x:
                                        0 if np.random.randint(x-2,x+5)/3 > 1 else 1 )

# 1 - there is garage, 0 - there isn't garage
#supposing houses are more likely to have garage
#def garage(type):
#    if (type == 0):
#        if (np.random.randint(100) < 85):
#            return 1
#    else: #if type == 1
#        if(np.random.randint(10) < 7):
#            return 1
#    return 0

def garage(type, ndorm):
    if (type == 0):
        if (np.random.randint(100) < (ndorm+1)*25):
            return 1
    else: #if type == 1
        if(np.random.randint(100) < (ndorm+1)*20):
            return 1
    return 0

data_real_state['flag_garage'] = data_real_state.apply(lambda row: garage(row['real_state_type'], row['n_dorms']),axis = 1)
#data_real_state['flag_garage'] = data_real_state.real_state_type.apply(lambda x: garage(x))

#                                    1 if np.random.randint(100) < 85  and x == 0
#                                    else np.random.randint(100) < 70 )  

# 1 - yes, 0 - no
data_real_state['near_subway'] = np.random.randint(2, size=100000)

# 1 - yes, 0 - no
data_real_state['concierge_service'] = data_real_state.real_state_type.apply(lambda x: np.random.randint(2) if x!=0 else 0)

# 1 - yes, 0 - no
data_real_state['furnished'] = np.random.randint(2, size=100000)

data_real_state['age'] = np.random.uniform(0, 45, 100000)

data_real_state['area'] = data_real_state.n_dorms.apply(lambda x: 
                            np.random.normal(55*(1.5*x+1),5))

#                                    np.random.normal(25, 5) if x == 0
#                                    else(np.random.normal(40, 5) if x == 1
#                                    else np.random.normal(50, 5) if x == 2
#                                    else np.random.normal(70, 5)))

# creating true_price using weighted sum + bayesian error
data_real_state['true_price'] = 100+(100 * data_real_state['n_dorms'] +
                                125 * data_real_state['n_suites'] +
                                50 * data_real_state['n_bathrooms'] +
                                30 * data_real_state['real_state_type'] +
                                50 * data_real_state['flag_garage'] +
                                200 * data_real_state['near_subway'] +
                                50 * data_real_state['concierge_service'] +
                                150 * data_real_state['furnished'] +
                                (-15) * data_real_state['age'] +
                                np.random.randint(20,40)*data_real_state['area'])
                                
# creating price using price + variation
data_real_state['price'] = (((np.random.normal(0, 0.1, 100000) + 1) *
                            data_real_state['true_price']))

# creating target using following rule: if price>true_price 1 else 0
#data_real_state.loc[data_real_state['price'] > data_real_state['true_price'],
#                                              'target'] = 1

data_real_state.loc[data_real_state['price'] > 1.05*data_real_state['true_price'], 'target'] = 'expensive'

data_real_state.loc[data_real_state['price'] < 0.95*data_real_state['true_price'], 'target'] = 'cheap'

data_real_state.target = data_real_state.target.fillna('ok')

# Minimum price == 0
data_real_state.loc[data_real_state.price < 0, 'price'] = 0

# print the first 5 lines
print(data_real_state.head())

print("O dataset de tamanho 100000 foi gerado no caminho /data/generate")
# export data
output_path = '../../../data/generate/'
data_real_state.to_excel(output_path + 'generated_data.xlsx', index=False)
