# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include='object')

print(categorical_var)

numerical_var = bank.select_dtypes(include='number')

print(numerical_var)


# code ends here


# --------------
# code starts here
banks = pd.DataFrame(bank)
banks.drop(['Loan_ID'],inplace=True,axis=1)
#print(banks)

print(banks.isnull().sum())

bank_mode = banks.mode()
#print(bank_mode)

print(banks.columns.values)
cols = banks.columns.values
banks[cols] = banks[cols].fillna(bank_mode.iloc[0])
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],
values='LoanAmount',aggfunc='mean')

print(avg_loan_amount)

#Another way to achieve this
temp_var = banks.groupby(['Gender','Married','Self_Employed'])['LoanAmount'].agg({'LoanAmount':'mean'})
#print(temp_var)
# code ends here



# --------------
# code starts here
loan_approved_se = banks[(banks['Self_Employed']== 'Yes')
    & (banks['Loan_Status']=='Y')].shape[0]
loan_approved_nse = banks[(banks['Self_Employed']== 'No')
    & (banks['Loan_Status']=='Y')].shape[0]

percentage = lambda num : (num/614)*100    
percentage_se = percentage(loan_approved_se)
percentage_nse = percentage(loan_approved_nse)

print(percentage_se,percentage_nse)

# code ends here


# --------------
# code starts here
#print(banks['Loan_Amount_Term'])

def convert_to_year(num):
    return num/12;

loan_term = banks['Loan_Amount_Term'].apply(lambda x: convert_to_year(x))   
big_loan_term = len(loan_term[loan_term >=25 ])
print(big_loan_term)

# code ends here


# --------------






# code starts here
loan_groupby = banks.groupby(['Loan_Status'])['ApplicantIncome','Credit_History']
mean_values = loan_groupby.mean()
print(mean_values)




# code ends here


