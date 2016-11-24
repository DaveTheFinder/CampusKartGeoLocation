#!/usr/bin/env python

"""
Program: EMLID_Coordinates
Authors: David Ernesto Sáenz Sáenz & Aaron de Santiago Maldonado
Date: Aug - Dec 2016

Listing Contents:
            Class CampusKartLocation:
                Purpose: Retrieve the location data from the EMLID RTK Device
                Limitations: The EMLID RTK's IP and PORT must be previously known.
                             NOTE: By default, the EMLID RTK is configured at the 9001.
                                   But this can be changed at the EMLID RTK Web interface.
                                   IP must be know. It is suggested that the device is
                                   connected in a closed network.
                Def Coordinates(self, host_ip, port):
                    Purpose: To retrieve the location data from the EMLID RTK TCP/IP Socket.
                    Limitations: Extracts the data(coordinates) once at a time.
                                 For a continuously data extraction, call this method within
                                 a 'For' or 'While' loop.
                                 Data is received in one line, separated by blank spaces.
                                 It is splitted within the method, but for further specific
                                 use, you skip the split and return the full string. 

    Class declarations:
        CampusKartLocation()
        
"""

import socket

class CampusKartLocation():

    def Coordinates(self, host_ip, port):

        #  IP & Port from the EMLID RTK Device
        TCP_IP = host_ip
        TCP_PORT = int(port)

        """
        The suggested Buffer Size is 1024.
        Modify this varible if needed.
        """
        BUFFER_SIZE = 1024

        #  Simple message to be send. Not a critial part.
        MESSAGE = "HearBeat"

        #  Socket initialization and connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((TCP_IP, TCP_PORT))
        sock.send(MESSAGE)

        #  Data received from the socket
        raw_data = sock.recv(BUFFER_SIZE)

        """
        Array with the data splitted.
        The Data is received as a whole String
        separated by blank spaces.  
        """ 
        Data = raw_data.split()

        """
        The location Data are in these Array's
        position. More Data be obtained from
        the device. Check the EMLID RTK Documentation
        for more in-depth.
        """
        Latitude = Data[2]
        Longitude = Data[3]
        Altitude = Data [4] 

        sock.close()

        return Latitude, Longitude, Altitude

#  Execute Main Program
if __name__ == "__main__":
    main = CampusKartLocation()
    main.Coordinates()