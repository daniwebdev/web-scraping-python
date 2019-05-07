
# coding: utf-8

# In[130]:


from bs4 import BeautifulSoup


# In[153]:


import requests
page = requests.get('http://detik.com')
soup = BeautifulSoup(page.text, "html.parser")
ul = soup.findAll("ul", {"class": 'list_fokus list_fokus_add'})
li = ul[1].findChildren("li" , recursive=False)


# In[154]:


for index, data in enumerate(li):
    item  = li[index].findAll("div", {"class": 'title_lnf'})
    text  = item[0].text
    title = text.replace("\n", "")


# In[155]:


populer = soup.findAll("div", {"id": "box-pop2"})


# In[156]:


pop_child = populer[0].findAll("li")


# In[149]:


for index, item in enumerate(pop_child):
    title = "{} - {}".format(index+1, item.find("span", {"class":"normal"}).text)
    url   = item.find("a")['href']
    print(title)
    

