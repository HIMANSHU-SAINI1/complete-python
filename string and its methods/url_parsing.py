url=input("enter the url")
protocol=url[ :url.find(':')]
dot1=url.find('.')
dot2=url.find('.',dot1+1)
domain=url[dot1+1:dot2]
page=url[url.rfind('/'):]
print(protocol)
print(domain)
print(page)