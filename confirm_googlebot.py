#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script takes a list of ip addresses from a csv file and
confirms whether or not they are truly googlebot as outlined
by Google in this post:
https://support.google.com/webmasters/answer/80553

In order to verify Googlebot, this script will:

1. Run a reverse DNS lookup on the accessing IP address from your logs, using the host command.
2. Verify that the domain name is in either googlebot.com or google.com
3. Run a forward DNS lookup on the domain name retrieved in step 1 using the host command on the retrieved domain name. Verify that it is the same as the original accessing IP address from your logs.

###
Created on Fri May 17 17:58:05 2019
@author: tylerreardon
"""

import socket
import json
 
def reverse_dns(ip_address):
    '''
    This method returns the true host name for a 
    given IP address
    '''
    host_name = socket.gethostbyaddr(ip_address)
    reversed_dns = host_name[0]
    return reversed_dns


def forward_dns(reversed_dns):
    '''
    This method returns the first IP address string
    that responds as the given domain name
    '''
    try:
        data = socket.gethostbyname(reversed_dns)
        ip = str(data)
        return ip
    except Exception:
        # fail gracefully!
        print('error')
        return False

def ip_match(ip, true_ip):
    '''
    This method takes an ip address used for a reverse dns lookup
    and an ip address returned from a forward dns lookup
    and determines if they match.
    '''
    if ip == true_ip:
        ip_match = True
    else:
        ip_match = False
    return ip_match

def confirm_googlebot(host, ip_match):
    '''
    This method takes a hostname and the results of the ip_match() method
    and determines if an ip address from a log file is truly googlebot
    '''
    googlebot = False
    if host != False:
        if host.endswith('.googlebot.com') or host.endswith('.google.com'):
            if ip_match == True:
                googlebot = True
    return googlebot
                

def run(ipList):
    real_googlebots = []
    try:
        for ip in ipList:
            host = reverse_dns(ip)
            true_ip = forward_dns(host)
            is_match = ip_match(ip, true_ip)
            result = confirm_googlebot(host, is_match)
            print(result)
            if result == True:
                real_googlebots.append(ip)
            if len(real_googlebots) > 0:
                return real_googlebots
            else:
                return False
    except:
        return False
        
    
        

        
        