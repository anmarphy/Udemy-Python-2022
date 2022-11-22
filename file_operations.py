#!/usr/bin/env python
# coding: utf-8

# In[1]:


def save_file(content, file_name):
    with open(file_name, 'w') as file:
        file.write(content)


# In[2]:


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()


# In[ ]:




