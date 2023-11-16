# ada-2023-project-nada2023
Abstract: 
We’re exploring the international success of movies. Our goal? Discover what makes a movie successful outside of its production country given its domestic and international box-office. We’re curious about the mix of genres, available translations, production countries etc. that captivate not only their local audience but the world at large. This project aims to reveal the perfect recipe to produce films that resonate universally. In an increasingly globalized world where culture has been a major vector of this trend, we also would like to explore the evolution of the international expansion of cinema across time. Our data story is not only about numbers, it’s for everyone who wonders why some movies cross borders so easily. 

Research Questions:
As an intro, how has international success of movies evolved across time?
Which decades saw significant spikes or declines in international movie success and can we relate that to historic events? (beginning of the internet or of streaming platforms for example)
Are there any noticeable trends in the genres or production countries of movies that tend to perform well internationally in different eras?

What is the influence of the genre on the international success of movies?
Which genres have consistently performed well internationally?
for each regions what are the predominantly watched genres 

What is the influence of the production’s country on the international success of movies?
Do co-productions between countries increase international success?  
For each country where does it export the most?

Putting 2 and 3 together, what is the best combination of production’s country and genre for international success (for example American action movies, Japanese anime…).

What is the influence of diversity (ethnicity/language//gender/) on the international success of movies?
Ethnicity
How has ethnic diversity evolved vs movie’s international success?
What’s the ethnicity’s impact on a movie's international success?
What’s the perfect ethnic diversity?
Gender
How has gender diversity evolved vs movie’s international success?
What’s the gender’s impact on a movie's international success?
What’s the perfect gender diversity?
Spoken languages
What is the impact of speaking a language in the countries that speak those languages?
What is the impact of the number of spoken languages on international success?


Proposed additional dataset:
BoxOfficeMojo: to get the box office in different regions of the world. This will allow us to have a better idea of how well a movie did in different regions. We did the scrapping ourselves and created a data frame for each movie that we merged in our dataframe.

Methods:

The metric to measure a movie’s international success will be the percentage of its box-office that is made outside of its production’s country.
Linear Regression
We will use linear regression (probably with OLS) to see the impact of various factors on the revenue first globally and then on the different regions and the box office. We will use R-squared to see how much impact those factors have.

Pair Matching
We use pair matching to evaluate the difference between the different groups by matching the data using propensity scores on various attributes like genre year of release… the threshold for the propensity score will probably be around 0.95, we might lower it to have enough matching.
Proposed timeline:
Organization within the team:
?

Analysis : 
General : 
How is the CMU biased 
How is our new dataset biased 
Preprocess our new dataset (get total box office, get box office in country of origin, get box office by regions) 
Create maps from freebase ids to their values 
create the new dataset with scrapped info
Q1 :
Q2:
Q3:
Are there coproductions ? Add a feature for that ?
Q4:
