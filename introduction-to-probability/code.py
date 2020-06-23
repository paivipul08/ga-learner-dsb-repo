# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here

df = pd.read_csv(path)
# probability of  fico score greater than 700

p_a = df[df['fico'].astype(float) >700].shape[0]/df.shape[0]
print(p_a)


# probability of purpose == debt_consolidation
p_b = df[df['purpose']== 'debt_consolidation'].shape[0]/df.shape[0]
print(p_b)

# Create new dataframe for condition ['purpose']== 'debt_consolidation' 
df1 = df[df['purpose']== 'debt_consolidation']

# Calculate the P(A|B)
p_a_b = df1[df1['fico'].astype(float) >700].shape[0]/df1.shape[0]
print(p_a_b)
# Check whether the P(A) and P(B) are independent from each other
result = (p_a == p_a_b)
print(result)




# code ends here


# --------------
# code starts here
prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0]/df.shape[0]

prob_cs = df[df['credit.policy'] == 'Yes'].shape[0]/df.shape[0]

new_df = df[df['paid.back.loan'] == 'Yes']

prob_pd_cs = new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]

bayes = (prob_pd_cs*prob_lp)/prob_cs
# code ends here


# --------------
# code starts here
#df[df['purpose']].plot(kind='bar')
#df[df['purpose']].plot.bar()
plt.bar(df['purpose'].index,df['purpose'])

df1 = df[df['paid.back.loan']=='No']
plt.bar(df1['purpose'].index,df1['purpose'])

# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
df.hist('installment',bins=10)
df.hist('log.annual.inc',bins=10)



# code ends here


