import pandas as pd 
import matplotlib.pyplot as plt  

import chardet # Cause the encodeing of read_csv file was different 

with open("top10s.csv", 'rb') as file:  #Encoding procedure 
    result = chardet.detect(file.read(10000)) 
print(result)  

df = pd.read_csv("E:\\Spotify songs data analytics\\top10s.csv", encoding=result['encoding'])   

print(df.head())

df.info()

# Check missing values 
print("Total missing values in DataFrame:", df.isna().sum().sum())

# Check for duplicate rows and remove them if needed:
num_duplicates = df.duplicated().sum()
print("Number of duplicate rows:", num_duplicates)
if num_duplicates > 0:
    df = df.drop_duplicates()

print("Columns in the dataset:", df.columns.tolist())  # To know the columns names

top_song_indexes = df.groupby("year")["pop"].idxmax()  #Group data by years and popularity. 

top_songs_by_year = df.loc[top_song_indexes]
print(top_songs_by_year[['year', 'title', 'artist', 'pop']])


# Plotting
plt.figure(figsize=(8, 5))

plt.bar(top_songs_by_year['year'].astype(str), top_songs_by_year['pop'], color='skyblue')
plt.xlabel("Year")
plt.ylabel("Popularity")
plt.title("Top Spotify Song Popularity by Year (2010-2019)")
plt.show()   

#Trend analysis overtime

yearly_avg = df.groupby("year")[['bpm', 'nrgy', 'dnce', 'dB', 'live', 'val', 'dur', 'acous', 'spch', 'pop']].mean()

plt.figure(figsize=(10, 6))

# Loop over each audio feature and plot its average value over the years.
for feature in yearly_avg.columns:
    plt.plot(yearly_avg.index, yearly_avg[feature], marker='o', label=feature)

plt.xlabel("Year")
plt.ylabel("Average Value")
plt.title("Average Audio Features by Year")

plt.legend(title="Audio Feature")
plt.tight_layout()
plt.show()

#Genre analysis 

genre_counts = df['top genre'].value_counts()

plt.figure(figsize=(12, 6))

plt.bar(genre_counts.index, genre_counts.values, color='skyblue')

plt.xlabel("Genre")
plt.ylabel("Count")
plt.title("Number of Top Songs by Genre")

#Rotating for better visibility 
plt.xticks(rotation=90)
plt.tight_layout()
plt.show() 
