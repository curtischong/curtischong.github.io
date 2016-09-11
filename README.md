### wattpad dataset insights

###Project Scope:

To help Authors and advertisers to reach their target audiences by helping:

authors - discover similar authors and their userbase

readers - discover recommended authors

advertisers - locate the most influential authors

We used the wattpad dataset from tranquint to generate the stats to visualize the data.

####Usage
###Databricks
In our data exploration notebook at:
```
https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/76642992983592/2291514426826163/6108891135845519/latest.html
```

you can view our data exploration.

In our submission notebook:
```
https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/76642992983592/1145876117047168/6108891135845519/latest.html
```
you can view our recommendation algorithum which uses the features: age, language, gender, and platform 
to predict author recommendations for new readers that have the same follower characteristics.

###Maps
go to splacorn/github.io to view the map visualiztion of our hack.
Note: due to a lack of a powerful server try not to click on the map or else major lag will occur. clicking on the red points is okay
Simply click on a red point to view all of the followers for that author and some additional statistics.

From the recommendation algorithum in our databricks, you will receive the a list of 3 author ids.
simply paste that author id into the search box and it'll popup on screen (along with its followers)
