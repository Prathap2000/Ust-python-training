#step1 
#read the csv 
path =r"C:\Users\Administrator\Desktop\python training\case\students.csv"
filedata=open(path,'r')
data=filedata.readlines()
print(data)
filedata.close()



class_dict = {}
columns = [item.strip() for item in data[0].split(',')] # Keys of the student dictionary
for dataitem in data[1:]:
    values = [item.strip() for item in dataitem.split(',')] # Values for the student dictionary
    student_dict = dict(zip(columns, values)) # Zipping keys and values to form the student dictionary
    class_dict[student_dict['regid']] = student_dict # Adding student dictionery to class dictionary


print("\n" + "-"*100)
# print("INFO -> step 2 \n", class_dict)

# Step 3
# Calculate the average
grade_col=['math','english','science']
for student_id,student_data in class_dict.items():
    grades=[int(student_data[col]) for col in grade_col if col in student_data]
    if grades:
        avg=sum(grades)/len(grades)
        student_data['avg']=avg
    else:
        student_data['avg']=None

print("\n" + "-"*100)
print("INFO -> step 3 -> Class dictionary after averages updated\n", class_dict)

# Step 4
# Calculate the rank
sorted_std=sorted(class_dict.values(),key=lambda x:x.get('avg',0), reverse=True)
for rank,student in enumerate(sorted_std,start=1):
    student['rank']=rank
class_dict={student['regid']:student for student in sorted_std}

print("\n" + "-"*100)
# print("INFO -> step 4 -> Class dictionary after ranks updated\n", class_dict)
