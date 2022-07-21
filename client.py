import xmlrpc.client 

s = xmlrpc.client.ServerProxy('http://localhost:8000')
while(1):
    n = int(input("Enter a number  "))
    print("The factorial of",n ,"is {}".format(s.fact(n)))