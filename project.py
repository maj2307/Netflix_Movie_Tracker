# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 12:21:59 2019

@author: a_ari
"""
#File: project.py
#Author: 
#Ashlynn Droddy
#ALexander Arias
#Micaleb Johnson
#Date: 05/01/2019
#E-mail: 
#ashlynnmarieee@tamu.edu
#ada180829@tamu.edu
#maj2307@tamu.edu
#Description: open netflix csv file and find certain statistics 

#part 1#########################################################################################################################
#import csv and read file
import csv
f = open('2016_movie_data.csv', encoding='utf8', errors='ignore')
reader = csv.reader(f)
    
#create empty list 
movie = []
release_date = []
distributor = []
genre = []
mpaa = []
tickets_sold = []
file = []

for row in reader:
    #append to empty list
    movie.append(row[0])
    release_date.append(row[1])
    distributor.append(row[2])
    genre.append(row[3])
    mpaa.append(row[4])
    tickets_sold.append(row[5])
    file.append(row)
        
#split date
new_file = []
for i in file:
    x = i[1].split('/')
    i.remove(i[1])
    i.insert(1, x)
    new_file.append(i)

#close file    
f.close()

#remove header rows
new_file = new_file[1::]
movie = movie[1::]
release_date = release_date[1::]
distributor = distributor[1::]
genre = genre[1::]
mpaa = mpaa[1::]
tickets_sold = tickets_sold[1::]
   
#create empty sets
distinct_genres = set()
distinct_mpaa = set()
distinct_distributor = set()

#find distinct genre, mpaa, and distributors
for i in genre:
    distinct_genres.add(i)
for i in mpaa:
    distinct_mpaa.add(i)   
for i in distributor:
    distinct_distributor.add(i)   
    
#find total number of tickets
total_tickets_sold = 0
for i in tickets_sold:
    x = i.replace(',', '')
    total_tickets_sold += int(x)
        
#print statements
print('========Dataset details========')
print()
print('Number of Movies:', len(movie) )
print('Number of different genres:', len(distinct_genres))
print('Number of different MPAA:', len(distinct_mpaa))
print('Number of different distributors:', len(distinct_distributor))
print('Total Number of Tickets Sold:', total_tickets_sold)
print()
print('===============================')
      
#part 2#####################################################################################################################

#create months dictionary
months = { 'January':0, 'February':0, 'March':0 , 'April':0, 'May':0, 'June':0, 'July':0,'August':0,'September':0, 'October':0 , 'November':0 , 'December':0}

#import modules
import matplotlib.pyplot as plot   
  
#find how time a movie was released in each month
for a in range(len(movie)):
    if release_date[a][0:2:1] == '10':
        months['October'] += 1
    if release_date[a][0:2:1] == '11':
	    months['November'] +=1
    if release_date[a][0:2:1] == '12':
	    months['December'] +=1   	 
    if release_date[a][0:2:1] == '1/':
	    months['January'] +=1
    if release_date[a][0:2:1] == '2/':
	    months['February'] +=1
    if release_date[a][0:2:1] == '3/':
	    months['March'] +=1
    if release_date[a][0:2:1] == '4/':
	    months['April'] +=1
    if release_date[a][0:2:1] == '5/':
	    months['May'] +=1
    if release_date[a][0:2:1] == '6/':
	    months['June'] +=1
    if release_date[a][0:2:1] == '7/':
	    months['July'] +=1  
    if release_date[a][0:2:1] == '8/':
	    months['August'] +=1
    if release_date[a][0:2:1] == '9/':
	    months['September'] += 1

#find max value
max_movies = 0
for i,j in months.items():
    if j > max_movies:
        max_movies = j
        
#find corresponding month
key_list = list(months.keys())
val_list = list(months.values())
max_month = (key_list[val_list.index(max_movies)])

#print statements
print()
print('Most number of movies (' + str(max_movies) + ') released in', str(max_month)+'.')

#create empty list for each month
jan_tickets = []
feb_tickets = []
mar_tickets = []
apr_tickets = []
may_tickets = []
jun_tickets = []
jul_tickets = []
aug_tickets = []
sep_tickets = []
oct_tickets = []
nov_tickets = []
dec_tickets = []

#Find how many tickets each month sold
for i in new_file:
    if i[1][0] == '1':
        jan_tickets.append(i[5])
    elif i[1][0] == '2':
        feb_tickets.append(i[5])
    elif i[1][0] == '3':
        mar_tickets.append(i[5])
    elif i[1][0] == '4':
        apr_tickets.append(i[5])
    elif i[1][0] == '5':
        may_tickets.append(i[5])
    elif i[1][0] == '6':
        jun_tickets.append(i[5])
    elif i[1][0] == '7':
        jul_tickets.append(i[5])
    elif i[1][0] == '8':
        aug_tickets.append(i[5])
    elif i[1][0] == '9':
        sep_tickets.append(i[5])
    elif i[1][0] == '10':
        oct_tickets.append(i[5])
    elif i[1][0] == '11':
        nov_tickets.append(i[5])
    elif i[1][0] == '12':
        dec_tickets.append(i[5])

#create dictionary for list
months2 = { 'January':0, 'February':0, 'March':0 , 'April':0, 'May':0, 'June':0, 'July':0,'August':0,'September':0, 'October':0 , 'November':0 , 'December':0}

#function for adding total tickets for each month
def total_tickets_month(x):
    #parameter x is a list of string numbers
    total_tickets_sold = 0
    for i in x:
        x = i.replace(',', '')
        total_tickets_sold += int(x)
    return total_tickets_sold

#assign totals to dictionary
months2['January'] = total_tickets_month(jan_tickets)
months2['February'] = total_tickets_month(feb_tickets)
months2['March'] = total_tickets_month(mar_tickets)
months2['April'] = total_tickets_month(apr_tickets)
months2['May'] = total_tickets_month(may_tickets)
months2['June'] = total_tickets_month(jun_tickets)
months2['July'] = total_tickets_month(jul_tickets)
months2['August'] = total_tickets_month(aug_tickets)
months2['September'] = total_tickets_month(sep_tickets)
months2['October'] = total_tickets_month(oct_tickets)
months2['November'] = total_tickets_month(nov_tickets)
months2['December'] = total_tickets_month(dec_tickets)

#find max value
max_tickets = 0
for i,j in months2.items():
    if j > max_tickets:
        max_tickets = j

#find corresponding month
key_list = list(months2.keys())
val_list = list(months2.values())
max_month = (key_list[val_list.index(max_tickets)])

print('Most amount of tickets sold (' + str(max_tickets) + ') in', str(max_month)+'.')
print()
print('===============================')
print()

#part 3######################################################################
    
print('========Tickets sold by distributors========')
print()

#create dictionary with every distinct distributor
distributors = {}
for i in distinct_distributor:
        distributors[i] = 0
        
#add total tickets
for i in new_file:
    distributors[i[2]] += int(i[5].replace(',', ''))

#create another dictionary
distributors2 = {}
for i in distinct_distributor:
        distributors2[i] = 0

#add percentage
for i,j in distributors.items():
    distributors2[i] = ((j/total_tickets_sold) * 100)

#create an other group if less than 1 percent
percent_d = { 'Others' : 0}
for i,j in  distributors2.items():
    if j < 1:
        percent_d['Others'] += j
    else:
        percent_d[i] = j
        
#create list of values of percent_d to order 
val_list = list(percent_d.values())
val_list.sort()
val_list.reverse()

#dreate function to get corresponding keys
def get_key(val):
    #parametr val is a value in dictionary
    for key, value in percent_d.items():
        if val == value:
            return key
        
#print in order
for i in val_list:
    print(get_key(i), ':', str(round(i, 2))+'%')
print()
print('==================')

# Data to plot
labels = list(percent_d.keys())
sizes = list(percent_d.values())

#create function to count genre in specified month
def month_genres(x, month):
    #function to count genre in a specified month
    #parameter x is a dictionary {'Drama':0, 'Horror' : 0, 'Action':0, 'Comedy':0}
    #parameter month is a int 1-12 corresponding to month
    for i in new_file:
        if i[1][0] == month:
            if i[3] == 'Drama':
                x['Drama'] += 1
            elif i[3] == 'Horror':
                x['Horror'] += 1
            elif i[3] == 'Action':
                x['Action'] += 1
            elif i[3] == 'Comedy':
                x['Comedy'] += 1
    return x

#create dictionaries for each month
genres_jan = {'Drama':0, 'Horror' : 0, 'Action':0, 'Comedy':0}
genres_feb = {'Drama':0, 'Horror' : 0, 'Action':0, 'Comedy':0}
genres_mar = {'Drama':0, 'Horror' : 0, 'Action':0, 'Comedy':0}
genres_apr = {'Drama':0, 'Horror' : 0, 'Action':0, 'Comedy':0}
genres_may = {'Drama':0, 'Horror' : 0, 'Action':0, 'Comedy':0}
genres_jun = {'Drama':0, 'Horror' : 0, 'Action':0, 'Comedy':0}
genres_jul = {'Drama':0, 'Horror' : 0, 'Action':0, 'Comedy':0}
genres_aug = {'Drama':0, 'Horror' : 0, 'Action':0, 'Comedy':0}
genres_sep = {'Drama':0, 'Horror' : 0, 'Action':0, 'Comedy':0}
genres_oct = {'Drama':0, 'Horror' : 0, 'Action':0, 'Comedy':0}
genres_nov = {'Drama':0, 'Horror' : 0, 'Action':0, 'Comedy':0}
genres_dec = {'Drama':0, 'Horror' : 0, 'Action':0, 'Comedy':0}

#find the amount of each genre in each month
jan = month_genres(genres_jan, '1')
feb = month_genres(genres_feb, '2')
mar = month_genres(genres_mar, '3')
apr = month_genres(genres_apr, '4')
may = month_genres(genres_may, '5')
jun = month_genres(genres_jun, '6')
jul = month_genres(genres_jul, '7')
aug = month_genres(genres_aug, '8')
sep = month_genres(genres_sep, '9')
octo = month_genres(genres_oct, '10')
nov = month_genres(genres_nov, '11')
dec = month_genres(genres_dec, '12')

#make list to plot 
drama = [jan['Drama'], feb['Drama'], mar['Drama'], apr['Drama'], may['Drama'], jun['Drama'], jul['Drama'], aug['Drama'], sep['Drama'], octo['Drama'], nov['Drama'], dec['Drama']]
horror = [jan['Horror'], feb['Horror'], mar['Horror'], apr['Horror'], may['Horror'], jun['Horror'], jul['Horror'], aug['Horror'], sep['Horror'], octo['Horror'], nov['Horror'], dec['Horror']]
action = [jan['Action'], feb['Action'], mar['Action'], apr['Action'], may['Action'], jun['Action'], jul['Action'], aug['Action'], sep['Action'], octo['Action'], nov['Action'], dec['Action']]
comedy = [jan['Comedy'], feb['Comedy'], mar['Comedy'], apr['Comedy'], may['Comedy'], jun['Comedy'], jul['Comedy'], aug['Comedy'], sep['Comedy'], octo['Comedy'], nov['Comedy'], dec['Comedy']]

months3 = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September', 'October', 'November', 'December']

#plots#########################################################################

#1 Number of movies released in different months of 2016
plot.figure(1)
plot.bar([a for a in months],[b for b in months.values()])
plot.xlabel('Month', fontsize = 5)
plot.ylabel('Number of movies', fontsize = 5)
plot.tick_params(axis='both', labelsize = 5)
plot.title('Number of movies released in different months of 2016', fontsize = 5)
plot.show()

#2 Tickets sold in different months of 2016
plot.figure(2)
plot.plot([a for a in months2],[b for b in months2.values()])
plot.xlabel('Month', fontsize = 5)
plot.ylabel('Number of tickets sold', fontsize = 5)
plot.tick_params(axis='both', labelsize = 5)
plot.title('Tickets sold in different months of 2016', fontsize = 5)
plot.show()

#3 Percentage of tickets sold by different distributors
plot.figure(3)
fig1, ax1 = plot.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90, textprops={'fontsize': 5})
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plot.title('Percentage of tickets sold by different distributors', fontsize = 7)
plot.show()

#4 Number of movies released in different months of 2016
plot.figure(4)
plot.plot(months3,drama, label = 'Drama')
plot.plot(months3,horror, label = 'Horror')
plot.plot(months3,action, label = 'Action')
plot.plot(months3,comedy, label = 'Comedy')
plot.legend(loc = 1, fontsize = 5)
plot.tick_params(axis='both', labelsize = 5)
plot.xlabel('Month', fontsize = 6)
plot.ylabel('Number of movies', fontsize = 6)
plot.title('Number of movies released in different months of 2016', fontsize = 6)
plot.show()

