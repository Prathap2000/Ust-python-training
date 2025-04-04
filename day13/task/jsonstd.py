import json
#opening json file
with open('students.json') as f:
  std = json.load(f)
#avg calculation
for s in std:
  s['avg']=sum([s['phy'],s['math'],s['chem'],s['bio']])/4
sorted_std=sorted(std,key=lambda x: x['avg'],reverse=True)
#rank arrangement based on avg
for i,s in enumerate(sorted_std,1):
  s['rank']=i
#writing into json 
with open('std-report','w')as f:
  json.dump(sorted_std,f,indent=4)
print("Report done!")