#!/usr/bin/env python

__author__ = 'Michael DeMory'

import requests
import turtle
import time

def astro_info():
    response = requests.get('http://api.open-notify.org/astros.json')

    response.raise_for_status()

    return response.json() ["people"]

def location():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    location = response.json()["iss_position"]
    Lat = float(location["latitude"])
    Long = float(location["longitude"])

    return Lat, Long

def iss_map(Lat, Long):

    screen = turtle.Screen()

    screen.setup(width=720, height=360)

    screen.setworldcoordinates(-180, -90, 180, 90)

    screen.register_shape("iss.gif")

    screen.bgpic("map.gif")

    iss = turtle.Turtle()
    iss.shape("iss.gif")
    # iss.color('yellow')
    iss.setheading(90)
    iss.penup()
    iss.goto(Long, Lat)
    
    

    # Location of Indianapolis, IN
    lat_indy = float(39.768452)
    long_indy = float(-86.156212)

    location_indy = turtle.Turtle()
    location_indy.penup()
    location_indy.color('yellow')
    location_indy.goto(long_indy, lat_indy)
    location_indy.dot(5)
    location_indy.hideturtle()
    screen.exitonclick()
    return screen

def overhead():

    location_indy = turtle.Turtle()

    parameters = {"lat": 39.768452, "long": -86.156212}

    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

    data = response.json

    over_indy = data['response'][1]['risetime']



    # time.ctime(data['request']['risetime'])

    style = ('Arial',6,'bold')

    return location_indy.write(time.ctime(over_indy),font=style)


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

    iss_map(Lat, Long)

    overhead()

    
    



if __name__ == '__main__':
    main()
