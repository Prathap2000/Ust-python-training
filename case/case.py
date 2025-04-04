path=r'C:\Users\Administrator\Desktop\python training\case\students.csv'
csvf=open(path,"r")
data=csvf.readlines()
# print(data)
csvf.close()

class_dict={}
columns = [item.strip() for item in data[0].split(',')]
# print(columns)
for dataitem in data[1:]:
    values=[item.strip() for item in dataitem.split(',')]
    student_dict = dict(zip(columns, values))
    class_dict[student_dict['regid']]=student_dict
# print(class_dict)
#avg
grade_col=['phy','chem','math','bio']
for sutdent_id,student_data in class_dict.items():
    grades=[int(student_data[col]) for col in grade_col if col in student_data]
    # print(grades)
    if grades:
        avg=sum(grades)/len(grades)
        student_data['avg']=avg
    else:
        student_data['avg']=None
# print(class_dict)

#rank
student_rank=sorted(class_dict.values(),key=lambda x:x.get('avg',0),reverse=True)
for rank,student in enumerate(student_rank,start=1):
    student['rank']=rank
# print(student_rank)
class_dict={student['regid']: student for student in student_rank}
print(class_dict)

#display the reposrt
template = "{0:8} | {1:15} | {2:5} | {3:5} | {4:5} | {5:5} | {6:5} | {7:5} | {8:5}"
line = '-'*90

print("\nCLASS REPORT")
print(line)
print(template.format('REGID', 'NAME', 'AGE', 'PHY', 'CHEM', 'MATH', 'BIO', 'AVG', 'RANK'))
print(line)
for regid in class_dict.keys():
    name = class_dict[regid]['name']
    id = class_dict[regid]['regid']
    age = class_dict[regid]['age']
    phy = class_dict[regid]['phy']
    chem = class_dict[regid]['chem']
    math = class_dict[regid]['math']
    bio = class_dict[regid]['bio']
    avg = class_dict[regid]['avg']
    rank = class_dict[regid]['rank']
    print(template.format(id, name, age, phy, chem, math, bio, avg, rank))
  