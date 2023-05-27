#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries
import matplotlib.pyplot as plt
import matplotlib as mat
import pandas as pd
import numpy as np
from tabulate import tabulate
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[2]:


credit = pd.read_csv("DS1_C5_S4_Credit_Data_Hackathon.csv")
credit


# In[3]:


credit.head()


# In[4]:


credit.tail()


# In[5]:


credit.info()


# In[6]:


credit.columns


# In[7]:


credit.isnull().sum()


# In[8]:


def seperate_data_types(credit):
    categorical = []
    continous = []
    for column in credit.columns:
        if credit[column].dtypes == object:
            categorical.append(column)
        else:
            continous.append(column)
    return categorical,continous
categorical,continous = seperate_data_types(credit)
table = [categorical,continous]
print(tabulate({'Categorical':categorical,'continous':continous},headers=['categorical','continous']))


# In[8]:


# Calculating Mean , Min , Max ,Count and SD of Credit amount , Good Price , Days Employed and Total Income
credit[['AMT_INCOME_TOTAL', 'AMT_CREDIT', 'DAYS_EMPLOYED', 'AMT_GOODS_PRICE',]].describe()


# In[17]:


data = pd.pivot_table(credit,index= ['TARGET'],values=['AMT_INCOME_TOTAL','AMT_CREDIT','DAYS_EMPLOYED','AMT_GOODS_PRICE'],aggfunc = ['mean','median', lambda x: x.mode().values[0]])
data


# In[9]:


# information of Categorical and providing null values treatment
def info_of_cat(col):
    print(f" unique values in {col} : {credit[col].unique()}")
    print(f" Mode in {col} : {credit[col].mode()[0]}")
    print(f" Total Counts of Null Value in {col} : {credit[col].isnull().sum()}")


# In[10]:


info_of_cat('NAME_TYPE_SUITE')


# In[11]:


credit['NAME_TYPE_SUITE'].fillna('Unaccompanied',inplace=True)


# In[12]:


info_of_cat('NAME_TYPE_SUITE')


# In[13]:


info_of_cat('OCCUPATION_TYPE')


# In[14]:


credit['OCCUPATION_TYPE'].fillna('Laborers',inplace=True)


# In[15]:


info_of_cat('OCCUPATION_TYPE')


# In[16]:


# information of numerical and providing null values treatment
def info_of_num(col):
    print(f" Mean in {col} : {credit[col].mean()}")
    print(f" Median in {col} : {credit[col].median()}")
    print(f" Total Counts of Null Value in {col} : {credit[col].isnull().sum()}")


# In[17]:


info_of_num('AMT_GOODS_PRICE')


# In[18]:


credit['AMT_GOODS_PRICE'].fillna(538345.1489706662,inplace=True)


# In[19]:


info_of_num('AMT_GOODS_PRICE')


# In[20]:


info_of_num('CNT_FAM_MEMBERS')


# In[21]:


credit['CNT_FAM_MEMBERS'].fillna(2.1556715567155673,inplace=True)


# In[22]:


info_of_num('AMT_INCOME_TOTAL')


# In[23]:


info_of_num('AMT_GOODS_PRICE')


# In[24]:


info_of_num('AMT_CREDIT')


# In[25]:


info_of_num('DAYS_EMPLOYED')


# In[26]:


credit.isnull().sum()


# # Uni - Variate : 

# In[12]:


# definning a function for display the count on bar
def bar_count(ax,count):
    for bar in ax.patches:
        values = f"{round((bar.get_height()/count)*100,2)}%"
        x = bar.get_x()+bar.get_width()/2
        y = bar.get_height()
        ax.annotate(values,(x,y),va="bottom",ha="center")


# ## 1 : Analyze Defaulter & Non-Defaulter (Target)

# In[28]:


fig,ax = plt.subplots(1,2,figsize=(10,6))
ax[0].set_title("Count of Defaulter & Non-Defaulter Clients")
data = credit['TARGET'].value_counts()
labels = data.keys()
sns.countplot(x = credit['TARGET'],ax=ax[0])

plt.pie(data,labels=labels,autopct = "%.2f%%",explode = [0.02,0.04])
plt.show()


# ## Interpretation :  In Target Column  , 1  represents : defaulter Applicants and 0 : Non-defaulter. Here "0" means Non-Defaulter applicants are 92%. and  8% are defaulter applicants.

# ##  2 : Analyze Name_Income_type 

# In[29]:


fig,ax = plt.subplots(figsize=(15,6))
sns.countplot(x = credit['NAME_INCOME_TYPE'])
bar_count(ax,len(credit))
plt.show()


# ## Interpretation : In All Applications  ,  52% Working Clients have applied for loan. 2nd highest is Commercial associate with 23% applications.

# ## 3 : Analyze Gender-wise clients

# In[30]:


fig,ax = plt.subplots(figsize=(10,6))
ax.set_title("Gender-wise Applicants")
sns.countplot(x = credit['GENDER'])
bar_count(ax=ax,count=len(credit))
plt.show()


# ## Interpretation : 66% Female Applicants are applied for loans. Female are more counts than Male.

# ## 4 : Analyze Education of Clients

# In[31]:


fig,ax = plt.subplots(figsize=(15,6))
ax.set_title("Count of Applicants with Highest education")
sns.countplot(x = credit['NAME_EDUCATION_TYPE'])
bar_count(ax,len(credit))
plt.show()


# # Interpretation : Education of maximum clients are secondary special, Which is 71 percent of total applicants.

# ## 5 : Analyze Occupation of Applicants

# In[5]:


fig,ax = plt.subplots(figsize=(15,10))
ax.set_title("Occupation of Clients")
sns.countplot(y = credit['OCCUPATION_TYPE'])
for bar in ax.patches:
        values = bar.get_width()
        y = bar.get_y()+bar.get_height()/2
        x = bar.get_width()
        ax.annotate(values,(x,y),va="bottom",ha="left")
plt.show()


# ## Interpretation : Laborers are 49201 , who has applied for the loan.These are maximum counts in Occupation than other Occupation.

# ## 6 : Analyze Total Documents submitted by Applicants.

# In[33]:


fig,ax = plt.subplots(figsize=(10,6))
ax.set_title("Number of Documents submitted by Applicants")
sns.countplot(x = credit['TOTAL_DOC_SUBMITTED'])
bar_count(ax,len(credit))
plt.show()


# ## Interpretation : 88 percent Applicants have submitted only 1 document for loan application. and from graphs 10% clients have not submitted any documents.

# ## 7 : Analyze NAME_CONTRACT_TYPE

# In[7]:


fig,ax = plt.subplots(figsize=(10,6))
ax.set_title("Total Applications on Cash loans and Revolving loans")
sns.countplot(x = credit['NAME_CONTRACT_TYPE'])
bar_count(ax,len(credit))
plt.show()


# ## Interpretation : From graph, Here More applications have come for cash loan , which is total 90.5 % of total applications. 

# # Bi - Variate

# ## Task : Visualizing the Co-rrelation between All Numerical Columns by Heatmap

# In[35]:


fig,ax = plt.subplots(figsize=(15,7))
sns.heatmap(credit.corr() , cbar=True , linewidth = 0.5, annot = True)
plt.show()


# ## Interpretation : Displaying Co-Relation between all numerical columns by Heatmap. 
# * From heatmap , 
# * Children and Family Members column are Positively co-related.
# * Credit Amount is strongly Positive co-related with Goods Price Amount.
# * Work_Phone column is Strongly Negative Co-related with Days_Employed Column.

# ### Task 1 : Analyze Gender-wise defaulter and Non-Defaulter Applicants 

# In[36]:


fig,ax = plt.subplots(figsize=(10,6))
ax.set_title("Gender-wise defaulter and non-Defaulter clients")
sns.countplot(x = credit['GENDER'],hue=credit['TARGET'])
bar_count(ax,len(credit))
plt.show()


# ## Interpretation : Female Applicants are more non-defaulter than Male , which are 62%

# ### Task 2 : Analyze Income Type with Target.

# In[19]:


fig,ax = plt.subplots(figsize=(16,6))
ax.set_title("Income Type vs Target variables")
sns.countplot(x = credit['NAME_INCOME_TYPE'],hue=credit['TARGET'])
bar_count(ax,len(credit))
plt.show()


# ## Interpretation : 47 % Working Applicants are Non-defaulter and 2nd maximum Non-defaulter are Commercial associates, Which is 22%  who has applied for loan application.

# ### Task 3 : Relationship between Children vs Family Members.

# In[38]:


fig,ax = plt.subplots(figsize=(7,5))
ax.set_title('Children vs Family members')
sns.regplot(x=credit['CNT_FAM_MEMBERS'], y =credit['CNT_CHILDREN'])
plt.show()


# ## Interpretation : Graphs represents positive co-relation , when Family members are increasing and Children counts are also increasing.  
# ### Family counts are high then children counts will be high.  Means Dependent counts will be more then This will become an obstacle in getting the loan approved.

# ### Task 4 : Analze Target Applicants owns Car or not .

# In[39]:


fig,ax = plt.subplots(figsize=(8,6))
ax.set_title("clients own car or not")
sns.countplot(x = credit['Car'],hue=credit['TARGET'])
bar_count(ax,len(credit))
plt.show()


# # Interpretation : 60% Non-Defaulter clients do not own a car. and also maximum  defaulter and non-defaulter client have not any car.

# ### Task 5 : Relationship between Goods Price Vs Amount Credit

# In[40]:


fig,ax = plt.subplots(figsize=(7,5))
ax.set_title('Goods price vs Amount Credit')
sns.scatterplot(x=credit['AMT_CREDIT'], y =credit['AMT_GOODS_PRICE'])
plt.show()


# ## Interpretation : Graphs represents positive co-relation between Credit Amount and Goods Price. when Credit amount of the loan is increasing and Goods Price (means price of the goods for which the loan is given) is also increasing.
# from analysis , Loan Amount is high then Goods Price will be high.

# ### Task 6 : Analyze Target-wise price of the Goods

# In[4]:


fig,ax = plt.subplots(figsize=(15,5))
ax.set_title('Target vs Good Price Amount')
bins = [100000,200000,300000,400000,500000,600000,700000,800000]
sns.histplot(x=credit['AMT_GOODS_PRICE'], hue =credit['TARGET'],bins=bins)
plt.show()


# ## Interpretation : good price amount of maximum non- defaulter clients are between 2-3 lakhs and 4-5 lakhs . it is the price of the goods for which the loan is given.

# ### Task 7 : Analyze Target Applicants owns House or not 

# In[42]:


fig,ax = plt.subplots(figsize=(8,6))
ax.set_title("clients own their own House or not")
sns.countplot(x = credit['House'],hue=credit['TARGET'])
bar_count(ax,len(credit))
plt.show()


# ## Interpretation : 64% Non-Defaulter clients own their own house or flat. and from graph, defaulter and non-defaulter clients both have maximum counts, whose their own house.

# # Task 8 : Analyze Target Applicants vs Contract Type

# In[13]:


fig,ax = plt.subplots(figsize=(8,6))
ax.set_title("Target vs Contract Type")
sns.countplot(x = credit['NAME_CONTRACT_TYPE'],hue=credit['TARGET'])
bar_count(ax,len(credit))
plt.show()


# # Interpretation : As per uni-variate , Cash loan counts are 91% . so here I analyzed that whose applied for cash loan , 83% are non-defaulter applicants and 8% are defaulter Applicants.

# ## Task 9 : Analyze Target Applicants vs NAME_FAMILY_STATUS 

# In[15]:


fig,ax = plt.subplots(figsize=(8,6))
ax.set_title("Target vs NAME_FAMILY_STATUS")
sns.countplot(x = credit['NAME_FAMILY_STATUS'],hue=credit['TARGET'])
bar_count(ax,len(credit))
plt.show()


# # Interpretation : Married Applicants have 59.26% non-defaulter and 5% defaulter. Which are more than other family status. 

# In[ ]:





# ### Task 10 : Analyze Target-wise Credit Amount

# In[6]:


fig,ax = plt.subplots(figsize=(15,5))
ax.set_title('Target vs Credit-Amount')
bins = [100000,200000,300000,400000,500000,600000,700000,800000]
sns.histplot(x=credit['AMT_CREDIT'], hue =credit['TARGET'],bins=bins)
plt.show()


# ## Interpretation : Maximum counts of non-defaulter clients , which have applied for loan . and the range of loan amount of non- defaulter clients is between 2 - 3 lakhs.

# ### Task 11 : Analyze Target-wise Total Income Amount

# In[8]:


fig,ax = plt.subplots(figsize=(15,5))
ax.set_title('Target vs Total Income Amount')
bins = [25000,50000,75000,100000,125000,150000,175000,200000,250000,300000,350000,400000]
sns.histplot(x=credit['AMT_INCOME_TOTAL'], hue =credit['TARGET'],bins=bins)
plt.show()


# ## Interpretation : non-defaulter clients have Total income between 1- 4 lakhs, but maximum non-defaulter clients have income between 1 - 1.5 lakhs and also between 2 - 2.5 lakhs.

# ### Task 12 : Analyze Days Employeed before loan applied with Target

# In[10]:


fig,ax = plt.subplots(figsize=(15,5))
ax.set_title('Days-Employeed Target-wise')
bins = [1000,1500,2000,2500,3000,3500,4000,4500,5000]
sns.histplot(x=credit['DAYS_EMPLOYED'], hue =credit['TARGET'],bins = bins)
plt.show()


# # Interpretation : here graph is right skewed. and number of non-defaulter clients are most and started current employment 1000-1500 days before the loan application. and number of clients are 10000.

# ## Task 13 : Analyze Relationship between Contract type with amount credit and Good price amount.

# In[30]:


fig,ax = plt.subplots(figsize=(10,6))
melt_1 = pd.melt(df, id_vars = ['NAME_CONTRACT_TYPE'], value_vars = ['AMT_CREDIT','AMT_GOODS_PRICE'],
                 var_name = 'variable',value_name = 'value')
sns.lineplot(x = 'NAME_CONTRACT_TYPE', hue = 'variable', y = 'value', data = melt_1  )
plt.show()


# ## Interpretation : Cash loans have high credit amount and good price amount than Revolving loans.

# In[ ]:





# # Multi - Variate :

# ## Task 1 : Analyze Non-defaulter clients , who get loan approval.

# In[3]:


df = credit[(credit['NAME_INCOME_TYPE']=='Working') | (credit['NAME_INCOME_TYPE']=='Commercial associate') &
            (credit['GENDER']!='XNA') & (credit['NAME_EDUCATION_TYPE']=='Secondary / secondary special') &
            (credit['TOTAL_DOC_SUBMITTED']==1) & (credit['NAME_CONTRACT_TYPE']=='Cash loans') & 
            (credit['House']=='Y') & (credit['AMT_GOODS_PRICE']>=200000) & 
            (credit['AMT_GOODS_PRICE']<=300000)& (credit['AMT_INCOME_TOTAL']>=100000)&
            (credit['AMT_INCOME_TOTAL']<=250000) & (credit['DAYS_EMPLOYED']>=1000)& (credit['DAYS_EMPLOYED']<=1500)]


# In[4]:


fig,ax = plt.subplots(1,2,figsize=(10,6))
ax[0].set_title("defaulter and non-defaulter counts")
data = df['TARGET'].value_counts()
labels = data.keys()
sns.countplot(x = df['TARGET'],ax=ax[0])

plt.pie(data,labels=labels,autopct = "%.2f%%",explode = [0.02,0.04])
plt.show()


# # Interpretation : Target - 0 represents non-defaulter clients. from graph , Most applications comes under non-defaulter.
# #### These are the main parameters from which I can find out non - defaulter clients or applicants -
# * clients who are working and His education is secondary special. 
# * clients own their own house. 
# * His income should be between 100000-250000. 
# * Apply for cash loan and loan amount should be between 200000-300000.
# * Those who satisfy all the conditions are non defaulter Applicants.
# ### *As per the analysis, 85% of the applications should be approved for the loan. because it satisfies all the  conditions of non-defaulter clients.

# ## Task 2 : Analyze the defaulter customers.

# In[48]:


# filter the dataset.
df_1=credit[(credit['OCCUPATION_TYPE']== 'Laborers') & (credit['NAME_FAMILY_STATUS']== 'Married') 
            &(credit['DAYS_EMPLOYED']>= 1000) & (credit['DAYS_EMPLOYED']<= 1500)]


# In[49]:


fig,ax = plt.subplots(figsize=(15,5))
ax.set_title('Target vs Days_Employed')
sns.boxplot(y=df_1['DAYS_EMPLOYED'], x =df_1['TARGET'])
plt.show()


# ## Interpretation : from boxplot , I analyzed that ' Target 1 : defaulter clients ' have more spread and distribution than non-defaulter clients . means Many applications have come from the defaulter clients.
# #### These are the main parameters from which I can filter-out defaulter clients.
# * clients are married.
# * working as laborers.
# * started current employment 1000-1500 days before applied the loan.

# ## Task 3 : Analyze for those customers who are in between both defaulter and non-defaulter (case of 50-50).

# In[50]:


df_2=credit[(credit['NAME_EDUCATION_TYPE']=='Secondary / secondary special') & (credit['AMT_INCOME_TOTAL']>=200000)&
        (credit['AMT_INCOME_TOTAL']<=250000)&(credit['NAME_CONTRACT_TYPE']=='Cash loans')]


# In[51]:


fig,ax = plt.subplots(figsize=(10,5))
ax.set_title('target vs income total')
sns.boxplot(x=df_2['TARGET'], y =df_2['AMT_INCOME_TOTAL'])
plt.show()


# ## Interpretation : from boxpplot , I analysed that both target 0 and target 1 have same spread. means here , This is a 50-50 chance to get the loan, as some clients are supporting default parameters and some are non-default.

# In[ ]:




