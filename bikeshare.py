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
    print('Let\'s explore US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    getCity = input('Enter City: ...\nChicago, New York City, Washington\n\nINPUT: ').lower()
    
    while getCity not in ['chicago', 'new york city', 'washington']:
        getCity = input('NOT A VALID INPUT.\n\nEnter City: ...\nChicago, New York City, Washington\n\nINPUT: ')
    

    # TO DO: get user input for month (all, january, february, ... , june)
    getMonth = input('\nEnter Month: ...\nFrom "January" to "June" or "all" to choose all months.\n\nINPUT: ').lower()
    
    while getMonth not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        getMonth = input('NOT A VALID INPUT.\n\nEnter Month: ...\nFrom "january" to "june" or "all" to choose all months.\n')

                              
    
     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    getDay = input('\nEnter Day: ...\nFrom "Sunday" to "Saturday" or "all" to choose all days of the week.\n\nINPUT: ').lower()
    
    while getDay not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
        getDay = input('NOT A VALID INPUT.\n\nEnter Day: ...\nFrom "Sunday" to "Saturday" or "all" to choose all days of the week.\n\nINPUT:')
    
    
    
    print('-'*40)
    return getCity, getMonth, getDay

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    # extract month from Start Time to create month column
    df['month'] = df['Start Time'].dt.month
     # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] ==  month]
    
    
    
    # extract and day of week from Start Time to create month column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    
    return df


def time_stats(df):
    """The most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month: ' +str(df['month'].mode()[0]))     
 
    # TO DO: display the most common day of week
    print('The most common day of the week: ' +str(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('The most common hour: '+str(df['Start Time'].dt.hour.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """The most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    print('The most common Start Station: {}'.format(df['Start Station'].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    print('The most common End Station: {}'.format(df['End Station'].value_counts().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ " -- " + df['End Station']
    print("The most common Start and End station: {}".format(
        df['routes'].value_counts().idxmax())
    )
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """The total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    
    print('Mean travel time: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Bikeshare users Statistics."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('user types:\n{}'.format(df['User Type'].value_counts()))
    
    
    # TO DO: Display counts of gender
    if 'Gender' in list(df.columns):
        print('\nCounts of Gender:\n{}'.format(df['Gender'].value_counts(dropna = False)))
    else: 
        print('Error')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    # Earliest Year of Birth
    if 'Birth Year' in list(df.columns):
        # Earliest Year of Birth
        print('\nEarliest Year of Birth :{}'.format(int(df['Birth Year'].min())))
        
        # Most Recent Year of Birth
        print('Most Recent Year of Birth :{}'.format(int(df['Birth Year'].max())))
        
        #Most Common Year of Birth
        print('Most Common Year of Birth :{}'.format(int(df['Birth Year'].mode().values[0])))
    else : 
        print('\nEarliest Year of Birth : Error\nMost Recent Year of Birth : Error\nMost Common Year of Birth : Error')
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_rdata(df):
    first_row = 0
    last_row   = 5
    display_data = input("Do you want to display the raw data?: ").lower()

    if display_data == 'yes':
        while last_row <= df.shape[0] - 1:

            print(df.iloc[first_row:last_row,:])
            first_row += 5
            last_row   += 5

            display_more = input("Do you want to display more data ?: ").lower()
            if display_more == 'no':
                break
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rdata(df)
       
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
