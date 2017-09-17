##首先定义一个人先
import sys
class person:
      ##获取参数，例如是名字，年龄
      def __init__(self):
          var =  sys.argv
          if var[1]:
              print("你的特工名字叫%s" %(var[1]))

          else:
              print("你默认的名字就叫做占士邦")
      def name(self):
          print('xx')


james = person()