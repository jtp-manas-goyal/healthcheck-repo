echo "This is the image tag to be used:"

if aws lambda get-function --function-name healthcheck-lambda; then
  echo "Updating Lambda function code..."
  aws lambda update-function-code --function-name healthcheck-lambda \
    --image-uri ${ACCOUNT_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/healthcheck-playwright-repo:latest
    
else
  echo "Creating new Lambda function 'healthcheck-lambda'..."
  aws lambda create-function --function-name healthcheck-lambda \
    --package-type Image \
    --code ImageUri=${ACCOUNT_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/healthcheck-playwright-repo:latest \
    --role arn:aws:iam::${ACCOUNT_ID}:role/Roleforhealthchecklambdaecsupdate \
    --region ap-northeast-1 \
    --memory-size 1024 \
    --timeout 180 
fi
