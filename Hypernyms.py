#!/usr/bin/env python
# coding: utf-8

# In[79]:


import nltk


# In[77]:


import wordnet


# In[80]:


from nltk.corpus import wordnet


# In[93]:


for synset in wordnet.synsets('green'):
   for hypernym in synset.hypernyms():
       print(synset, hypernym)


# In[82]:



for synset in wordnet.synsets('vibration'):
  for hypernym in synset.hypernyms():
      print(synset, hypernym)


# In[15]:





# In[20]:


nltk.download('wordnet')


# In[21]:





# In[23]:


for synset in wordnet.synsets('green'):
   for hypernym in synset.hypernyms():
       print( hypernym)


# In[24]:


for synset in wordnet.synsets('vibration'):
   for hypernym in synset.hypernyms():
       print( hypernym)


# In[25]:





# In[83]:


wordnet.synsets('vibration')


# In[86]:


wordnet.synsets('marriage')


# In[103]:


v = wordnet.synsets('vibration')[0]


# In[104]:


m=wordnet.synsets('marriage')[0]


# In[101]:



wordnet.synsets('marriage')[0].definition()


# In[102]:


wordnet.synsets('vibration')[0].definition()


# In[106]:


m.lowest_common_hypernyms(v)


# In[105]:


v.lowest_common_hypernyms(m)


# In[36]:





# In[37]:





# In[94]:


syn = wordnet.synsets('vibration')[0] 


# In[39]:


syn.hypernyms()


# In[40]:


syn.hypernyms()[0]


# In[44]:


wordnet.synsets('vibration')


# In[51]:





# In[63]:





# In[61]:





# In[57]:





# In[65]:


for synset in wordnet.synsets('vibration'):
   for hypernym in synset.hypernyms():
       print(hypernym)


# In[95]:


dog = wordnet.synsets('dog')[0]
cat = wordnet.synsets('cat')[0]


# In[67]:


cat = wordnet.synsets('mar')[0]


# In[107]:


dog = wordnet.synsets('dog')[0]


# In[108]:


cat= wordnet.synsets('cat')[0]


# In[72]:





# In[109]:


dog.lowest_common_hypernyms(cat)


# In[ ]:




