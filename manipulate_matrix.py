import pandas as pd
dep_data = pd.read_csv('user_status_match_dep.csv')
dep = pd.read_csv('dep.csv')

#rename columns
dep_data.columns = ['drop','userid','time','status','drop2']


#merge tables
result = pd.merge(dep_data, dep, how='outer', left_on = 'userid', right_on = 'userid')

#drop and select columns
result2 = result.drop(['drop','drop2'], 1)
result2.head()

result3 = result2 [['userid','time','status']]

# sort 
sort_time = result3.sort_values(by=['userid','time'])

#drop NA
result4 = result3.dropna()

#add frequency column
result4['freq'] = result4.groupby('userid')['userid'].transform('count')

#select user status >30

df.loc[df['A'] == 'foo']