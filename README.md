# distributed-data-processing-with-python-intro-talk
Introduction To Distributed Data Processing With Python - Map Reduce, Apache Spark, Structured Streaming

# Setup and Running The Map Reduce code on Google Cloud
  - Download the yelp dataset from https://www.yelp.com/dataset 
  - Extract the dataset keep location of yelp_academic_dataset_business.json handy
  - Create virtualenv `python3.9 -m venv env`
  - Activate virtualenv `source env/bin/activate`
  - Install requirements `pip install -r requirements.txt` 
    - `grpcio` takes a lot of time to build and install.
  - Create Google Dataproc account 
    - Go to cloud.google.com and create an account if you don't have one. Need to add billing and payment info.
    - Search for `dataproc` in search bar of services and products in navigation bar
    - Click on Enable button to enable the service
    - Go to APIs & Services > Credentials
      - Create Credentials  > Service account key 
      - Select Compute Engine - All Admin access
      - Create the key
    - After Key creation create the JSON key pair
    - Store the json at a location you like e.g. I stored it in the home directory `~/.dataproc/importdart-e111a7baa3ce.json` 
  - Run the map reduce script 
      `GOOGLE_APPLICATION_CREDENTIALS=~/.dataproc/importdart-e111a7baa3ce.json python map_reduce_dataproc.py -r dataproc  yelp_academic_dataset_business.json > output.txt`

# Concepts to cover
  - What is Map-Reduce?.
  - What's Hadoop?.
  - Problems with Hadoop
  - What is Apache Spark?. 
    - High level Architecture 
    - How does it overcome the Hadoop problem and relationship with Hadoop

# Code 
## get a dataset for yelp dataset 
  - json -> csv individual files each in respective type folder ( review, users etc )
  
## write a map reduce multi-step script
## apache spark
   - Read entire JSON in memory
   - RDD for computing the ans
   - SQL for computing the ans
## real time distributed data processing architecture ??? Not sure if I can cover this in the same hr

  - stream json to redis streams or kafka or socket
    - one topic for every type
    - windowing / append to df directly
