from flask import Flask
import requests
from flask import jsonify
from flask import make_response
from flask import json
import re

app = Flask(__name__)

def lambda_handler(event, context):
    # token = event['pathParameters']['proxy']
    with app.app_context():
        my_ip=event['pathParameters']['get_my_ip']
        regex_conv = re.findall("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",my_ip)
        if regex_conv:
            link="http://worldtimeapi.org/api/ip/"+ my_ip
            response=requests.get(link)
            data = response.json()
            version="v1"
            timezone=data['timezone']
            abbrevation=data['abbreviation']
            dst=data['dst']
            # response={}
            # response["my_ip"]=my_ip
            return {
                'statusCode': 200,
                'body': json.dumps({
                    "Version": version,
                    "Timezone": timezone,
                    "Abbrevation": abbrevation,
                    "dst": dst
                })
            }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    "success": "false",
                    "Message":"Please provide valid public ip"
                })
            }
    
        # regex_conv = re.findall("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",my_ip)
        # if regex_conv:
        #     link="http://worldtimeapi.org/api/ip/"+ my_ip
        #     response=requests.get(link)
        #     data = response.json()
        #     version="v1"
        #     timezone=data['timezone']
        #     abbrevation=data['abbreviation']
        #     dst=data['dst']
        #     return make_response (
        #         jsonify(
        #             {
        #                 "Version": version,
        #                 "TimeZone": timezone,
        #                 "dst": dst,
        #                 "abbreviation": abbrevation
        #             }
        #         )
        #     )
        # else:
        #     return make_response(
        #         jsonify(
        #         {
        #             "Status": "404",
        #             "Message": "No Public IP, Please append ip "
        #         }
        #     )
        # )

if __name__ == '__main__':
    app.run()