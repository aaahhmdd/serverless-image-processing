#!/usr/bin/env bash
STACK_NAME=ImageProcStack
TEMPLATE=deployment/template.yaml
ZIP=function.zip
ARTIFACT_BUCKET=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='UploadsBucketName'].OutputValue" --output text)

# Zip lambda code
deploy_lambda() {
  cd src || exit
  pip install -r requirements.txt -t .
  zip -r ../deployment/$ZIP .
  cd -
}

deploy_lambda
aws s3 cp deployment/$ZIP s3://$ARTIFACT_BUCKET/
aws cloudformation deploy --template-file $TEMPLATE --stack-name $STACK_NAME --capabilities CAPABILITY_IAM