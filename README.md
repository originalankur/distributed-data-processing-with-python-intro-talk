# Introduction To Distributed Data Processing With Python - Map Reduce, Apache Spark

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

# Installing Apache Spark + Jypter Notebook for local development via Docker
  - `docker pull jupyter/pyspark-notebook`
  - `docker run -it -p 8888:8888 -v `(pwd)`:/home/jovyan/work/projects/ jupyter/pyspark-notebook`
  - Click the hyperlink that shows after running the above docker image 
    ``` [I 2022-02-06 21:37:44.610 ServerApp] Jupyter Server 1.13.5 is running at:
        [I 2022-02-06 21:37:44.610 ServerApp]  or http://127.0.0.1:8888/lab?token=5fd2e5e9849c10b88faeb4a0def592fa6dd07bf7a18c9051
    ```
