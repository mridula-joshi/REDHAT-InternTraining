#!usr/bin/python3
import sys
import requests

def communicate_api(endpoint,method,api,token):
        try:
                url1=endpoint + api
                response=requests.request(method=method,url=url1,headers={"X-Auth-Token": token})
        except Exception as e:
                print(e)
                return
        print(response.text)

arguments=sys.argv
communicate_api(arguments[1],arguments[2],arguments[3],arguments[4])

