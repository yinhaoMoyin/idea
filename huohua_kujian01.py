# -*- coding: utf-8 -*-
#导入接口使用包
import unittest,requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


#创建类
class Test_case(unittest.TestCase):
    # s = requests.session()


 def runTest(self):
    pass


# 接口1:通过课件名称访问uuid查询接口
 def test_001(self):

   # 查询用户接口
   kid  = "EN-S1-U16-7"
   url1 = 'https://cw-00.huohuacdn.com/courseware/%s/manifest.json' % kid
   # 参数定义
   para = { "v":"1602656686679"}
   # 访问查询用户接口
   res = requests.get(url1, params=para,)
   resq01 =res.json()['stable']


   return resq01



#接口2:通过uuid查询课件结构接口
 def test_002(self, continus=None):

  uuid  = self.test_001()
  print(uuid)
  url2 =  'https://cw-00.huohuacdn.com/courseware/%s/manifest.json' % uuid
  res02 = requests.get(url2)


  #返回值中获取'blocks'.'title',并放进文件中
  for i in range(10):
    try:
     resq02 = res02.json()['blocks'][i]['title']
     self.open("%s:" % i)
     self.open(resq02+"\n")
     print(resq02)
     
    except:
        continus
  


#参数放入文件方法(路径改动下(改成自己的))
 def open(self,j):
  with open('/Users/panyinhao/PycharmProjects/idea/date/json.list', 'ab') as f:
   f.write(j)




if __name__ == '__main__':
        unittest.main()



#实现：返回值中获取all['blocks'.'title'],并放进文件中