# Simulaciones de los modelos que aparecen en el PDF

Game:
Each seller i receives ci and capi. Where ci U[0,1] and capi =ci+ei where eiU[0,0.1] 
Each seller i decides b_i and submits bid in the range [0, ci+ei] 
Buyer accepts the 8th lowest offers and buys those paying the corresponding bids
Seller i’s profits are given by:
(c,b)=(b-c) Pr[selling]
where:
Pr[selling]=Pr[b<B(8)]=1-Pr[B(8)<b]=1-F(8)(b)

and where F(8)(b) is the CDF for the 8th order statistics of other’s bids in a sample of 15 other bidders.

Equilibrium:
It is assumed a symmetric equilibrium function
bi(ci,capi)=b*(ci,capi)

Conjectures on the equilibrium form:
Consider b(ci) to be i’s optimal bidding when everyone else faces a price cap except i and, also, everyone plays b*(ci,capi). If we conjecture that i’s profit function (ci,bi) is quasiconcave in i’s bid (this is a form of single crossing property), we have that the equilibrium function must take this form:
b*(ci,capi)=min{b(ci),capi}
Where b(ci) is an increasing, continuous function.

This simplifies a lot the search for equilibrium since b(ci) does have simple properties such as strict monotonicity. More importantly we can ignore the cap from the perspective of the optimizing bidder assuming it applies only to the rest. The numerical exercises show this conjecture is correct at least to the extent the equilibrium found numerically has this form. 

Numerical exercises:
I applied the logic above to find the equilibrium function b(ci). 

This is how the numerical exercise works: 
I start with a b(ci) assumed to be a polynomial of degree 5. This is the matlab function poly_8.m. Initial form is linear.
Then I assume everyone else plays b*(ci,capi)=min{b(ci),capi}
Assuming this allows me to form the CDF of “others’ bids”.  This is in the matlab function F_cap.m. This is F-i(z)
With the CDF of others bids, I can form the CDF of the 8th lowest draw of others’ bids using standard order-statistics formulae. I denoted this CDF above as F(8)(b). This is in the matlab function n_th_ord_CDF.m.
With this I can form the probability of winning = 1-F(8)(b)
Putting all together, I input all these elements in the profit function called cap_obj.m. where we will optimize over b: (ci,b)=(b-ci) (1-F(8)(b))
The objective function in called in the m file called a__MainCap.m that also set the other parameters such as the number of sellers and the number of objects to be bought. 
The way I find the equilibrium is by iterating over coefficients of b(ci). For example, I start assuming everyone plays b(c)=0.5+0.5c1+0c2+0c3+0c4+0c5 and then find i’s best response to that in terms of new polynomial coefficients. Then I assume everyone else plays according to those new coefficients and recalculate the best response. I keep doing that until things converge. 
It is important to note this is not the best method as it assumes iterative best responses approaches to equilibrium. That is not always the case and it is not guaranteed here. However if the initial values are not crazy, it seems to work ok in our case. 

