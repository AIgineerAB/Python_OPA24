# Exercise 2 - Pandas and data processing

These exercises aim for you to train in fundamental pandas and data processing with real datasets.

> [!NOTE]
> These exercises covers lecture 7-12.

## 1. Working with MYH (Myndigheten för yrkeshögskolans) data

Download the [data in excel format from MYH homepage](https://www.myh.se/yrkeshogskolan/resultat-ansokningsomgangar/resultat-for-program). Use the latest file in 2024, which is *resultat-ansokningsomgang-2024.xlsx* and read tabell 3. 
This dataset contains outcomes of applications from education providers to open yrkeshögskolan programs in Sweden. 

&nbsp; a) How many unique educational programs (*Utbildningsnamn*) are there in the dataset?

&nbsp; b) How many unique educational area (*Utbildningsområde*) are there in the dataset?

&nbsp; c) Compare the numbers of educational providers (*Utbildningsanordnare administrativ enhet*)) applying to Data/IT programs (*Utbildningsområde*) in Stockholm and Göteborg

&nbsp; d) What is the total number of applied places (*Sökta platser totalt*) per educational area (*Utbildningsområde*)?

&nbsp; e) Which educational area has the highest success rate in getting approved places by comparing "Beviljade platser totalt" to "Sökta platser totalt"?

&nbsp; f) Plot a bar chart showing the number of unique educational programs (*Utbildningsnamn*) for each "Utbildningsområde"

&nbsp; g) Based on the data here, which educational areas does the government decide to invest more in this year? Plot graphs to support your analysis

&nbsp; h) Following up your analysis on question g), is it different in Göteborg and Stockholm? 



## 2. Olympic games data

In this exercise we'll explore the [olympic games data 120 years back](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results) in time to see if we can find anything interesting. 

&nbsp; a) Start with reading in the dataset into a dataframe using pandas

&nbsp; b) Use pandas columns method to find out the columns

&nbsp; c) Find out the 10 oldest atheletes, their age and the sport

&nbsp; d) Find out the 10 youngest atheletes, their age and the sport

&nbsp; e) Find out the five sports with highest median age

&nbsp; f) Find out the five sports with lowest median age

&nbsp; g) Find out top 10 countries after number of gold medals

&nbsp; h) Find out top 10 countries after number of medals

&nbsp; i) Plot a time series line chart of number of female and male atheletes in same graph.


## 3. Theory questions

&nbsp; a) How do you create a DataFrame in Pandas from a dictionary, a list of dictionaries, and a CSV file, json object?

&nbsp; b) What is the difference between .loc[] and .iloc[] for indexing in Pandas?

&nbsp; c) What is the purpose of the .groupby() method in Pandas? How is it used in data aggregation?

&nbsp; d) How do you export a pandas dataframe into a csv file?




