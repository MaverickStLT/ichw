#1700011605 李韬
def exchange(currency_from, currency_to, amount_from):
    w='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from
    return (w)
#将输入的货币与数量合并为网站并输出#
    

def dec(web):
    from urllib.request import urlopen
    doc = urlopen(web)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return (jstr)
#从Cornell网站里面获取汇率转换结果#

def numb(string):
    l=len(string)
    num=''
    nu=0
    for i in range(l):
        if ord(string[i])>=48 and ord(string[i])<=57:
            p=i
            while (ord(string[p])>=48 and ord(string[p])<=57) or string[p]=='.':
                p=p+1
            break
#把第一个数字（原货币）跳过去，防止其干扰第二个数字（目标货币）的提取#
    for i in range (p,l):
        if (ord(string[i])>=48 and ord(string[i])<=57) or string[i]=='.':
            num=num+string[i]
    return (num)
#选出第二个数字，并且输出#

def test_exchange():
    assert('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5' == exchange('USD','EUR','2.5'))
    assert('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=CNY&amt=1' == exchange('USD','CNY','1'))
    assert('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=CNY&to=VND&amt=100' == exchange('CNY','VND','100'))
    
def test_dec():
    assert('{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }' == dec('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5'))
    assert('{ "from" : "1 United States Dollar", "to" : "6.52615 Chinese Yuan", "success" : true, "error" : "" }' == dec('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=CNY&amt=1'))
    assert('{ "from" : "100 Chinese Yuan", "to" : "348331.16866759 Vietnamese Dong", "success" : true, "error" : "" }' == dec('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=CNY&to=VND&amt=100'))
    
def test_numb():
    assert('2.0952375' == numb('{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }'))
    assert('6.52615' == numb('{ "from" : "1 United States Dollar", "to" : "6.52615 Chinese Yuan", "success" : true, "error" : "" }'))
    assert('348331.16866759' == numb('{ "from" : "100 Chinese Yuan", "to" : "348331.16866759 Vietnamese Dong", "success" : true, "error" : "" }'))
#对三个函数进行分别测试#

def testAll():
    test_exchange()
    test_dec()
    test_numb()
    print("All tests passed")
#对三个函数同时进行测试#

testAll()
a=input('currency from ')
b=input('currency to ')
c=input('amount from ')
#输入相关货币以及数量#
w=exchange(a,b,c)
s=dec(w)
print (numb(s))
#程序运行主体#
