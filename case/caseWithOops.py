class student(object):
    def __init__(self,name,regid):
        self.name=name
        self.regid=regid
        self.details={'age':0}
        self.marks={'physis':0,'chemistry':0,"maths":0,"biology":0}
        self.average=0
        self.rank=0
    def __repr__(self):
        return str(self.name),str(self.regid)
    def calculate_average(self):
        self.average=sum(self.marks.values())/len(self.marks.values())
    def set_rank(self,rank):
        self.rank=rank
    def set_marks(self,subj,marks):
        pass
    def get_marks(self):
        return self.marks
    def __str__(self):
        return ','.join([str(self.name),str(self.age),str(self.regid),'.'.join(self.marks.values()),\
                          str(self.average)]
        
if __name__=="__main__":
    s=student("prathap",25)
    s.set_marks(phy=90,chem=80,math=98,bio=7)

    