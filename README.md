# ada-2023-project-nada2023
## Abstract 
We’re exploring the international success of movies. Our goal? Discover what makes a movie successful outside of its production countries given its domestic and international box-offices. We’re curious about the mix of genres, available translations, production countries etc. that captivate not only their local audience but the world at large. This project aims to reveal the perfect recipe to produce films that resonate universally. In an increasingly globalized world where culture has been a major vector of this trend, we also would like to explore the evolution of the international expansion of cinema across time. Our data story is not only about numbers, it’s for everyone who wonders why some movies cross borders so easily. 

## Research Questions
- As an intro, how has international success of movies evolved across time?
  - Which decades saw significant spikes or declines in international movie success and can we relate that to historic events? (e.g. beginning of the internet and/or streaming platforms)
  - Are there any noticeable trends in the genres or production countries of movies that tend to perform well internationally in different eras?

- What is the influence of the genre on the international success of movies?
  - Which genres have consistently performed well internationally?
  - For each regions what are the predominantly watched genres?

- What is the influence of the production’s country on the international success of movies?
  - Do co-productions between countries increase international success?  
  - For each country where does it export the most?

Putting 2 and 3 together, what is the best combination of production’s country and genre for international success (for example American action movies, Japanese anime…).

- What is the influence of diversity (ethnicity/gender/languages) on the international success of movies?
  - Ethnicity
    - How has ethnic diversity evolved vs movie’s international success?
    - What’s the ethnicity’s impact on a movie's international success?
    - What’s the perfect ethnic diversity?
  - Gender
    - How has gender diversity evolved vs movie’s international success?
    - What’s the gender’s impact on a movie's international success?
    - What’s the perfect gender diversity?
  - Spoken languages
    - What is the impact of speaking a language in the countries that speak those languages?
    - What is the impact of the number of spoken languages on international success?

## Proposed additional dataset:
- [**Box Office Mojo**](https://www.boxofficemojo.com/?ref_=bo_nb_tt_mojologo):
  - What?
    The box office of movies across countries.
  - Why?
    In order to determine whether a movie performed well internationally we decided to use the box office in the production country vs in the other countries as a metric. Hence, it is crucial for our project to collect data on this. 
  - How?
  For approximately 10 000 movies of the original dataset, we were able to scrap their detailed box office across each country from the website of BoxOfficeMojo. We merged this additional dataset with the original one. 


## Methods:

The metric to measure a movie’s international success will be the percentage of its box-office that is made outside of its production’s country.

### Linear Regression
We will use linear regression (probably with OLS) to see the impact of various factors on the revenue first globally and then on the different regions and the box office. We will use R-squared to see how much impact those factors have.

### Pair Matching
We use pair matching to evaluate the difference between the different groups by matching the data using propensity scores on various attributes like genre year of release… the threshold for the propensity score will probably be around 0.95, we might lower it to have enough matching.

### Network Analysis
We will use network analysis to deepen our understanding and visualize the patterns that exist between the different regions of the world and the different languages spoken around the globe as well. We are probably going to use community analysis to find the trends between and inside our groups. 

## Milestones
### Step 1: General Pre-Processing
- **Gross_IMdB**
  - We scrapped [**Box Office Mojo**](https://www.boxofficemojo.com/?ref_=bo_nb_tt_mojologo). This allowed us to get gross for different movies and have information about the distribution of their box office in different countries.
  - We decided to groups countries in two different ways, first by region (Europe, Middle-East,...) and by language (English, French, Spanish,...).
- **Movie Metadata**
  - From this file we are using the following columns: `genre`, `release_date`, `languages` & `countries`.
  - We made sure that there weren't too many missing values for our analysis.  
- **Character Metadata**
  - From these files we are using the following columns: `actor_gender` & `actor_ethnicity`
  - For the `actor_gender` columns we used it to compute the percentage of men and women in each movies. Same reasoning for `actor_ethnicity`

Then we decided to create a dataframe for each of our questions which are ready to be use for our analysis. 

### Step 2: International Success Over Time
We will be looking at the evolution of the percentage of the box office in the home country. To answer the first part of the question we will mostly use visualization method. We will then use ANOVA to see if there are some genres or coprodution countries that outperform the other in a given year. If any of those occur we will try to map them to big events that occured in that period.

### Step 3: Factor Analysis
We will use ANOVA to see if in general a certain value of a factor outperforms the others (e.g. having a certain genre, or a specific production country). Are there certain values that are better perfoming in our prediefined regions/languages. We might use network analysis to see if we can create links between various values using our data, we will also check if the clusters we find are the same as in the previous point. 

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
    <td class="tg-0lax">Create meaningful visualizations<br><br>Analyze genre and coproduction<br><br>Working on the web interface</td>
  </tr>
  <tr>
    <td class="tg-0lax">@GeorgetteFR</td>
    <td class="tg-0lax">Analyze ethnicity gender and spoken languages<br><br>Perform paired matching<br><br>Develop the web interface</td>
  </tr>
  <tr>
    <td class="tg-0lax">@oElliotJacquetF</td>
    <td class="tg-0lax">Develop the web interface<br><br>Performs network analysis<br><br>Develop the final text for the data story</td>
  </tr>
  <tr>
    <td class="tg-0lax">@Gilles de Waha</td>
    <td class="tg-0lax">Analyze successfull actors<br><br>Develop the final text for the data story<br><br>Perform paired matching</td>
  </tr>
  <tr>
    <td class="tg-0lax">@AmauryGeorge</td>
    <td class="tg-0lax">Create meaningful visualizations<br><br>Performs network analysis<br><br>Develop the final text for the data story</td>
  </tr>
</tbody>
</table>

