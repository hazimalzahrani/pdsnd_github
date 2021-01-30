import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington).
    city=input("what city you want to check? ").lower()
    while city !='new york city' and city !='chicago' and city != 'washington':
        city=input('please choose a valid city ')
    
    #get user input for month (all, january, february, ... , june)
    
    month=input('what month you want to check, or "all" to apply no filter ').title()
    while month!='January' and month!='February' and month!='March' and month!='April' and month!='May' and month!='June' and month!="All":
        month=input("please write a valid month name ").title()
    #get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('what day of the week you want to check, or "all" to applly no filters ').title()
    while day!='Saturday' and day!='Sunday' and day!='Monday' and day!='Tuesday' and day!='Wednesday' and day!='Thursday' and day!='Friday' and day!='Saturday' and day!='All':
        day=input("please write a valid day of week name ").title()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    if city=="new york city":
        df=pd.read_csv("new_york_city.csv")
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_name()
        if month!="All":
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            month= months.index(month)+1
            df=df[df['month']==month]
        if day!= "All":
            df = df[df['day_of_week']==day.title()]
        
    if city=="chicago":
        df=pd.read_csv("chicago.csv")
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_name()
        if month!="All":
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            month= months.index(month)+1
            df=df[df['month']==month]    
        if day!= "All":
            df = df[df['day_of_week']==day.title()]
            
        
    if city=="washington":
        df=pd.read_csv("washington.csv")
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.day_name()
        if month!="All":
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            month= months.index(month)+1
            df=df[df['month']==month]
        if day!= "All":
            df = df[df['day_of_week']==day.title()]
            
      
    return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #display the most common month
    months={1:'January',2:'February',3:'March',4:'April',5:'May',6:"Juen"}
    month_stat = df['month'].mode()[0]
    Name_of_month = months.get(month_stat)
    print("most common month is {}".format(Name_of_month))

    #display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("most common day is {}".format(common_day))
    
    #display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("most common start hour is {}".format(common_hour))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("most commonly used start station is {}".format(common_start_station))

    #display most commonly used end station
    common_end_station= df['End Station'].mode()[0]
    print("most commonly used end station is {}".format(common_end_station))

    #display most frequent combination of start station and end station trip
    common_end_and_start_station = (df['Start Station']+df['End Station']).mode()[0]
    print("the most common combination of start and end stations are {}".format(common_end_and_start_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    the_sum = df['Trip Duration'].sum()
    print("the total travel time is {}".format(the_sum))


    #display mean travel time
    travel_mean = df['Trip Duration'].mean()
    print("the mean travel time is {}".format(travel_mean))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    counts_user_types = df['User Type'].value_counts()
    print("the count for user types is \n {}".format(counts_user_types))

    #Display counts of gender
    if 'Gender' in df:

        counts_gender = df['Gender'].value_counts()
        print("the counts for each Gender is\n {}".format(counts_gender))



     #Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
    
        print("the earliest year of birth is {}".format(int(earliest_birth)))

        recent_birth = df['Birth Year'].max()
        print("the most recent birth year is {}".format(int(recent_birth)))

        common_birth = df['Birth Year'].mode()[0]
        print("the most common year of birth is {}".format(int(common_birth)))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def view_data(df):
    '''Displays a request for the user to see the data table.
    Args:
        df- pandas DataFrame containg all the colums modified and added
    Returns:
        df - five rows of the DataFrame upon request'''
    view_data=input("would you like to see five rows of the data?").lower()
    start_loc=5
    old_loc=0
    while view_data=="yes":
        print(df.iloc[old_loc:start_loc])
        old_loc=start_loc
        start_loc+=5

        view_data=input("would you like to see five more rows of data?").lower()




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
