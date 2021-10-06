import time
import pandas as pd
import numpy as np

CITY_DATA = {'c': 'chicago.csv',
             'ny': 'new_york_city.csv',
             'w': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - number of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')



    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please select the city, type\n C for Chicago\n NY for New York City\n W for Washington: ').lower()
    while city not in CITY_DATA:
        print('Invalid answer')
        city = input('Please select the city, type\n C for Chicago\n NY for New York City\n W for Washington: ').lower()

    # TO DO: get user input for filter type (month, day or both).
    # TO DO: get user input for filter type (month, day or both).
    filter = input('Please select the data by month, day, both, or none? ').lower()
    while filter not in (['month', 'day', 'both', 'none']):
          print('Invalid answer')
          filter = input('Please select the data by month, day, both, or none? ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if filter == 'month' or filter == 'both':
       month = input('Please select the month - January, February, March, April, May, or June? ').lower()
       while month not in months:
             print('Invalid answer')
             month = input('Please select the month - January, February, March, April, May, or June? ').lower()
    else:
         month = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if filter == 'day' or filter == 'both':
       day = input('Please select the day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').title()
       while day not in days:
             print('Invalid answer')
             day = input('Please select the day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').title()
    else:
         day = 'all'

    print('-' * 40)
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

    # load data file into a dataframe
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.strftime("%A")

    # filter by month and day
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]
    else:
        month = 'all'
    if day != 'all':
        df = df[df['Day'] == day]
    else:
         day = 'all'
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month= df['Month'].mode()[0]
    print("The most common month is {}".format(popular_month))
    # TO DO: display the most common day of week
    popular_day= df['Day'].mode()[0]
    print("The most common day is {}".format(popular_day))

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['Hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['Hour'].mode()[0]
    print("The most common hour is {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most common start station is {}".format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most common end station is {}".format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = popular_trip.mode()[0]
    print("The most common frequent combination of start station and end station trip is {}".format(popular_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days = total_travel_time.days
    hours = total_travel_time.seconds // (60 * 60)
    minutes = total_travel_time.seconds % (60 * 60) // 60
    seconds = total_travel_time.seconds % (60 * 60) % 60
    print("The total travel time is {} days, {} hours, {} minutes and {} seconds".format(days, hours, minutes, seconds))

    # TO DO: display mean travel time
    average_travel_time = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    days = average_travel_time.days
    hours = average_travel_time.seconds // (60 * 60)
    minutes = average_travel_time.seconds % (60 * 60) // 60
    seconds = average_travel_time.seconds % (60 * 60) % 60
    print("The average travel time is {} days, {} hours, {} minutes and {} seconds".format(days, hours, minutes, seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print("The distributiom of user types is\n {}".format(user_types_count))
    # TO DO: Display counts of gender
    if 'Gender' in (df.columns):
        gender_count = df['Gender'].value_counts()
        print("The distribution of gender is \n {}".format(gender_count))
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in (df.columns):
        print("The earliest birth year is {} \nThe most recent birth year is {}\nThe most common birth year is {}".format(int(df['Birth Year'].min()), int(df['Birth Year'].max()), int(df['Birth Year'].mode()[0])))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    """Ask the user if he/she wants to display the raw data and print 5 rows at time"""
    display_raw = input('Would you like to check the raw data? Type yes or no\n').lower()
    filename = CITY_DATA[city]
    chunksize = 5
    while display_raw == 'yes':
        for chunk in pd.read_csv(filename, chunksize=chunksize):
            print(chunk)
            display_raw = input('Would you like to check the raw data? Type yes or no\n').lower()
            if display_raw != 'yes':
                break
        break

def main():
    """
    Main function
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart != 'yes':
            break
        print('Thank you for your time.')


if __name__ == "__main__":
    main()