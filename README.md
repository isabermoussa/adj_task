# adj_task

>Solutions for Adjust challenge with python3 and Django.

## Table of Contents

1. [Problem](#problem)
2. [Install](#install)
3. [Usage](#usage)


### problem
> Expose the sample dataset through a single generic HTTP API endpoint, which is capable of filtering, grouping and sorting. Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a given date, advertising channel, country and operating system. It is expected to be stored and processed in a relational database of your choice.

> Client of this API should be able to:
    1. filter by time range (date_from / date_to is enough), channels, countries, operating systems
    2. group by one or more columns: date, channel, country, operating system
    3. sort by any column in ascending or descending order
    4. see derived metric CPI (cost per install) which is calculated as cpi = spend / installs

### install
1. clone this [repo](https://github.com/esabermousa/adj_task)
2. enter repo dir and create virtualenv python 3.6 or higher.
3. install dependancies from requirements file.
    ``` 
    $ source env/bin/activate
    $ pip install -r requirements.txt
    ```
4. update postgres DB cradentials in settings.py file.
5. migrate DB and seed data from csv fiel to Postgres Database.
    ```
    $ cd adjustapi
    $ python manage.py migrate
    $ python manage.py seed_dataset -f `file path` -d postgresql://DBuser:DBpass@DBhost:5432/DBname
    ```
6. run test cases
    ```
    $ python manage.py test dataset
    ```
7. run django app,
    ```
    $ python manage.py runserver
    ```

### usage
> There is only one endpoint GET `/api/dataset/` so changes in params.

#### Request Parameters

Name | Type | Description | Required | Using
---- | ---- | ----------- | -------- | ------------------------
channel | String | channel value to filter with | NO | Filter by
date__range | Date `comma separated` | date range to filter with. **Format:** 2017-06-12,2017-06-14 | NO | Filter by
country | String | country value to filter with  | NO | Filter by
os | String | country value to filter with | NO | Filter by
ordering | `- to Desc Order` String | field names to order by them **Format:** -revenue,date | NO | Ordering
group_by | String `comma separated` | field names to group by them **Format:** channel,country,date | NO | Group by

#### Sample Response
```
[
    {
        "date": "2017-06-03",
        "channel": "adcolony",
        "country": "US",
        "impressions": 20555,
        "clicks": 598,
        "installs": 144,
        "spend": "179.400",
        "revenue": "517.210",
        "cpi": 1.2458333333333333
    },
    {
        "date": "2017-06-02",
        "channel": "adcolony",
        "country": "US",
        "impressions": 23551,
        "clicks": 529,
        "installs": 104,
        "spend": "158.700",
        "revenue": "505.200",
        "cpi": 1.5259615384615384
    },
    ...
]
```
