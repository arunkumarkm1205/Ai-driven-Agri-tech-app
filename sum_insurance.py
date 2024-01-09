#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import numpy as np


# In[80]:


data = pd.read_csv("insurance(R).csv")
data_new = data.copy(deep = True)


# In[81]:


data.head()


# In[82]:


import re

obj_columns = data.select_dtypes("object")

for col in obj_columns:
    data[col] = data[col].apply(lambda x: re.sub(r'[^a-zA-Z0-9]', '', x.lower())).astype("str")


# In[83]:


data.head()


# In[84]:


season_catogory = list(data.season.values)
scheme_catogory = list(data.scheme.values)
state_catogory  = list(data.state_name.values)
district_catogory = list(data.district_name.values)


# In[85]:


columns = ['season','scheme','state_name','district_name']
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
for col in columns:
    data[col] = encoder.fit_transform(data[col])


# In[86]:


season_label = list(data.season.values)
scheme_label = list(data.scheme.values)
state_label = list(data.state_name.values)
district_label = list(data.district_name.values)


# In[87]:


season_category_label_dict = dict(zip(season_catogory, season_label))


# In[88]:


scheme_category_label_dict = dict(zip(scheme_catogory, scheme_label))


# In[89]:


state_category_label_dict = dict(zip(state_catogory, state_label))


# In[90]:


district_category_label_dict = dict(zip(district_catogory, district_label))


# In[ ]:





# In[91]:


from sklearn.compose import ColumnTransformer
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler, FunctionTransformer
from sklearn.model_selection import train_test_split


# In[92]:


X = data.drop("sum_insured", axis=1)
y = data["sum_insured"]


# In[93]:


# X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=1000, test_size=0.2)


# In[94]:


# from sklearn.ensemble import ExtraTreesRegressor
# from sklearn.metrics import r2_score
# # Create ExtraTreesRegressor with custom parameters
# model = ExtraTreesRegressor(
#     n_estimators=200,
#     criterion='squared_error',  
#     max_depth=None,
#     min_samples_split=2,
#     min_samples_leaf=1,
#     max_features=5,
#     random_state=1000
# )
# model.fit(X, y)


# In[95]:


# import pickle as pk
# filename= 'crop_insurance_sum_Raghu.pkl'
# pk.dump(model,open(filename,'wb'))


# In[96]:


def encoding(input_data):
      input_data[0] = season_category_label_dict[input_data[0].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
      input_data[1] = scheme_category_label_dict[input_data[1].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
      input_data[2] = state_category_label_dict[input_data[2].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
      input_data[3] = district_category_label_dict[input_data[3].lower().replace(" ","").replace(" ","").replace(" ","").replace(" ","")]
      return input_data



