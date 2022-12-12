import pandas as pd
df = pd.read_csv('./answer.csv') #อ่านไฟล์csv
group = list(set(df['รถที่ใช้ในการเดินทาง'])) 

data_female = {}
data_male = {}
count_female = []
count_male = []

data_509 = {}
data_5010 = {}
data_5011 = {}
count_509 = []
count_5010 = []
count_5011 = []

for x in group:
  data_female[x] = 0
  data_male[x] = 0

  data_509[x] = 0
  data_5010[x] = 0
  data_5011[x] = 0


for x in range(len(df['รถที่ใช้ในการเดินทาง'])):
  if df['เพศ'][x] == 'หญิง':
    data_female[df['รถที่ใช้ในการเดินทาง'][x]] += 1
  if df['เพศ'][x] == 'ชาย':
    data_male[df['รถที่ใช้ในการเดินทาง'][x]] += 1

  if df['ระดับชั้น'][x] == '5/9':
    data_509[df['รถที่ใช้ในการเดินทาง'][x]] += 1
  if df['ระดับชั้น'][x] == '5/10':
    data_5010[df['รถที่ใช้ในการเดินทาง'][x]] += 1
  if df['ระดับชั้น'][x] == '5/11':
    data_5011[df['รถที่ใช้ในการเดินทาง'][x]] += 1

for n in group:
  count_male.append(data_male[n])
  count_female.append(data_female[n])
  count_509.append(data_509[n])
  count_5010.append(data_5010[n])
  count_5011.append(data_5011[n])

graph = pd.DataFrame({'Male':count_male,'Female':count_female},index=group)
graph.plot(kind="bar", color=['gold', 'tomato',],title="Questionnaire",fontsize='10',rot=0) 

graph_class = pd.DataFrame({'5/9':count_509,'5/10':count_5010,'5/11':count_5011},index=group)
graph_class.plot(kind="bar", color=['blue','aqua','lightblue'],title="Questionnaire",fontsize='10',rot=0)