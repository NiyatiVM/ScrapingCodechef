import requests 
from bs4 import BeautifulSoup 
def ps():
  firsturl='https://www.codechef.com/problems/school'
  respone=requests.get(firsturl)
  if respone.status_code==200:
    print("Successfully opened the first web page")
    print("The problem codes are as follows :-\n")
    soupone=BeautifulSoup(respone.content,'html.parser')
    #print(soupone.prettify)
    #table=soupone.find("table").find("tbody").find('td')
    table=soupone.find_all("div",{'class':'problemname'})
    new=[]
    for t in table:
      new.append(t.find("a").get('href'))
    print(new)
  for i in new:
    url='https://www.codechef.com'+i
    resp=requests.get(url)
    if resp.status_code==200:
      print("\nSuccessfully opened the problem page\n")
      print(f"------------------------{i}-------------------------\n")
      print("The problem is as follow :-\n")
      soup=BeautifulSoup(resp.content,'html.parser')
      all=soup.find_all("div",attrs={"class":"content"})
      a=all[1].text
      b=a.replace('$','')
      b=b.replace('\le','<=').replace('\ldots','...').replace('- ','').replace("```","\n")
      print(b)
  else:
    print("Error")
ps()
