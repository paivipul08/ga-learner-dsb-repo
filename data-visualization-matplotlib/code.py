# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()

plt.figure(figsize=[14,8])
plt.bar(loan_status.index,loan_status)


# --------------
#Code starts here





property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)


# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()

education_and_loan.plot(kind='bar',stacked=True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')

plt.xticks(rotation =45)


# --------------
#Code starts here

graduate = data[data['Education']=='Graduate']
not_graduate = data[data['Education']=='Not Graduate']

fig, (ax_1, ax_2) = plt.subplots(1,2, figsize=(20,10))
graduate.plot(kind='density',ax=ax_1,label='Graduate')
ax_1.set_title('Loan Amount')
not_graduate.plot(kind='density',ax=ax_2,label='Not Graduate')
ax_2.set_title('Loan Amount')










#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1, ax_2,ax_3) = plt.subplots(3,1, figsize=(20,10))

data.plot.scatter(x='ApplicantIncome', y='LoanAmount',ax=ax_1)
ax_1.set_title('Applicant Income')

data.plot.scatter(x='CoapplicantIncome', y='LoanAmount',ax=ax_2)
ax_1.set_title('Coapplicant Income')

data['TotalIncome'] = data['ApplicantIncome']+ data['CoapplicantIncome']

data.plot.scatter(x='TotalIncome', y='LoanAmount',ax=ax_2)
ax_1.set_title('Total Income')



