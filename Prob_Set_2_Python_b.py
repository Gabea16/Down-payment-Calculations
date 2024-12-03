# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:11:52 2024

@author: gabea
"""

# Establish Variables and input requests
print('Enter your annual salary:')
annual_salary=float(input())

print('Enter the percentage of your salary to save, as a decimal:')
portion_saved=float(input())

print('Enter the cost of your dream home:')
total_cost=float(input())

print('Enter the semi-annual raise, as a decimal:')
semi_annual_raise=float(input())

# Initializing more variables
portion_down_payment=.25*total_cost
months=0
current_savings= 0
r=.04

# when current savings is less than required down payment, execute the additions onto current savings and months. For every 6 months, add the semi annual raise to salary. Looped until Current savings meets portion needed, then print number of months of savings needed to meet downpayment requirement.
while current_savings<portion_down_payment:
    current_savings += current_savings*r/12
    current_savings += portion_saved*(annual_salary/12)
    months+=1 
    if months % 6 == 0:
        annual_salary += semi_annual_raise*annual_salary       
if current_savings>=portion_down_payment:
    print('Number of months:'+str(months))