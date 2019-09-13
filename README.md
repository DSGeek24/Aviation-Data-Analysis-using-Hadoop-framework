Aviation Data Analysis using Mapper-Reducers

Given is a dataset which consists of data in .csv file format of all flights that occurred between 2006 and 2008 in US. Each line in the csv file corresponds to the information of one flight (Year, Month, Origin Airport, Departure Delay, Arrival delay etc.) which is obtained from a public data source. (http://stat-computing.org/dataexpo/2009/the-data.html) 

The problem is to find the percentage of delayed flights per an origin airport and percentage of delayed flights per origin airport in a given month which is useful for summarizing descriptive statistics of data. Such summary can help in deriving insights about which airport has more instances of delayed flights and also the month in which the flights were more delayed.  

The dataset given is too large with around 21 million flight records. For large datasets, Hadoop serves as a good framework to process vast amounts of data in parallel on clusters with multiple nodes. The dataset is split into independent parts which are then processed by mappers in parallel manner. The output of the maps is sorted and then sent as input to reducers.
