import numpy as np
import random

n_simul = 100
n_bidders = 16
n_demand = 8
markup = 5
error = 5 # equal to markup?
cost_support_inf = 10
cost_support_sup = 100


def simul(a):
	bids = []
	profits = []
	i = 0
	while i < n_bidders:
		c = np.random.random_integers(cost_support_inf,cost_support_sup)
		c_hat = c + np.random.random_integers(-error,error)
		cap = c_hat + markup
		b = bid(c, cap)
		bids.append(b)
		bids.sort()
		k = 0
		while k < n_demand:
			b = bids[k]
			if b > c:
				profit = b - c
				profits.append(profit)
 			k = k + 1
		i = i + 1
	return profits

def bid_function(c):
	a = 20 # in the cost support 
	b = 0.5 # debe ser b < 1
	return a + b*c

def bid(c, cap):
	if bid_function(c) < cap:
		b = cap
	elif bid_function(c) < c:
		b = c
	else:
		b = bid_function(c)
	return b
