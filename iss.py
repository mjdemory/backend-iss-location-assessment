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
    response.raise_for_status()
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
    iss.setheading(90)
    iss.penup()
    iss.goto(Long, Lat)
    return screen
    # screen.exitonclick()
    
    

# def overhead(long_indy, lat_indy):

    
#     parameters = {"lat": lat_indy, "long": long_indy}

#     response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

#     data = response.json

#     over_indy = data['response'][1]['risetime']

#     # return time.ctime(over_indy)
#     style = ('Arial',6,'bold')
#     # time.ctime(data['request']['risetime'])

#     return location_indy.write(time.ctime(over_indy),font=style)


def main():
    names = ''
    astro_dict = astro_info()
    for people in astro_dict:
        names += people['name'] + ', '

    print('Their names are: ' + names[:-2] + ' and they are on '+ str(people['craft']) + '.')

    print("The current number of astronauts is {}.".format(len(astro_dict)))

    Lat, Long = location()

    print("Latitude: ", Lat)
    print("Longitude: ", Long)

    screen = None
    
    screen = iss_map(Lat, Long)


    lat_indy = float(39.768452)
    long_indy = float(-86.156212)

    location_indy = turtle.Turtle()
    location_indy.penup()
    location_indy.color('yellow')
    location_indy.goto(long_indy, lat_indy)
    location_indy.dot(5)
    location_indy.hideturtle()
    # indy_pass = overhead(lat_indy, long_indy)
    # location_indy.write(indy_pass, font=style)

    if screen is not None:
        print('Click on screen to exit...')
        screen.exitonclick()
        # style = ('Arial',6,'bold')



if __name__ == '__main__':
    main()
