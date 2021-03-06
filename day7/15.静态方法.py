#liuhao
import time
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    @staticmethod   #静态方法
    def now():
        t=time.localtime()
        return Date(t.tm_year,t.tm_mon,t.tm_mday)
    '''打印：
            <__main__.Date object at 0x0000022298A754A8>'''
    @classmethod #改成类方法
    def class_now(cls):
        t=time.localtime()
        return cls(t.tm_year,t.tm_mon,t.tm_mday) #哪个类来调用,即用哪个类cls来实例化
    '''
    输出结果:
    year:2017 month:3 day:3
    '''
class EuroDate(Date):
    def __str__(self):
        return 'year:%s month:%s day:%s' %(self.year,self.month,self.day)

e=EuroDate.now()
print(e) #我们的意图是想触发EuroDate.__str__,此时e就是由EuroDate产生的,所以会如我们所愿
print(EuroDate.class_now())
print(Date.now())