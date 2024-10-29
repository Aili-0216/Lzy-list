from lxml import etree
import requests

url='https://www.zhipin.com/wapi/zpgeek/search/joblist.json'
url_1='https://www.zhipin.com/wapi/zpgeek/search/joblist.json'
params={
'scene': 1,
'query': '数据',
'city': 101240100,
'experience':'',
'payType':'',
'partTime':'',
'degree':'',
'industry':'',
'scale': '',
'stage':'' ,
'position':'' ,
'jobType': '',
'salary':'',
'multiBusinessDistrict':'',
'multiSubway':'',
'page':1,
'pageSize':30
}
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'referer':'https://www.zhipin.com/web/geek/job?query=%E6%95%B0%E6%8D%AE',
    'cookie':'fid=0f7222c9098b513132449df526ab9e62; lastCity=101240100; ab_guid=969593ed-d121-4e08-b92f-4ab284380f48; __g=-; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E6%2595%25B0%25E6%258D%25AE&r=&g=&s=3&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1729848667,1729865339; HMACCOUNT=FBEBF84315FC8153; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1729865540; __zp_stoken__=8c4afw4RWPAY0EF8PWxpOYXZEwoPCt1bCvnprdsKmX3Jdw4lqwqxdVVNbwrXCtcOKwq%2FCvsKqwrDCvVHDgFDDu0vCm1DDv1%2FEgMKtw7vCnsKdxJbDs3HEsEfCj8K%2BwqlAJxAOEgUOEA4SBQ4aBAsQDwUPCxAPExENGhE7MsSCwqnCqzVIPzUsT0VZC1BoV1JoTBJpUUQ%2BNBgSYlQ0JEI1PkDCtELDgg7Dij7CtQXCtEDDiWI1NkA%2BwrTCiDkywr9iEcK%2Bw4gawrvCjy3DgMO3BkMaw5BVLcKeworCtcWDLjdIw4DEvT9AHEo%2FOz4%2FNTY7QCw1ccOSXjHCn8KKwrQkL0AfQ0A%2FPkk7QD88P0kkP0jCiDFAPjA7BREYBgYkQ8OKwrTCvsOqQD8%3D; __c=1729865338; __a=63267823.1729848660.1729865127.1729865338.13.3.5.13'
}
res=requests.get(url_1,params=params,headers=headers)
res.encoding=res.apparent_encoding
res_txt=res.json()
print(res_txt)
res.close()
