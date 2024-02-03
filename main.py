# Answer 1

import pandas as pd
import matplotlib.pyplot as plt


file_name_prefix = "tennis_wta-master/wta_matches_"
no_of_usa_winners = {}

for i in range(1968,2024):
    file_name = file_name_prefix + str(i) + '.csv'
    
    df = pd.read_csv(file_name)
    no_of_usa_winners[i] = len(df[df['winner_ioc'] == 'USA'])

print(no_of_usa_winners)


# Answer 1

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name_prefix = "tennis_wta-master/wta_matches_"
no_of_usa_winners = {}


age_data = pd.DataFrame()
for i in range(1968,2024):
    file_name = file_name_prefix + str(i) + '.csv'
    
    df = pd.read_csv(file_name)
    winner_age = df['winner_age']
    loser_age = df['loser_age']
    age_data_temp = pd.DataFrame({'Winner Age': winner_age, 'Loser Age': loser_age})
    age_data = pd.concat([age_data, age_data_temp], ignore_index=True)
    # print(i,len(age_data))
    
# Plot the violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=age_data, inner='quartile', palette='pastel')
plt.title('Age Distribution of Winners and Losers in Tennis Matches [1968 - 2013]')
plt.ylabel('Age')
plt.show()


# Answer 2.1

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict, Counter

file_name_prefix = "tennis_wta-master/wta_matches_"
# file_name_prefix = "tennis_wta-master/wta_matches_qual_itf_"
country_winners = defaultdict(dict)

for i in range(1968,2024):
    file_name = file_name_prefix + str(i) + '.csv'
    
    df = pd.read_csv(file_name)
    country_winners[i] = Counter(df['winner_ioc'])

df = pd.DataFrame(country_winners).transpose()
df = df[['USA','RUS','CHN','FRA','AUS','GBR']]
# print(df)
df.plot(kind="bar", stacked=True)
plt.xlabel('Year')
plt.ylabel('Number of Winners')
plt.title('Winner Distribution of 6 countries with Year')
plt.legend(title='Country', loc='upper right')
plt.show()



# Answer 2.2

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name_prefix = "tennis_wta-master/wta_matches_"
# file_name_prefix = "tennis_wta-master/wta_matches_qual_itf_"

combine_df = pd.DataFrame()

for i in range(1968, 2024):

    file_name = file_name_prefix + str(i) + '.csv'    
    df = pd.read_csv(file_name)
    year_df = df[['winner_age']]
    year_df['year'] = i
    combine_df = pd.concat([combine_df,year_df], ignore_index=True)

# print(combine_df)
box_plot = combine_df.boxplot(column='winner_age', by='year', figsize=(15, 8),patch_artist=True)
    
plt.title('Winner Age Distribution by Year')
plt.xlabel('Year')
plt.ylabel('Winner Age')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




# Answer 2.3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pywaffle import Waffle
from collections  import Counter

file_name = "tennis_wta-master/wta_matches_2023.csv"    
df = pd.read_csv(file_name)
dic = Counter(df['winner_ioc'])
length = 0
for key in dic:
    length += dic[key]

new_dic = {}
for key in dic:
    dic[key] = round((dic[key]/length)*100)
    if dic[key] != 0:
        new_dic[key] = dic[key]


fig = plt.figure(
    FigureClass=Waffle,
    rows=10,
    columns=10,  
    values= new_dic,
    legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)},
    cmap_name = 'tab20',
    facecolor = 'whitesmoke',
    title = {"label": "Age distribution at daycare", "loc": "Center", "size": 15}, 
    # icons = 'child',
    figsize = (15, 12),
    vertical=False
)
plt.title('Waffle plot of distribution of winner counties in year 2023')
plt.show()

    
# Answer 3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
file_name_prefix = "tennis_wta-master/wta_matches_"
# file_name_prefix = "tennis_wta-master/wta_matches_qual_itf_"

heights_range = [130,135,140,145,150,155,160,165,170,175,180,185,190,195,200]
ages_range = [0,5,10,15,20,25,30,35,40,45,50,55,60,65]
height_range_count = len(heights_range) - 1
age_range_count = len(ages_range) - 1
matrix = np.zeros((height_range_count, age_range_count), dtype=int)

for i in range(1968, 2024):

    file_name = file_name_prefix + str(i) + '.csv'    
    df = pd.read_csv(file_name)
    for index, row in df.iterrows():
        height = row['winner_ht']
        age = row['winner_age']
        height_range = sum(height >= bin_value for bin_value in heights_range) - 1
        age_range = sum(age >= bin_value for bin_value in ages_range) - 1
        matrix[-height_range][age_range] += 1
   
print(matrix[3:])
plt.imshow(matrix[3:], cmap='cividis', aspect='auto')
plt.xticks(range(len(ages_range) - 1), [f'{ages_range[i]}-{ages_range[i + 1]}' for i in range(len(ages_range) - 1)])
plt.yticks(range(len(heights_range) - 1), [f'{heights_range[i]}-{heights_range[i + 1]}' for i in range(len(heights_range) - 1)])
plt.colorbar(label='Winners Count')
plt.xlabel('Age Range')
plt.ylabel('Height Range')
plt.title('Heatmap of Winnners Counts based on Age and Height Ranges')
plt.show()


# Answer 5

import pandas as pd
import matplotlib.pyplot as plt
from collections  import Counter

file_name = "tennis_wta-master/wta_matches_2023.csv"    
df = pd.read_csv(file_name)
dic = Counter(df['winner_hand'])
length = 0
for key in dic:
    length += dic[key]

# print(dic)

plt.pie(dic.values(), labels=dic.keys(), autopct='%1.1f%%', startangle=140)
plt.title("Pie plot of distribution of winner's hand in year 2023")
plt.show()


# Answer 7

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import LabelEncoder

file_name_prefix = "tennis_wta-master/wta_matches_"
# file_name_prefix = "tennis_wta-master/wta_matches_qual_itf_"

combine_df = pd.DataFrame()

for i in range(2020, 2024):

    file_name = file_name_prefix + str(i) + '.csv'    
    df = pd.read_csv(file_name)
    year_df = df[['winner_ioc', 'surface', 'winner_hand']]
    year_df.loc[:,('year')] = i
    combine_df = pd.concat([combine_df,year_df], ignore_index=True)

print(combine_df)

label_encoder1 = LabelEncoder()
label_encoder2= LabelEncoder()
label_encoder3= LabelEncoder()
label_encoder4 = LabelEncoder()
combine_df["year_encoded"] = label_encoder1.fit_transform(combine_df["year"])
combine_df["winner_country_encoded"] = label_encoder2.fit_transform(combine_df["winner_ioc"])
combine_df["surface_encoded"] = label_encoder3.fit_transform(combine_df["surface"])
combine_df["hand_encoded"] = label_encoder4.fit_transform(combine_df["winner_hand"])

print(combine_df)

fig = px.parallel_coordinates(combine_df,
                              dimensions=['year_encoded', 'winner_country_encoded','surface_encoded','hand_encoded'],
                              color="year_encoded",
                              labels={"surface_encoded": "Surface", "winner_country_encoded": "Winner Country", "year": "Year", "hand_encoded": "Hand"},
                              color_continuous_midpoint=0,
                              title="Parallel Coordinate Plot showing distribution of winner country, winner hand and surface for year 2020 to year 2023")

fig.show()

# year_legend = []
# for i in range(0,4):
#     year_legend.append((i,label_encoder1.classes_[i]))
# print('\n',year_legend)

# country_legend = []
# for i in range(1,73):
#     country_legend.append((i,label_encoder2.classes_[i]))
# print('\n',country_legend)

# surface_legend = []
# for i in range(0,3):
#     surface_legend.append((i,label_encoder3.classes_[i]))
# print('\n',surface_legend)

# hand_legend = []
# for i in range(0,3):
#     hand_legend.append((i,label_encoder4.classes_[i]))
# print('\n',hand_legend)


# Answer 2.3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

file_name_prefix = "tennis_wta-master/wta_matches_"
# file_name_prefix = "tennis_wta-master/wta_matches_qual_itf_"

years = []
R_hand = []
L_hand = []
for i in range(1968, 2024):

    file_name = file_name_prefix + str(i) + '.csv'    
    df = pd.read_csv(file_name)
    # year_hand[i] = Counter(df['winner_hand'])
    years.append(i)
    R_hand.append(Counter(df['winner_hand'])['R'])
    L_hand.append(Counter(df['winner_hand'])['L'])

# print(years, R_hand,L_hand)    

fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(years, [-count for count in L_hand], color='blue', label='Left Hand')
ax.barh(years, R_hand, color='orange', label='Right Hand')
ax.set_xlabel('Count')
ax.set_ylabel('Year')
ax.set_yticks(years)
ax.set_title('Population Pyramid-like Plot of Left and Right Hand Data (1968-2023)')
ax.legend()
plt.show()


# Answer 4

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name_prefix = "tennis_wta-master/wta_matches_"
no_of_usa_winners = {}


age_data = pd.DataFrame()
for i in range(2023,2024):
    file_name = file_name_prefix + str(i) + '.csv'
    
    df = pd.read_csv(file_name)
    winner_age = df['winner_age']
    age_data_temp = pd.DataFrame({'Winner_Age': winner_age})
    age_data = pd.concat([age_data, age_data_temp], ignore_index=True)

print(age_data)  

plt.figure(figsize=(8, 6))
sns.swarmplot(data=age_data, palette='pastel', dodge=True)

# Add labels and title
plt.xlabel("Winner's Age")
plt.ylabel('Age')
plt.title('Beeswarm Chart - Distribution of Winner Ages')

# Show the plot
plt.show()




import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import LabelEncoder

file_name_prefix = "tennis_wta-master/wta_matches_"
# file_name_prefix = "tennis_wta-master/wta_matches_qual_itf_"

combine_df = pd.DataFrame()

for i in range(2020, 2024):

    file_name = file_name_prefix + str(i) + '.csv'    
    df = pd.read_csv(file_name)
    year_df = df[['winner_ht', 'draw_size', 'surface']]
    year_df.loc[:,('year')] = i
    combine_df = pd.concat([combine_df,year_df], ignore_index=True)

print(combine_df)

label_encoder1 = LabelEncoder()
combine_df["surface_encoded"] = label_encoder1.fit_transform(combine_df["surface"])


print(combine_df)

fig = px.parallel_coordinates(combine_df,
                              dimensions=['surface_encoded', 'winner_ht', 'year','draw_size'],
                              color="surface_encoded",
                              labels={"surface_encoded": "Surface", "winner_ht": "Winner Height", "year": "Year", "draw_size": "Draw Size"},
                              color_continuous_midpoint=0,
                              title="Parallel Coordinate Plot showing distribution of winner country, winner hand and surface for year 2020 to year 2023")

fig.show()

surface_legend = []
for i in range(0,3):
    surface_legend.append((i,label_encoder1.classes_[i]))
print('\n',surface_legend)
