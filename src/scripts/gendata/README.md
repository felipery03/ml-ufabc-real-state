Creation of 100000 examples of real state in Sao Paulo

Variables created until now:

name (distribution, parameters)

n_dorms int (poisson, 2 rooms expected)
n_bathrooms  int (randint, 1 bathroom expected)
n_suites int (poisson, 1 suite expected)
flag_garage int (ranint, 0 or 1)
near_subway (randint, 0 or 1)
concierge_service (randint, 0, 1)
elevator (randint, 0, 1)
furnished (randint, 0, 1)
area continuous (normal, 50 m^2 esperado, std = 15)
real_state_type (randint, 0: house, 1: apartament)
age (uniform, 0 to 45)

true_price: price generated using vars  + bayesian error
price: price generated using true_price + some distribution
target: if(true_price >= price) 0 else 1

Another interesting variables

zone (one-hot-encoding, sul, leste, oeste, centro, norte)
gym (randint, 0, 1)
party_room (randint, 0, 1)
playground (randint, 0, 1)
swimming_pool (randint, 0, 1)
court (randint, 0, 1)

district (one-hot-encoding, pinheiros, aclimação, liberdade...)
