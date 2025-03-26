echo "This is the image tag to be used: $SHA"
echo "SHA: $SHA"
echo "ACCOUNT_ID: $ACCOUNT_ID"
echo "REGION_ID: $REGION_ID"

if aws lambda get-function --function-name healthcheck-lambda; then
  echo "Updating Lambda function code..."
  aws lambda update-function-code --function-name healthcheck-lambda \
    --image-uri ${ACCOUNT_ID}.dkr.ecr.${REGION_ID}.amazonaws.com/lambda-from-container-image:$SHA
else
  echo "Creating new Lambda function 'healthcheck-lambda'..."
  aws lambda create-function --function-name healthcheck-lambda \
    --package-type Image \
    --code ImageUri=${ACCOUNT_ID}.dkr.ecr.${REGION_ID}.amazonaws.com/lambda-from-container-image:$SHA \
    --role arn:aws:iam::${ACCOUNT_ID}:role/Roleforhealthchecklambdaecsupdate \
    --region ${REGION_ID}
fi