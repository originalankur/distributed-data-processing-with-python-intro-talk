# distributed-data-processing-with-python-intro-talk
Introduction To Distributed Data Processing With Python - Map Reduce, Apache Spark, Structured Streaming

# Concepts to cover
  - What is Map-Reduce 
  - What's Hadoop?.
  - Problems with Hadoop
  - What is Apache Spark?. 
    - High level Architecture 
    - How does it overcome the Hadoop problem and relationship with Hadoop

# Code 
## get a dataset for yelp dataset 
  - json -> csv individual files each in respective type folder ( review, users etc )
  
## write a map reduce multi-step script to find
  - Which state has the most resturant?.
  - Which resturant has most reviews?
  - What % of resturant has takeout?.
  - Food Category distribution
  - Who are the top 100 reviewers of food

## apache spark
   - Read entire JSON in memory
   - RDD for computing the ans
   - SQL for computing the ans

## real time distributed data processing architecture

  - stream json to redis streams or kafka or socket
    - one topic for every type
    - windowing / append to df directly
