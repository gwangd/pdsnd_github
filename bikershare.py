# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:37:26 2018

@author: JD
"""
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
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        while True:
          city=input('Please enter the name of the city that you want to explore. Choose: Chicago, New York City, or Washington')
          if city.lower() not in ['chicago','new york city','washington']:
                 print("Please choose one of the three cities")

          else: 
                 city=city.lower()
                 break
        print('You select {}'.format(city.title()))

        # TO DO: get user input for month (all, january, february, ... , june)
        while True:
            months=['jan','feb','mar','apr','may','jun','all']
            month=input("Select a month you want to explore: Jan, Feb, Mar, Apr, May, Jun or \"All\"")
            if month.lower() not in months:
                print("Please Choose one of the valid months, or \"All\"")
            else:
                month=month.lower()
                break

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            day=input("Choose the day of the week by entering three letter expression\
                      :Mon, Tue, Wed , etc. ; or \"All\"")
            days=['mon','tue','wed','thu','fri','sat','sun','all']
            day=day.lower()
            if day not in days:
                print("Please choose a valid day, or \"All")
            else:
                day=days.index(day)
                break

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
        df=pd.read_csv(CITY_DATA[city])
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['month']=df['Start Time'].dt.month
        df['day_of_week']=df['Start Time'].dt.weekday
        df['hour']=df['Start Time'].dt.hour
        months=['all','jan','feb','mar','apr','may','jun']
        if month!='all':
            month=months.index(month)
            df=df[df['month']==month]

        if day !=7:
            df=df[df['day_of_week']==day]

        return df


def time_stats(df):
        """Displays statistics on the most frequent times of travel."""

        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # TO DO: display the most common month
        most_common_month = df['month'].mode()
        print("The most common month is :", most_common_month)


        # TO DO: display the most common day of week
        most_common_day = df['day_of_week'].mode()
        print("The most common day of week is :", most_common_day)

        # TO DO: display the most common start hour
        most_common_start_hour = df['hour'].mode()
        print("The most common start hour is :", most_common_start_hour)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def station_stats(df):
        """Displays statistics on the most popular stations and trip."""

        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # TO DO: display most commonly used start station
        most_common_start_station = df['Start Station'].mode()[0]
        print("The most commonly used start station :", most_common_start_station)

        # TO DO: display most commonly used end station
        most_common_end_station = df['End Station'].mode()[0]
        print("The most commonly used start station :", most_common_start_station)

        # TO DO: display most frequent combination of start station and end station trip
        most_frequent_combination_station=df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)
        s=most_frequent_combination_station['Start Station'].iloc[0]
        e=most_frequent_combination_station['End Station'].iloc[0]
        print('Most Popular Combination of Start and End Stations: Start: {} End {}'.format(s,e))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def trip_duration_stats(df):
        """Displays statistics on the total and average trip duration."""

        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # TO DO: display total travel time
        total_travel_time = df['Trip Duration'].sum()
        print("Total travel time :", total_travel_time)

        # TO DO: display mean travel time
        mean_travel_time = df['Trip Duration'].mean()
        print("Mean travel time :", mean_travel_time)


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def user_stats(df):
        """Displays statistics on bikeshare users."""

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        counts_user_types=df.groupby(['User Type']).sum()
        print("Counts of User Types :",counts_user_types)

        # TO DO: Display counts of gender
        if 'Gender' in df.columns:
            counts_gender=df['Gender'].value_counts()
            print("Counts of Gender :", counts_gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df.columns:
            earliest_year=df['Birth Year'].max()
            recent_year=df['Birth Year'].min()
            common_year=df['Birth Year'].mode()
            print('The earliest birth year is: {}'.format(earliest_year))
            print('The most recent birth year is: {}'.format(recent_year))
            print('The most common birth year is: {}'.format(common_year))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_data(df, current_line):
        display = input('\nWould you like to view individual trip data?'
                        ' Type \'yes\' or \'no\'.\n')
        display = display.lower()
        if display == 'yes':
            print(df.iloc[current_line:current_line+5])
            current_line += 5
            return display_data(df, current_line)
        if display == 'no':
            return
        else:
            print("\nI'm sorry, I'm not sure about whether you wanted to see more data. Let's try again.")
            return display_data(df, current_line)


def main():
        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
        main()
