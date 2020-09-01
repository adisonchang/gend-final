# GEND FINAL PROJECT
# Author: Adison Chang
# Date: 8/31/2020

# This file is responsible for all of the data
# importing and manipulation.

import pandas as pd
import psycopg2


conn = psycopg2.connect(
    host="generationdata.c9g5wowukaqz.us-east-1.rds.amazonaws.com",
    database="generationdata",
    user="gendata_student",
    password="**********" # REPLACE PW HERE 
)
cur = conn.cursor()

# QUERY 1: Mail In Totals
cur.execute(
    """
    select party
    , count(ballot_return_date) as ret
    , count(ballot_issued_date) as iss
    , count(ballot_issued_date) - count(ballot_return_date) as rem
    from ga_absentee
    where ballot_style = 'MAILED'
    group by party
    """
)
col = ['Party', 'Returned', 'Issued', 'Remaining']
mail_tots = pd.DataFrame(data=cur.fetchall(), columns=col)

# QUERY 2: Total Totals
cur.execute(
    """
    select party
    , count(ballot_return_date) as ret
    , count(ballot_issued_date) as iss
    , count(ballot_issued_date) - count(ballot_return_date) as rem
    from ga_absentee
    group by party
    """
)
col = ['Party', 'Returned', 'Issued', 'Remaining']
tot_tots = pd.DataFrame(data=cur.fetchall(), columns=col)

# QUERY 3: Mail In Totals By County
cur.execute(
    """
    select county
    , count(ballot_issued_date) as iss
    , count(ballot_return_date) as ret
    , count(ballot_issued_date) - count(ballot_return_date) as rem
    from ga_absentee
    where ballot_style = 'MAILED'
    group by county
    """
)
col = ['County', 'Issued', 'Returned', 'Remaining']
mail_county = pd.DataFrame(data=cur.fetchall(), columns=col)

# QUERY 4: Dem Mail In Totals By COUNTY
cur.execute(
    """
    select county
    , count(ballot_issued_date) as iss
    , count(ballot_return_date) as ret
    , count(ballot_issued_date) - count(ballot_return_date) as rem
    from ga_absentee
    where ballot_style = 'MAILED'
    and party = 'DEMOCRAT'
    group by county
    """
)
col = ['County', 'Issued', 'Returned', 'Remaining']
dem_mail_county = pd.DataFrame(data=cur.fetchall(), columns=col)

# QUERY 5: Counties to Target
cur.execute(
    """
    select county
    , count(ballot_issued_date) as iss
    , count(ballot_return_date) as ret
    , count(ballot_issued_date) - count(ballot_return_date) as rem
    from ga_absentee
    where ballot_style = 'MAILED'
    and (party = 'DEMOCRAT' or party = 'NON-PARTISAN')
    group by county
    order by rem desc
    """
)
col = ['County', 'Issued', 'Returned', 'Remaining']
target_county = pd.DataFrame(data=cur.fetchall(), columns=col)

# QUERY 6: Problem Counties
cur.execute(
    """
    select county
    , count(application_date) as app
    , count(ballot_issued_date) as iss
    , round(count(ballot_issued_date) * 100.0 / count(application_date), 2)
    as perc_issued
    from ga_absentee
    where ballot_style = 'MAILED'
    group by county
    order by perc_issued
    """
)
col = ['County', 'Applied', 'Issued', 'PercentIssued']
problem_county = pd.DataFrame(data=cur.fetchall(), columns=col)

cur.close()
conn.close()
