from operator import gt
class time(object):
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
    def __add__(self,other):
        return((self.h+other.h),(self.m+other.m),(self.s+other.s))
    def __gt__(self,other):
        return ((self.h>other.h),(self.m >other.m),(self.s>other.s))
    def __str__(self):
        return ':'.join([str(self.h),str(self.m),str(self.s)])
t=time(10,30,30)
t
