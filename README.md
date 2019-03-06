# **Introduction**

## Problem Statement

Traveling the world today seems easy and exciting! However, there is a lot of research to be done when considering exactly where you want to go. Often times, this research involves exploring multiple websites across the internet to find all kinds of information that you would need when going to a new place as a tourist. Time is spent on websites such as Tripadvisor to find descriptions of the places you might be visiting and Airbnb to find reasonable accommodations. The search doesn&#39;t end here, I&#39;m sure most people would also like to know if the place they are planning to visit is safe and family friendly or not. Thus, this introduces our problem for travelers today; **How can travelers save time and easily figure out which cities are most in-line with where they want to visit?**

## Solution: Recommendation Engine

The aim is to create a city recommendation interface for travel savvy users to find cities that match their interests. Conceptually, each city has a Travel Guide, or text data, attached to it that describes a city&#39;s features like activities, landscapes, food, housing, cost of living, safety, and history.

We consider these features the main criteria a traveler would focus on for choosing his future destination, so overall these Travel Guides are wholesome enough to provide accurate recommendations for these tourists.

By proposing this recommendation engine for these tourists, it will not only save them the hassle of searching the web for countless of hours on different websites but it will also provide accurate results on which cities are most compatible with the features the traveler is looking for. This way, the tourist saves time as well as guaranteed satisfaction on their vacation!

# **Datasets and Web-scraping**

We have 3 sources of data for this project:

- WorldTravelGuide for travel guides
- Numbeo for crime indexes,
- Source of AIRBNB data

Below is an example of a city&#39;s Travel Guide that includes in it information about the city that a traveler might want to know before visiting. The paragraph featured in the &quot;About&quot; section of &quot;Rio de Janeiro&quot; is an example of the text that was scrapped for each city. It should be noted that a total of 130 cities were scrapped for the purpose of this recommendation engine.

![Figure 1](/images/Picture1.png)

Figure 1.

The travel guide data has been scraped from [https://www.worldtravelguide.net/guides/](https://www.worldtravelguide.net/guides/)  where the city and text have been put into a data frame as such:


![Figure 2](/images/Picture2.png)

Figure 2.

The Numbeo and AIRBNB DATA came directly into a structured csv format and were taken off of a Kaggle forum.

# **Coming up with Recommendations**

## Pre-processing the Data

Pre-processing the Data is an important step to consider when dealing with text date as we are from our &quot;review&quot; descriptions for each city. The following steps were taken in order to preprocess the data:

- We first processed the data table into a data frame with each city have the following attributes: _review, Crime Index,__airbnb\_(daily)._ Each city&#39;s review representing a cell.
- Using this data frame, we began the text pre-processing by lower-casing the review section of the data
- This was followed by tokenizing each word in this review cell for each of the cities
- We followed that by lemmatizing the review text
- Lastly, stop words were removed from the review text before we could begin cosine similarity calculations

In addition, the program comes up with recommendations by taking an input from the user through the file _attributes.txt._

## Applying Cosine Similarity

After preprocessing the text data and attributes, we merged attributes and text in a list and applied tf-idf vectorizer to get tf-idf scores.

After getting tf-idf scores, the next step was to calculate cosine similarity. We used [linear\_kernel](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.linear_kernel.html#sklearn.metrics.pairwise.linear_kernel) function to calculate cosine similarity scores instead of [cosine\_similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#sklearn.metrics.pairwise.cosine_similarity) function since we used tf-idf scores which made linear\_kernel and cosine\_similarity functions [equivalent](https://scikit-learn.org/stable/modules/metrics.html#cosine-similarity).

Results are stored in a list named &quot;cosine\_similarities&quot;.

## Results of Recommendation Engine

After getting cosines similarity scores, we filtered considering the price input given by the user. If the city has a higher daily airbnb price than what user put, those cities are filtered out. Then, 5 cities with highest similarity scores with the attributes are printed as output along with their crime indexes and daily airbnb prices so that user can see the crime rate and prices before making a travel decision.

Some examples of output can be seen below.

The first example showcases cities based off of the following text attributes: finance, skyscraper, money and was filtered by a price of $100

![Figure 3](/images/Picture3.png)

Figure 3. Output based off of the following text attributes: finance, skyscraper, money

The second example showcases cities based off of the following text attributes: Cars, industrial, music, and was filtered by a price of $80


![Figure 4](/images/Picture4.png)

Figure 4. Output based off of the following text attributes: Cars, industrial, music

# **Insights from Analysis**

## Limitations

One major limitation that we came up with has to do with choosing the right variables to determine which cities are best suited for our users. We only considered scraping one website to gather information to predict recommendations. It would have been beneficial to use non-text predictors or other numerical data points to better provide to tourists&#39; city options.

Furthermore, we encountered some misclassification problems while using some words in the recommendation search tab. For example, when we entered Church, Cathedral, monument the result was wrong since Ankara was showcased.

![Figure 5](/images/Picture5.png)
Figure 5. Output based off of the following text attributes: Church, Cathedral, monument

# Business Insights

Overall, the problem statement we were trying to solve was: **H**** ow can travelers save time and easily figure out which cities are most in-line with where they want to visit?**

The insights we gained from solving this problem was that there were cities that were spread all across the globe that had similar features. For example: while looking for finance driven cities, our recommendation system predicted cities that were located in continents from Europe (Riga, Geneva etc.) all the way to North America (Chicago).

If this recommendation system was featured on a web-page it could provide insight to travel websites. This recommendation system would also help increase the click through rate of the business which is measured by dividing the number of users who click on a specific link by the number of total users who view a page. This will help the business to measure the level of user engagement as well as the effectiveness and popularity of its engine.

Overall, we got accurate results by using this tool as can be seen in **Figure 3 and 4** and it proves that using text can be used in recommendation engines and provides accurate results.
