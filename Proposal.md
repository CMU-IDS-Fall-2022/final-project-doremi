
# Final Project Proposal

**With this project we would like to answer several questions:**

Does the location of the artists influence their success? Is there a relationship between an artist's most streamed locations in the artist's international success? Are similar artists reproduced in similar places?
1. Does the location of the artists influence their success? Is there a relationship between an artist's most streamed locations in the artist's international success? Are similar artists reproduced in similar places?
—>  If I wanted to become the next Ed Sheeran, is there a country I should focus on?

2. Do the characteristics of the music, features like danceability, liveness, valance, instrumentales… have an influence on the artist's success? Can we use these features to recommend similar music? Do the top items of each artist have similarities in character?
2. Do the characteristics of the music, features like danceability, liveness, valance, instrumentales… have an influence on the artist's success? Can we use these features to recommend similar music? Do the top items of each artist have similarities in character?


3. EXTRA: How can we bring an interesting interaction for the users to explore new music:
At the end of the project, we could also bring a fun game for the audiences to help them explore some fun facts between popularity and their location. Ideally it could support the interaction between multi-users, like people in different regions. We can show how many songs could connect them together by associating the artists’ region or the lyrics of the songs. It’s also possible to let users explore what kind of music is most popular when they choose a country.

To approach this problem and try to answer these questions we are going to use the  Spotify web API (https://developer.spotify.com/documentation/web-api/ ) as our data source. This API lets us access data about any artist on their platform. Available data are location of the audience, the playcount, duration, and the associated artists, which could be our dataset for the project.  We will study and analyze this data to create: map plots (question 1) , or create feature reduction using TSNE and then finding the closest neighbors (question 2). 
 
To make our project even more interactive, we would like to let the user add any artist into our dataset. So we will create an initial dataset with some artists pick us by us and make conclusions. Nevertheless, the dataset would be open for the users to add their choice of artists and that way be able to make their own conclusions.

**GitHub Repo URL**: https://github.com/CMU-IDS-Fall-2022/final-project-doremi 

# Sketch

## Data Processing

The data used will be gathered from Spotify web. To show, a JSON file of each artist we will explore will be downloaded. Therefore, the data processing on this assignment will combine all the JSON files and then create a .csv file or a table from them so it can be later used in the application with pandas.
Below an example of this data scraping can be seen. We get the first artist on the Top 50 USA chart, Drake. We go to his profile and gather the JSON file downloaded by the network with the artist's information.


![image](https://github.com/CMU-IDS-Fall-2022/final-project-doremi/blob/main/1.jpeg)
 
Apart from this dataset, we will need a dataset that has the latitude and coordinates of the cities. We got this dataset from the internet.

## System Design

Compare the artist from the top charts of the countries we belong to:
-Top 50 USA -Top 50 China -Top 50 Spain -

![image](https://github.com/CMU-IDS-Fall-2022/final-project-doremi/blob/main/2.jpeg)

Compare by artist (add artist's origin city as a center point):

![image](https://github.com/CMU-IDS-Fall-2022/final-project-doremi/blob/main/3.jpeg)



**Team Members:**  *Chang Liu, Tomas Cabezon Pedroso, Hongyu Mao, Yang Bai*

