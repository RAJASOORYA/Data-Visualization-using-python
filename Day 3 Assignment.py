#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import libraries
import seaborn as sns

# load dataset
fmri = sns.load_dataset("fmri")

sns.lineplot(x="timepoint", y="signal", data=fmri);

