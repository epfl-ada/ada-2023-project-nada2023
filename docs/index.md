<meta http-equiv='cache-control' content='no-cache'> 
<meta http-equiv='expires' content='0'> 
<meta http-equiv='pragma' content='no-cache'>
<style>
.responsive-iframe {
    position: relative;
    overflow: hidden;
    padding-top: 60%; /* Height is 60% of width */
    height: 0;
}
.responsive-iframe iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: none;
}
</style>
# Welcome to Our Analysis of the CMU Movie Dataset

In this ADA project, we studied which factors may influence the international success of a movie, measureed by the proportion of it's box office done outside of its production countries.

## Table of Contents
- [Introduction](#introduction)
- [Evolution Across Time](#evolution-across-time)
- [Influence of the genre](#influence-of-the-genre)
- [Influence of the production countries](#influence-of-the-production-countries)
- [Influence of diversity](#influence-of-diversity)
- [Conclusion](#conclusion)

## Introduction

Welcome to our detailed exploration of the fascinating world of movies. In this project, we dive deep into the CMU Movie Dataset, combined with IMdBs box office data ([**BoxOfficeMojo.com**](https://www.boxofficemojo.com/)) unraveling the intricate factors that contribute to the international success of films. Our journey through this dataset is not just about numbers and charts; it's a story about how movies transcend borders and cultural barriers to captivate audiences worldwide.

We examine various elements such as genre preferences, box office trends, and the impact of production countries on a movie's global appeal. By combining statistical analysis with insightful visualizations, we aim to provide a comprehensive understanding of what makes a movie resonate internationally.

Join us as we uncover the hidden narratives behind the data and reveal the evolving landscape of the film industry in an increasingly interconnected world.


## Evolution Across Time

 We observed a nuanced shift in the patterns of international success of movies over the years. By integrating box office data with release dates, we could effectively trace the trajectory of international appeal. Our analysis revealed a gradual increase in the international market share of movies, especially in the latter half of the 20th century and early 21st century. 
![Evolution across time](plots/foreign_box_office_per_year.png)
We can clearly observe a trend since the the start of the 21st century of the ratio of the box office done internationally. Multiple factors could explain this observation : 
- Due to gloablisation, over the past few decades the investments in publicity abroad has drastically increased, and due to new technologies it is much easier to reach a wider audience
- Thanks to internet, it is much easier to gather data on international box office now than before, so we might have more accurate distribution of the box office per country

## Influence of the genre

 The first factor we studied was the influence of the genre on the international success of movies. We looked at the proportion of the box office done outside of the production countries, and the total box office, for each genre. We also looked at the evolution of the proportion of the box office done outside of the production countries for each genre across time.
 
 First, in order to get and idea of how many genres each movie has, here is a histogram of the number of movies per number of genres :

 ![number of genres](notebook_files/notebook_13_0.png)

Most movies have multiple genres, e.g. Titanic (1997) has all of the following genres: Tragedy, Costume drama, Historical fiction, Action/Adventure, Period piece, Drama, Disaster, Romantic drama and Romance Film. This explain why the most represented number of genres is 5.

Now let us look at which genres export the most, as well as the recent evolution of the most exported genres :

![revenue per genre](plots/most_international_genres.png)
<div class="responsive-iframe">
    <iframe src="plots/genre_evolution.html"></iframe>
</div>

## Influence of the Production Countries

In our dataset, we have access to the countries of production of the movies. We were interested in the evolution of co-productions across time, and whether co-productions betweeen countries affects its exports. Also which countries export most ?

![number of coproduction as a function of time](notebook_files/notebook_76_0.png)

As we see, as time advances, movies production companies from different countries seem to work more and more together. Now let us see the impact of co-producing on the total revenue of the movies as well as the share done outside their borders :

![revenue of coproduction as a function of time](notebook_files/notebook_83_0.png)
<div class="responsive-iframe">
    <iframe src="plots/mean_revenue_coprod_genre.html"></iframe>
</div>
![share of coproduction as a function of time](notebook_files/notebook_86_1.png)
<div class="responsive-iframe">
    <iframe src="plots/ratio_int_coprod_genre.html"></iframe>
</div>
We can see that coproducing does not seem to greatly impact the total revenue, however it does seem to increase the share of the revenue done outside the production countries. 

## Influence of Diversity

When investigating if dicersity impacted the performance in a movie, we looked at 3 different factors : 
- The gender ratio and representation of the actors
- The ethnicity of the actors
- The number of languages spoken in the movies

### Gender Representation

We analysed the proportion and number of both male and female actors, as well as cast sizes, and looked for links with the performance, internationally and globally:
![Revenue per number of actors per gender](notebook_files/notebook_54_0.png)
![Revenue per ratio of female actors](notebook_files/notebook_52_1.png)
![Ratio of interational revenue per ratio of female actors]()

We observe that although there is a negative correlation between the ratio of female actors to the total number of actors and the revenue, the international share of the gross does not seem significantly impacted.

## Conclusion
Content for the conclusion..




- [Analysis Part 1](network_region.md)
- [Analysis Part 2](notebook.md)

Explore our findings and discover interesting trends and patterns in movie data!
