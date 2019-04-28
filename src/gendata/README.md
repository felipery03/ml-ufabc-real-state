Creation of 100000 examples of real state in Sao Paulo  

Variables created until now:  

name (distribution, parameters)  

n_dorms int (poisson/2, 2 rooms expected)  
n_suites int (randint based on number of dorms)
n_bathrooms  int (randint based on number of suites)  
real_state_type (randint based on number of dorms, 0: house, 1: apartament)  
flag_garage int (ranint nased on real_state_type and n_dorms, 0: doesn't have garage or 1: has garage)  
near_subway (randint, 0: not near subway or 1: near subway)  
concierge_service (randint based on real_state_type, 0: doesn't have concierge service 1: has concierge service)  
furnished (randint, 0: not furnished or 1: furnished)  
age (continuous, uniform distribution, 0 to 45) 
area (continuous, random based on n_dorms)
true_price: price generated using vars*weigth, with area's weigth being a randint
price: price generated using true_price + normal distribution 
target: object expected category (expensive if price > 1.05*true_price, cheap if price<0.95*true_price and ok for the rest)

Another interesting,not implemented, variables

zone (one-hot-encoding, sul, leste, oeste, centro, norte)  
elevator (randint, 0, 1)  
gym (randint, 0, 1)  
party_room (randint, 0, 1)  
playground (randint, 0, 1)  
swimming_pool (randint, 0, 1)  
court (randint, 0, 1)  

district (one-hot-encoding, pinheiros, aclimação, liberdade...)  
