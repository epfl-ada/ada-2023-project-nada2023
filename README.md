# ada-2023-project-nada2023
## Abstract 
We’re exploring the international success of movies. Our goal? Discover what makes a movie successful outside of its production country given its domestic and international box-office. We’re curious about the mix of genres, available translations, production countries etc. that captivate not only their local audience but the world at large. This project aims to reveal the perfect recipe to produce films that resonate universally. In an increasingly globalized world where culture has been a major vector of this trend, we also would like to explore the evolution of the international expansion of cinema across time. Our data story is not only about numbers, it’s for everyone who wonders why some movies cross borders so easily. 

## Research Questions
1. As an intro, how has international success of movies evolved across time?
  a. Which decades saw significant spikes or declines in international movie success and can we relate that to historic events? (beginning of the internet or of streaming platforms for example)
  b. Are there any noticeable trends in the genres or production countries of movies that tend to perform well internationally in different eras?

2. What is the influence of the genre on the international success of movies?
  a. Which genres have consistently performed well internationally?
  b. For each regions what are the predominantly watched genres?

3. What is the influence of the production’s country on the international success of movies?
  a. Do co-productions between countries increase international success?  
  b. For each country where does it export the most?

Putting 2 and 3 together, what is the best combination of production’s country and genre for international success (for example American action movies, Japanese anime…).

4. What is the influence of diversity (ethnicity/language//gender/) on the international success of movies?
  a. Ethnicity
    i.   How has ethnic diversity evolved vs movie’s international success?
    ii.  What’s the ethnicity’s impact on a movie's international success?
    iii. What’s the perfect ethnic diversity?
  b. Gender
    i.   How has gender diversity evolved vs movie’s international success?
    ii.  What’s the gender’s impact on a movie's international success?
    iii. What’s the perfect gender diversity?
  c. Spoken languages
    i.   What is the impact of speaking a language in the countries that speak those languages?
    ii.  What is the impact of the number of spoken languages on international success?
   
## Milestones
### Step 1: General Pre-Processing
- **Gross_IMdB**
  - We scrapped [**Box Office Mojo](https://www.boxofficemojo.com/?ref_=bo_nb_tt_mojologo). This allowed us to get gross for different movies and have information about the distribution of their box office in different countries.
  - We decided to groups countries in two different ways, first by region (Europe, Middle-East,...) and by language (English, French, Spanish,...).
- **Movie Metadata**
  - From this file we are using the following columns: `genre`, `release_date`, `languages` & `countries`.
  - We made sure that their weren't to many missing values for our analysis.  
- **Character Metadata**
  - From this files we are using the following columns: `actor_gender` & `actor_ethnicity`
  - For the `actor_gender` columns we used it to compute the percentage of men and woman in each movies. Same reasoning for `actor_ethnicity`

Then we decided to create a dataframe for each of our question which is ready to be use for our analysis. 

### Step 2: International Success over time

We performed ANOVA testing to determine if there are differences in revenue mean for the movies released in different months. We then conducted 12 t-tests, with one month as one group and the rest as the other group. We repeated this analysis for the 10 most common genres.

### Step 3: Genre
We used $ethnicity\ score = \frac{number\ of\ ethnicities}{number\ of\ actors}$ and $female\ score = \frac{number\ of\ females}{number\ of\ actors}$ to measure the effect of diversity on revenue made. We used a threshold with $ethnicity\ score = 0.5$ and $female\ score = 0.5$ to create splits of the dataframe and then performed t-tests on the pairwise groups. For more insight we extended our analysis by a range of thresholds and calculated the confidence intervals. Additionally, we performed paired matching to control the effects of confounding variables and estimate causation effects.

### Step 4: Production Countries
We used One-Hot Encoding of the actors by creating a dummy variable for each actor. We created a new variable for each actor, so we had to experiment with different thresholds to avoid excessively large DataFrames. The threshold corresponds to how many movies the actor has played.
The DataFrame was then used in a linear regression model using the actors as categorical predictors. For more insights in potential patterns we used a network analysis, in which we modeled the actors as nodes and edges as indicators for movies two actors starred in together. We used the Louvain method to extract communities of actors and then analysed if movies, which have a majority of actors from one community or contain more than half of one community, have a higher revenue by using regression.

### Step 5: Ethnicity
We used runtime and box office revenue to split the DataFrames into pairwise groups on which we performed t-tests. 

### Step 6: Gender
We calculate the proportion of words with `positive` / `negative` / `violent` connotations out of all words in the movie summary. We used t-tests and linear regression to measure the effect of certain terms used to describe the movie.

### Step 7: Spoken Languages




## Proposed additional dataset:
BoxOfficeMojo: to get the box office in different regions of the world. This will allow us to have a better idea of how well a movie did in different regions. We did the scrapping ourselves and created a data frame for each movie that we merged in our dataframe.

## Methods:

The metric to measure a movie’s international success will be the percentage of its box-office that is made outside of its production’s country.

### Linear Regression
We will use linear regression (probably with OLS) to see the impact of various factors on the revenue first globally and then on the different regions and the box office. We will use R-squared to see how much impact those factors have.

### Pair Matching
We use pair matching to evaluate the difference between the different groups by matching the data using propensity scores on various attributes like genre year of release… the threshold for the propensity score will probably be around 0.95, we might lower it to have enough matching.

## Proposed timeline:
```
.
├── 22.11.22 - Perform paired matching
│  
├── 24.11.22 -  Perform trend analysis
│  
├── 29.11.22 - Pause project work
│  
├── 01.12.22 - Homework 2 deadline
│    
├── 08.12.22 - Perform final analysis
│  
├── 13.12.22 - Develop draft for data story
│  
├── 15.12.22 - Finalize code implementations and visualizations
│  
├── 18.12.22 - Finalize data story
│  
├── 22.12.22 - Milestone 3 deadline
.
```

## Organization within the team:
<table class="tg" style="undefined;table-layout: fixed; width: 342px">
<colgroup>
<col style="width: 164px">
<col style="width: 178px">
</colgroup>
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax">Tasks</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">@BrokenSki8</td>
    <td class="tg-0lax">Create meaningful visualizations<br><br>Continue exploring the dataset<br><br>Working on the web interface</td>
  </tr>
  <tr>
    <td class="tg-0lax">@GeorgetteFR</td>
    <td class="tg-0lax">Analyze successful movie themes<br><br>Create meaningful visualizations<br><br>Develop the web interface</td>
  </tr>
  <tr>
    <td class="tg-0lax">@oElliotJacquetF</td>
    <td class="tg-0lax">Develop the web interface<br><br>Develop the final text for the data story<br><br>Perform trend analysis</td>
  </tr>
  <tr>
    <td class="tg-0lax">@Gilles de Waha</td>
    <td class="tg-0lax">Analyze successfull actors<br><br>Develop the final text for the data story<br><br>Perform paired matching</td>
  </tr>
  <tr>
    <td class="tg-0lax">@AmauryGeorge</td>
    <td class="tg-0lax">Analyze successfull actors<br><br>Develop the final text for the data story<br><br>Perform paired matching</td>
  </tr>
</tbody>
</table>

