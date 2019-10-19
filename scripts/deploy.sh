#!/bin/bash

    sam package \
        --template-file ./template.yaml \
        --output-template-file ./packaged.yaml \
        --s3-bucket "sam-assignment" \
        --region ap-south-1 

    sam deploy \
        --template-file ./packaged.yaml \
        --stack-name GetIpData-green \
        --capabilities CAPABILITY_IAM \
        --region ap-south-1