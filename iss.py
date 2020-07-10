#!/usr/bin/env python

__author__ = 'Michael DeMory'

import requests
import turtle

def astro_info():
    response = requests.get('http://api.open-notify.org/astros.json')

    response.raise_for_status()

    return response.json() ["people"]

def location():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    location = response.json()["iss_position"]
    Lat = location["latitude"]
    Long = location["longitude"]

    return Lat, Long

def iss_map():

    screen = turtle.Screen()

    screen.setup()


def main():
    names = ''
    astro_dict = astro_info()
    for people in astro_dict:
        names += people['name'] + ', '

    print('Their names are: ' + names[:-2] + '.')

    print("The current number of astronauts is {}.".format(len(astro_dict)))

    Lat, Long = location()

    print("Latitude: ", Lat)
    print("Longitude: ", Long)





if __name__ == '__main__':
    main()
