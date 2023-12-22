---
layout: page
title: Movie exportation success
cover-img: ban_gpt.png
thumbnail-img: ban_gpt.png
share-img: ban_gpt.png
use-site-title: false
full-width-genres: true

---

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
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
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

Welcome to our detailed exploration of the fascinating world of movies. In this project, we dive deep into the CMU Movie Dataset, combined with IMdB's box office data ([**BoxOfficeMojo.com**](https://www.boxofficemojo.com/)) unraveling the intricate factors that contribute to the international success of films. Our journey through this dataset is not just about numbers and charts; it's a story about how movies transcend borders and cultural barriers to captivate audiences worldwide.

We examine various elements such as genre preferences, box office trends, and the impact of production countries on a movie's global appeal. By combining statistical analysis with insightful visualizations, we aim to provide a comprehensive understanding of what makes a movie resonate internationally.

Join us as we uncover the hidden narratives behind the data and reveal the evolving landscape of the film industry in an increasingly interconnected world.


## Evolution Across Time

 We observed a nuanced shift in the patterns of international success of movies over the years. By integrating box office data with release dates, we could effectively trace the trajectory of international appeal. Our analysis revealed a gradual increase in the international market share of movies, especially in the latter half of the 20th century and early 21st century. 
 
<div class="responsive-iframe">
    <iframe src="plots/foreign_evolution.html"></iframe>
</div>

We can clearly observe a trend since the start of the 21st century of the ratio of the box office done internationally. Multiple factors could explain this observation : 
- Due to gloablisation, over the past few decades the investments in publicity abroad has drastically increased, and due to new technologies it is much easier to reach a wider audience
- Thanks to internet, it is much easier to gather data on international box office now than before, so we might have more accurate distribution of the box office per country

![region_to_region](network_region_files/network_region_62_0.png)

## Influence of the genre

 The first factor we studied was the influence of the genre on the international success of movies. We looked at the proportion of the box office done outside of the production countries, and the total box office, for each genre. We also looked at the evolution of the proportion of the box office done outside of the production countries for each genre across time.
 
 First, in order to get an idea of how many genres each movie has, here is a histogram of the number of movies per number of genres :

 

 <div class="responsive-iframe">
    <iframe src="plots/nb_genres.html"></iframe>
</div>

Most movies have multiple genres, and the most common number of genres is 3. We can also see that there are a lot of movies with only one genre, and a few movies with 7 or more genres.

Now let us look at which genres export the most, as well as the recent evolution of the most exported genres :

<div class="responsive-iframe">
    <iframe src="plots/most_international_genres.html"></iframe>
</div>

<div class="responsive-iframe">
    <iframe src="plots/genre_evolution.html"></iframe>
</div>

As we see from above, science-fiction and thriller genres emerge as the most exported movie categories. This popularity can be attributed to their wide appeal, cutting-edge special effects, and often universal themes that resonate across different cultures. On the other hand, the World cinema and Documentary genres appear to be the least exported. This could be due to their niche appeal and the fact that documentaries and World cinema movies often delve into culturally specific subjects, which might not translate as effectively to international audiences. 

<div class="responsive-iframe">
    <iframe src="plots/pie_chart_exported.html"></iframe>
</div>

<div class="responsive-iframe">
    <iframe src="plots/pie_chart_watched.html"></iframe>
</div>


## Influence of the Production Countries

Another factor that we thought would be important for the export of movies is the coutries in which the movies were shot. 
We first tried to understand if a production region had an influence on how a movie was exporting. To do so, we performed a paired matching. In our case, the treatment is producing the movie in Europe. We used logistic regression to compute the propensity score based on the movie release date, the number of languages and the number of production countries. Unfortunately, we did not find any statistically significant difference between the two groups. And since the control group, is mostly composed of north american movies, the results would have been similar by taking North America as region of production as the treatment. 

<div class="responsive-iframe">
    <iframe src="plots/pair_matching_region.html"></iframe>
</div>

Therefore, we will focus on the influence of co-prodoctions of movies. Firstly, we do a brief analysis on the total gross of the movies to then fine-tune it to the ratio made in foreign coutries. 

<div class="responsive-iframe">
    <iframe src="plots/movies_coprod_ratio.html"></iframe>
</div>


As we see, as time advances movie production companies from different countries seem to work more and more together, but the ratio of films made in co-production barely goes up. From this graph we saw that there was a little increase in the ratio of movies that were made by mutlitple countries in the last 20 years. This small increase leads us to think that having a co-production would slightly boost the revenue of a movie. The question now is how many coutries should you have to maximize your revenue? And how many co-producing countries should you have if you want to maximize the ratio of the revenue made outside the production countries?   

<div class="responsive-iframe">
    <iframe src="plots/mean_revenue_coprod_number.html"></iframe>
</div>

So on average movies made in two countries are the one yielding the most revenues. The use of T-test allowed us to see that the difference in mean was statistically significant, which allows us to conclude that the collaboration of two countries should lead on average to a higher grossing film than any other number of co-production coutries. Even if the test allows us to say that the difference is statistically different the T-statistic is rather small (~2), this tells us that even if the difference exists it doesn't have a huge impact. The section above told us that the genre of a movie has an influence so let us see if all genres perform the same.

<div class="responsive-iframe">
    <iframe src="plots/tot_coprod_genre.html"></iframe>
</div>

For most genres we will have the same conclusion as for all movies, i.e. two co-production countries is the best. The notable exceptions are World Cinema, Romance Film and Comedy. We don't have an explanation for why that is but the fact that Romance Film and Comedy behave in the same way isn't surprising as 60% of movies that are romantic are also comedies and 40% of comedies are romantic films as well. For the World Cinema genre, we give an explanation about why it might behave like that after we analyse the number or production region for a movie. 

<div class="responsive-iframe">
    <iframe src="plots/country_co-productions.html"></iframe>
</div>


### Coproduction countries vs. ratio of international revenue

We now know that the best number of countries for total gross is usually 2, is this the same if we look at the ratio of the revenue made outside of the production countries? I'll let you pause for a minute and think about how increasing the number of co-production countries might affect the international ratio.

![mmmh!](plots/thinking_meme.jpg)

The following graphs are two representation of the same idea. The first on is a line plot of the Mean ratio of the revenue made by movies made in a given number of coutries. The second one is the same values but plotted as a box plot to give a more accurate idea about the distribution of the values. 

<div class="responsive-iframe">
    <iframe src="plots/mean_ratio_coprod.html"></iframe>
</div>
<div class="responsive-iframe">
    <iframe src="plots/ratio_int_box_coprod.html"></iframe>
</div>

Here we can see that the more co-production countries we have, the more the ratio of the revenue is made in foreign coutries. This result might be a little counter-intuitive. If we had defined a _main production country_ and we had looked at the ratio of the revenue made outside of this country it would have seemed obvious that it would be higher, because part of the revenue would have bean made in  the _secondary production country_. Here we look at the ratio of the box office made outside of all the production countries and we still have a positive correlation. As before the use of T-test allows us to be sure that the difference is statistically. Moreover, this time the T-statistic is much higher (for 1 country vs. multiple T-stat ~ -19). With the same reasoning as before we can now look at how different genres behave regarding the number of co-producing countries. We did various T-test to see which countries augmented their export by co-producing movies. With a T-statistique of around -13 the USA is the one country from the few we analyzed that gains the most when co-producing with other countries. France and India also gain a bit but the difference is much lower both have a T-statistic of ~3. 

<div class="responsive-iframe">
    <iframe src="plots/ratio_int_coprod_genre.html"></iframe>
</div>

In this case almost all genre seem to follow the expected trend with small variations. The only notable exception to the rule is the _Thriller_ genre that has a ratio of international revenue that goes down when we reach 4 co-production countries. 

### Influence of the number of regions 

We made a small analysis about the number of region that produced a movie and its relation to the ratio of international revenue. We found very similar results as for the number of co-production countries. We can explain that by the fact that 75% of the co-produced movies have countries from multiple regions. We can make the simplified hypothesis that adding a country is like adding a region so we won't repeat ourselves.    

## Influence of the number of languages

Since we analysed the influence of the number of co-production countries had in the revenue and the export of the movies. We wondered if having multiple languages could also help export movies. Since the two ideas are pretty simlar, we will follow the same template as for the number of coproduction countries. 

<div class="responsive-iframe">
    <iframe src="plots/movies_lang_ratio.html"></iframe>
</div>

This graph is really similar to the one about the ratio of movies made by more than one country. Our anaylsis stays the same if we see an augmentation it is probably due to multiple factors, one of them being that it should help boost the revenue of the movies. As before we ask ourself how many language should a movie have to have the best expected revenue? And is this the same number if we want our movie to export as much as possible?

<div class="responsive-iframe">
    <iframe src="plots/gross_languages.html"></iframe>
</div>

In the graph above we only kept movies that have up to five languages because our dataset doesn't contain enough movies with more infomation to be relevant in our study. This visualisation shows us that the more languages, or at least up to five languages, you have, the more on average your movie is suppose to make. Since we don't have enough information about movies with more languages we cannot say what the perfect number of languages would be, but we can say that the more the better although you probably don't want to overdo it. The T-test here is much clearer with a T-statistic of ~ -8, as usual the p/value is reallz small and allows us to say that the difference is statistically relevent. As for the co-production countries let us do the same analysis but seperate the result per genre. 

<div class="responsive-iframe">
    <iframe src="plots/mean_rev_lang_genre.html"></iframe>
</div>

We can see that most genres follow the expected trend with the notable exceptions being Adventure, Thriller and Crime Fiction. The Adventure movies mysteriously don't perform as well when they have 3 and five languages but others follow the expected trend. Thriller and Crime Fiction take a hit at 4 languages and then go back up at five. For all three of these anomalies we weren't able to give an explanation. But even with these particularities we would still advise a movie do have as many languages as possible (or at least up to five).

### Number of languages vs. ratio of international revenue

We now know that the higher the number of languages the higher the total gross is, can we say the same if we look at the ratio of the revenue made outside of the production countries. Just as before we'll let you pause and try to predict how the following graph might look like.

<img src = "plots/Drake_meme.png" class="center">


We used the same representation as before. Two graphes showing the average export ratio of the movies one as a line plot one as a box plot. 

<div class="responsive-iframe">
    <iframe src="plots/mean_ratio_lang.html"></iframe>
</div>

<div class="responsive-iframe">
    <iframe src="plots/ratio_int_box_lang.html"></iframe>
</div>

This time the ratio of international revenue behaves the same as the total revenue, i.e. the more languages you have the more you can expect your movie to export. As before the use of T-test allows us to be sure that the difference is statistically significant. Moreover, this time the T-statistic is much higher (for 1 language vs. multiple T-stat ~ -14). With the same reasoning as before we can now look at how different genres behave regarding the number of languages. We did various T-tests to see which language benifited in their export by mixing them with others movies. With a T-statistique of around -13 English is the one language from the few we analyzed that gains the most when mixing with others. French and Japanese also gain a bit but the difference is much lower both have a T-statistic of ~ -3. For Spanish and Hindi, which complete the top 5 of most common languages in our dataset, the difference is not statistically significant

<div class="responsive-iframe">
    <iframe src="plots/mean_rev_lang_genre.html"></iframe>
</div>

Except for minor exceptions the genres behave as we would except them to. Meaning that, at least up to 5 languages, the more languages the better. The science-fiction is the only genre that doesn't reach its maximum with 5 languages. 
 

## Influence of Diversity

When investigating if dicersity impacted the performance in a movie, we looked at 3 different factors : 
- The gender ratio and representation of the actors
- The ethnicity of the actors
- The number of languages spoken in the movies

### Gender Representation

We analysed the proportion and number of both male and female actors, as well as cast sizes, and looked for links with the performance, internationally and globally:
![Revenue per number of actors per gender](notebook_files/notebook_54_0.png)
<div class="responsive-iframe">
    <iframe src="plots/gross_per_female_ratio.html"></iframe>
</div>
<div class="responsive-iframe">
    <iframe src="plots/ratio_export_per_female.html"></iframe>
</div>

We observe that although there is a negative correlation between the ratio of female actors to the total number of actors and the revenue (spearman correlation of -0.14, P Value extremely close to 0), the international share of the gross does not seem significantly impacted (spearman correlation of -0.04, P Value extremely close to 0 once again). 

### Ethnic Diversity

Another factor taken into account is whether the number of represented ethnicities in a movie would have an impact. After retrieving the ethnicities of the actors we had access to in the CMU Dataset, we calculated the entropy of the ethnicity of the actors. For a given number of represented ethnies, the entropy is maximal when each ethnies appear with equal proportion. We then looked at the correlation between this entropy and the international share of the gross.
<div class="responsive-iframe">
    <iframe src="plots/ethnic_entropy"></iframe>
</div>

As we can see the entropy of the ethnies is positively correlated with the international share of the gross, meaning that the more diverse the cast is, the more likely the movie is to be successful internationally. However, this is also biased towards larger casts as the entropy is higher for larger casts. 

## Conclusion
Content for the conclusion..




- [Analysis Part 1](network_region.md)
- [Analysis Part 2](notebook.md)

Explore our findings and discover interesting trends and patterns in movie data!
