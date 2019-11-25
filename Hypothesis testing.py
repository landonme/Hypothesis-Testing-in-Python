# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:09:55 2019

@author: Lando
"""
from scipy.stats import t
from scipy.stats import norm
import matplotlib.pyplot as plt

## Some important definitinos
'''
alpha = The probability of observing a sample statistic as extreme (in favor of Ha) as the one you have if the null hypothsis is true.
        The probability you reject Ho when Ho is true.
        The probability of Type 1 Error.
        
Beta =  The probability of observing a sample statistic as inextreme (close to Ho) as the one you have if Ha is true.
        The probability you accept Ho when Ha is actually true.
        The probability of Type 2 Error.
        
Power = The probability of finding an effect when there trully is an effect.
        The probability of rejecting Ho when Ha is true
        1 - Beta
        
'''



# Tests about a single mean
###########################################

### 1 Sample Mean
#################
xbar = 12.3
mu = 11
s = 3
n = 45
tstat = (xbar-mu)/(s/(n**0.5))
alpha = 0.05

# 1 sided, greater than
## Ho: u <= mu
## Ha: u > mu
# We will reject Ho if xbar is greater than
cr = mu + (t.ppf(1-alpha, n-1))*s/(n**.5)
print(cr)
# The probability of getting xbar if u is mu is..
pvalue = 1-t.cdf(tstat, n-1)
print(pvalue)


# 1 sided, less than
## Ho: u >= mu
## ha: u < mu
# We will reject Ho if xbar is less than
cr = mu + (t.ppf(alpha, n-1))*s/(n**.5)
print(cr)
# The probability of getting xbar if u is actually mu is..
pvalue = t.cdf(tstat, n-1)
print(pvalue)


# 2 sided, different than
## Ho: u = mu
## ha: u != mu
# We will reject Ho if xbar is outside the interval
crlower = mu + (t.ppf(alpha/2, n-1))*s/(n**.5)
crupper = mu + (t.ppf(1-(alpha/2), n-1))*s/(n**.5)
print(crlower, ', ', crupper)
# The probability of getting xbar if u is actually mu is..
pvalue = 2*t.cdf(-abs(tstat), n-1)
print(pvalue)


## What's the Power of the Test?
 # Power = Prob(reject Ho | Ha is true)
 # You reject Ho when xbar is more extreme than the critical cut-off
u_ha = 13 # You set this. You can't actually know this..
cr = mu + (t.ppf(1-alpha, n-1))*s/(n**.5)
 # So, power = prob(xbar > cr | u = u_ha)
 #             prob((xbar - u_ha)/se > (cr - u_ha)/se)
 #             prob(t > (cr-u_ha)/se)
t_power = (cr - u_ha)/(s/n**.5)
power = 1-t.cdf(t_power, n-1)
print(power)


# Tests about  2 means
###########################
'''
We can either either use a pooled variance (more powerful) or unpooled.
To test if you can use a pooled variance, test that they're similar'
'''
m1 = 17
n1 = 45
s1 = 4

m2 = 12
n2 = 50
s2 = 4.3

## 2 Tailed
sp = ((n1-1)*s1**2 + (n2-1)*s2**2)/(n1+n2-2) # Pooled Variance
tstat = (m1-m2)/(sp*(1/n1 + 1/n2)**.5)

# Ho: m1 > m2
# Ha: m1 < m2
pvalue = t.cdf(tstat, n1+n2-2)
print(pvalue)

# Ho: m1 < m2
# Ha: m1 > m2
pvalue = 1-t.cdf(tstat, n1+n2-2)
print(pvalue)

# ho: m1 = m2
# ha: m1 !- m2
pvalue = 2*t.cdf(-abs(tstat), n1+n2-2)
print(pvalue)



## Tests about proportions
################################################

## A/B Test
s1 = 190 #Number of Successes in group 1
n1 = 200 # Number of Trials in group 1

s2 = 180
n2 = 200

p1 = s1/n1
p2 = s2/n2

p = (p1*n1 + p2*n2)/(n1+n2) #Used in Test Statistic. This is essentially their weighted avg.
se = ((p1*(1-p1)/n1) + (p2*(1-p2)/n2))**.5 # From STATS class
# se = (p*( 1 - p )*((1/n1) + (1/n2)))**.5 # From Penn State Online
z = (p1-p2)/se #If this is greater than 1.96 then

# Ho: p1 > p2
# Ha: p1 < p2
norm.cdf(z)

# Ho: p1 < p2
# Ha: p1 > p2
1-norm.cdf(z)

# Ho: p1 = p2
# Ha: p1 != p2
2*norm.cdf(-abs(z))



## Power of the Test for h:a P2 > p1

## What's the Power of the Test?
 # Power = Prob(reject Ho | Ha is true)
 # You reject Ho when p1 - p2 is more extreme than the critical cut-off
u_ha = 13 # You set this. You can't actually know this..
cr = 0 + norm.ppf(0.05)*se
 # So, power = prob((p1-p2) > cr | p1=a, ,p2=b)
 #             prob(((p1-p2) - (a-b))/se > (cr - (a-b))/se)
 #             prob(z > (cr - (a-b))/se)
t_power = (cr - u_ha)/(s/n**.5)
power = 1-t.cdf(t_power, n-1)
print(power)





















