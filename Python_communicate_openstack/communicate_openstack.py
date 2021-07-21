#!usr/bin/python3
import argparse
import logging
import requests

from logging.handlers import RotatingFileHandler

format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

hdlr = RotatingFileHandler(filename ='opstck.log' , maxBytes=2000 , backupCount=10)

hdlr.setFormatter(format)

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(hdlr)

class Communicate_with_api:
        
        def communicate_api(self,args):
                try:
                        url1=args.endpoint + args.api
                        response=requests.request(method=args.method,url=url1,headers={"X-Auth-Token": args.token})
                except request.exceptions.InvalidURL:
                        logger.error("INVALID URL Error")
                except request.exceptions.ConnectTimeout:
                        logger.error("Connection Error")
                except request.exceptions.HTTPError:
                        logger.error("HTTP Error")
                except Exception as e:
                        logger.warning("Exception %s", e)
                print(resonse.status_code)
                print(response.headers)
                print(response.text)
        

        def main(self):
                parser=argparse.ArgumentParser()
                parser.add_argument("endpoint" , help=" Endpoint Url")
                parser.add_argument("method" , help=" HTTP request method" , choices=['GET','DELETE'] , type= str)
                parser.add_argument("api" , help="api_ref")
                parser.add_argument("token" , help="Authorized token")
                self.communicate_api(parser.parse_args())

if __name__ == "__main__":
        co=Communicate_with_api()
        co.main()
