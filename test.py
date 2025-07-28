import numpy as np
import pandas as pd
import random
from datetime import date, timedelta, timezone
from datetime import datetime
from dateutil import tz
from termcolor import colored, cprint
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Create a sample dataset
def generate_random_list(size, start, end):
    random_list = []
    for _ in range(size):
        random_list.append(random.randint(start, end))
    return random_list

# Example usage:
random_numbers = generate_random_list(10, 1, 100)
print(random_numbers)
login_data = {
        #'MONTH': ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT"], 
        'day': generate_random_list(10, 1, 100), 
        'year': generate_random_list(10, 1, 500),
        'session_id': generate_random_list(10, 1, 1000)}
logins = pd.DataFrame(login_data)
print (logins)
print (logins.info())
print (logins.shape)

std_scaler = StandardScaler()
scaled_df = std_scaler.fit_transform(logins)
print (scaled_df)

# Initialize PCA object with the desired number of components
pca = PCA(n_components=3)

# Transform the data to the new lower-dimensional space
X_transformed = pca.fit_transform(scaled_df)

var_exp = pca.explained_variance_ratio_
print(var_exp)

print(pca.components_.shape)

print (colored ("############# Exercise Question #####################","red", attrs=['bold']))
x = ['cry', 'myth', 'aqua', 'ciao']
n_vowel = map(lambda w: w.count('a'),x)
print(list(n_vowel))

print (colored ("############# Exercise Question #####################","red", attrs=['bold']))
my_list = [1, 2, 3, 4, 5, 6]
even_numbers = list((lambda x: x % 2 == 0, my_list))
print (even_numbers)

print (colored ("############# Handle date #####################","red", attrs=['bold']))
hurricane_date = ['01/12/2019', '05/01/2022']
print (hurricane_date)

hurricane_date_mod = [date(2019, 1, 12), date(2022, 5, 1)]
print (hurricane_date_mod)

print (colored ("First hurricane date:","red", attrs=['bold','underline']))
print (hurricane_date_mod[0].day)
print (hurricane_date_mod[0].month)
print (hurricane_date_mod[0].year)

print (colored ("First hurricane date was on which weekday?","red", attrs=['bold','underline']))
print (hurricane_date_mod[0].weekday())

print (colored ("Second hurricane date:","red", attrs=['bold','underline']))
print (hurricane_date_mod[1].day)
print (hurricane_date_mod[1].month)
print (hurricane_date_mod[1].year)

print (colored ("Second hurricane date was on which weekday?","red", attrs=['bold','underline']))
print (hurricane_date_mod[1].weekday())

print (colored ("Substruct two dates","red", attrs=['bold','underline']))
d1 = date(2019, 1, 12)
d2 = date(2022, 5, 1)
delta = d2 - d1
print ("Difference between two dates: {}".format(delta.days))
d1 = date(2019, 1, 12)
print (colored ("Current date is {}".format(d1),"green", attrs=['bold','underline']))
print ("Current date in ISO format {}".format(d1.isoformat()))
td = timedelta(days=30)
for i in range(0,5):
    print (colored ("New date:{}".format(d1),"green", attrs=['bold','underline']))
    td = timedelta(days=30)
    d1 += td

print (colored ("######## STRFTIME #############", "green", attrs=['bold','underline']))
d1 = date(2019, 1, 12)
print ("1st type of strftime - YYYY-MM-DD format")
print (d1.strftime("%Y-%d-%m"))
print ("2nd type of strftime - YYYY-DD-MM format")
print (d1.strftime("%Y-%m-%d"))

florida_hurricane_dates = [date(1950, 8, 31), date(1950, 9, 5), date(1950, 10, 18), date(1950, 10, 21), date(1951, 5, 18), date(1951, 10, 2), date(1952, 2, 3), date(1952, 8, 30), date(1953, 6, 6), date(1953, 8, 29), date(1953, 9, 20), date(1953, 9, 26), date(1953, 10, 9), date(1955, 8, 21), date(1956, 7, 6), date(1956, 9, 24), date(1956, 10, 15), date(1957, 6, 8), date(1957, 9, 8), date(1958, 9, 4), date(1959, 6, 18), date(1959, 10, 8), date(1959, 10, 18), date(1960, 7, 29), date(1960, 9, 10), date(1960, 9, 15), date(1960, 9, 23), date(1961, 9, 11), date(1961, 10, 29), date(1962, 8, 26), date(1963, 10, 21), date(1964, 6, 6), date(1964, 8, 27), date(1964, 9, 10), date(1964, 9, 20), date(1964, 10, 5), date(1964, 10, 14), date(1965, 6, 15), date(1965, 9, 8), date(1965, 9, 30), date(1966, 6, 9), date(1966, 6, 30), date(1966, 7, 24), date(1966, 10, 4), date(1968, 6, 4), date(1968, 6, 18), date(1968, 7, 5), date(1968, 8, 10), date(1968, 8, 28), date(1968, 9, 26), date(1968, 10, 19), date(1969, 6, 9), date(1969, 8, 18), date(1969, 8, 29), date(1969, 9, 7), date(1969, 9, 21), date(1969, 10, 1), date(1969, 10, 2), date(1969, 10, 21), date(1970, 5, 25), date(1970, 7, 22), date(1970, 8, 6), date(1970, 9, 13), date(1970, 9, 27), date(1971, 8, 10), date(1971, 8, 13), date(1971, 8, 29), date(1971, 9, 1), date(1971, 9, 16), date(1971, 10, 13), date(1972, 5, 28), date(1972, 6, 19), date(1972, 9, 5), date(1973, 6, 7), date(1973, 6, 23), date(1973, 9, 3), date(1973, 9, 25), date(1974, 6, 25), date(1974, 9, 8), date(1974, 9, 27), date(1974, 10, 7), date(1975, 6, 27), date(1975, 7, 29), date(1975, 9, 23), date(1975, 10, 1), date(1975, 10, 16), date(1976, 5, 23), date(1976, 6, 11), date(1976, 8, 19), date(1976, 9, 13), date(1977, 8, 27), date(1977, 9, 5), date(1978, 6, 22), date(1979, 7, 11), date(1979, 9, 3), date(1979, 9, 12), date(1979, 9, 24), date(1980, 8, 7), date(1980, 11, 18), date(1981, 8, 17), date(1982, 6, 18), date(1982, 9, 11), date(1983, 8, 28), date(1984, 9, 9), date(1984, 9, 27), date(1984, 10, 26), date(1985, 7, 23), date(1985, 8, 15), date(1985, 10, 10), date(1985, 11, 21), date(1986, 6, 26), date(1986, 8, 13), date(1987, 8, 14), date(1987, 9, 7), date(1987, 10, 12), date(1987, 11, 4), date(1988, 5, 30), date(1988, 8, 4), date(1988, 8, 13), date(1988, 8, 23), date(1988, 9, 4), date(1988, 9, 10), date(1988, 9, 13), date(1988, 11, 23), date(1989, 9, 22), date(1990, 5, 25), date(1990, 10, 9), date(1990, 10, 12), date(1991, 6, 30), date(1991, 10, 16), date(1992, 6, 25), date(1992, 8, 24), date(1992, 9, 29), date(1993, 6, 1), date(1994, 7, 3), date(1994, 8, 15), date(1994, 10, 2), date(1994, 11, 16), date(1995, 6, 5), date(1995, 7, 27), date(1995, 8, 2), date(1995, 8, 23), date(1995, 10, 4), date(1996, 7, 11), date(1996, 9, 2), date(1996, 10, 8), date(1996, 10, 18), date(1997, 7, 19), date(1998, 9, 3), date(1998, 9, 20), date(1998, 9, 25), date(1998, 11, 5), date(1999, 8, 29), date(1999, 9, 15), date(1999, 9, 21), date(1999, 10, 15), date(2000, 8, 23), date(2000, 9, 9), date(2000, 9, 18), date(2000, 9, 22), date(2000, 10, 3), date(2001, 6, 12), date(2001, 8, 6), date(2001, 9, 14), date(2001, 11, 5), date(2002, 7, 13), date(2002, 8, 4), date(2002, 9, 4), date(2002, 9, 14), date(2002, 9, 26), date(2002, 10, 3), date(2002, 10, 11), date(2003, 4, 20), date(2003, 6, 30), date(2003, 7, 25), date(2003, 8, 14), date(2003, 8, 30), date(2003, 9, 6), date(2003, 9, 13), date(2004, 8, 12), date(2004, 8, 13), date(2004, 9, 5), date(2004, 9, 13), date(2004, 9, 16), date(2004, 10, 10), date(2005, 6, 11), date(2005, 7, 6), date(2005, 7, 10), date(2005, 8, 25), date(2005, 9, 12), date(2005, 9, 20), date(2005, 10, 5), date(2005, 10, 24), date(2006, 6, 13), date(2006, 8, 30), date(2007, 5, 9), date(2007, 6, 2), date(2007, 8, 23), date(2007, 9, 8), date(2007, 9, 13), date(2007, 9, 22), date(2007, 10, 31), date(2007, 12, 13), date(2008, 7, 16), date(2008, 7, 22), date(2008, 8, 18), date(2008, 8, 31), date(2008, 9, 2), date(2009, 8, 16), date(2009, 8, 21), date(2009, 11, 9), date(2010, 6, 30), date(2010, 7, 23), date(2010, 8, 10), date(2010, 8, 31), date(2010, 9, 29), date(2011, 7, 18), date(2011, 8, 25), date(2011, 9, 3), date(2011, 10, 28), date(2011, 11, 9), date(2012, 5, 28), date(2012, 6, 23), date(2012, 8, 25), date(2012, 10, 25), date(2015, 8, 30), date(2015, 10, 1), date(2016, 6, 6), date(2016, 9, 1), date(2016, 9, 14), date(2016, 10, 7), date(2017, 6, 21), date(2017, 7, 31), date(2017, 9, 10), date(2017, 10, 29)]
print (florida_hurricane_dates[0])

dt = datetime(2025, 7, 18, 22, 24, 30, 500000)
print ("Current time {}".format(dt))

dt = datetime(year=2025, month=7, day=18, 
              hour=22, minute=24, second=30, microsecond=500000)
print ("Current time {}".format(dt))

print (colored ("## Replace part of this datetime ##", "green", attrs=['bold','underline']))
dt_hr = dt.replace(minute=0, second=0, microsecond=0)
print ("Current time {}".format(dt_hr))

# Create datetime
dt = datetime (2019, 1, 12, 15, 9, 13)
string_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")
print ("Current date in customized strftime {}".format(string_datetime))

string_datetime = dt.strftime("%H:%M:%S on %Y-%m-%d")
print ("Current date in customized strftime {}".format(string_datetime))

print ("Current date in ISO format {}".format(dt.isoformat()))

date_input = "07/20/2025 11:32:30"
dt = datetime.strptime(date_input, "%m/%d/%Y %H:%M:%S")
print ("String to date format {}".format(dt))
print ("Type of the variable {}".format(type(dt)))

# From linux time stamp to datetime format conversion
#datetime.fromtimestamp

start_date = datetime(2025, 1, 30, 11, 57, 30)
end_date = datetime(2025, 2, 20, 11, 57, 30)
duratiuon = end_date - start_date
print ("Time difference is : {}".format(duratiuon))
print ("Time difference in seconds : {}".format(duratiuon.total_seconds()))

time_delta1 = timedelta(seconds=1)
final_date = start_date + time_delta1
print ("End time after time_delta1 : {}".format(final_date))

# Timezone 
IST = timezone(timedelta(hours=5,minutes=30))
start_date = datetime(2025, 1, 30, 11, 57, 30, tzinfo=IST)
print ("IST Time:: {}".format(start_date))
# Same can be achieved like below;
start_date = datetime(2025, 1, 30, 11, 57, 30)
print (colored ("IST Time:: {}".format(start_date.astimezone(IST)), "green", attrs=['bold','underline']))
print (colored ("IST Time:: {}".format(start_date.replace(tzinfo=timezone.utc)), "green", attrs=['bold','underline']))

PST = timezone(timedelta(hours=-8))
end_date = datetime(2025, 2, 20, 11, 57, 30, tzinfo=PST)
print ("PST Time:: {}".format(end_date))
# Same can be achieved like below;
end_date = datetime(2025, 2, 20, 11, 57, 30)
print (colored ("IST Time:: {}".format(end_date.astimezone(PST)), "green", attrs=['bold','underline']))

print (colored ("Finding timezone", "green", attrs=['bold','underline']))
india_timezone = tz.gettz('Asia/Kolkata')
print (india_timezone)
pst_timezone = tz.gettz('America/New_York')
print (pst_timezone)

print (colored ("Use of the timezone info", "red", attrs=['bold','underline']))
end_date = datetime(2025, 2, 20, 11, 57, 30, tzinfo=pst_timezone)
print ("PST Time:: {}".format(end_date))
end_date = datetime(2025, 2, 20, 11, 57, 30, tzinfo=india_timezone)
print ("IST Time:: {}".format(end_date))

