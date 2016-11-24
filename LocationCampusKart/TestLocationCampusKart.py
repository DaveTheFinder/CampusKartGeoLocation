#!/usr/bin/env python

from EMLID_Coordinates import CampusKartLocation

class TestLocationCK():
    
    def Test_1_CK(self):
        Location = CampusKartLocation()
        print "Starting Test..."
        print "I want to know the current coordinates of the Campus Kart\n"

        Host = raw_input("EMLID HOST IP: ")
        Port = raw_input("EMLID PORT: ")

        self.Latitude, self.Longitude, self.Altitude = Location.Coordinates(Host, Port)

        print "\nThe current location is: Latitude = ", self.Latitude, ", Longitude = ", self.Longitude, ", Altiude = ", self.Altitude

#  Execute Main Program
if __name__ == "__main__":
    main = TestLocationCK()
    main.Test_1_CK()