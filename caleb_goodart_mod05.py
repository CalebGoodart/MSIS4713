#! python3
# Program by Caleb Goodart
# MSIS4713
# Mod05
import sys

list_of_info = {'Weezer': {'Jan 30, 2018': ['Concrete Gold', 'Etihad Stadium', 'Melbourne, VIC'],
                           'Jun 16, 2018': ['Montebello Rockfest 2018', 'Montebello Marina', 'Montebello, QC']},
                'Tenacious D': {'May 06, 2018': ['Shaky Knees Music Festival 2018', 'Central Park', 'Atlanta, GA'],
                                'Jun 16, 2018': ['Montebello Rockfest 2018', 'Montebello Marina', 'Montebello, QC']},
                'Lamb of God': {
                    'Jun 09, 2018': ['Final World Tour: North America 2018', 'Keybank Pavilion', 'Burgettstown, PA'],
                    'Jun 16, 2018': ['Montebello Rockfest 2018', 'Montebello Marina', 'Montebello, QC']},
                'Ed Sheeran': {
                    'Mar 10, 2018': ['Ed Sheeran with Missy Higgins', 'Etihad Stadium', 'Melbourne, VIC']},
                'Cold War Kids': {'Jun 02, 2018': ['XFEST 2018', 'Keybank Pavilion', 'Burgettstown, PA']},
                'Steel Panther': {'Oct 21, 2017': ['Aftershock', 'Discovery Park', 'Sacramento, CA']}}

while True:
    for i in list_of_info:
        print(i)
        for j in list_of_info[i]:
            print("\t" + j)
            for k in range(len(list_of_info[i][j])):
                print("\t\t" + list_of_info[i][j][k])

    if input("Enter Y if you would like to add more events: ") == "Y":
        while True:
            new_band = input("Artist or Band: ")
            new_concert = input("Concert: ")
            new_date = input("Date: ")
            new_venue = input("Venue: ")
            new_local = input("Location: ")

            if new_band not in list_of_info:
                list_of_info.setdefault(new_band, {new_date: [new_concert, new_venue, new_local]})
            else:
                list_of_info[new_band][new_date] = [new_concert, new_venue, new_local]

            if input("q to stop, anything else to continue: ") == "q":
                break

    else:
        sys.exit()
