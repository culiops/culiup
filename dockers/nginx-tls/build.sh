#!/bin/bash

VERSION=$1

if [[ -z "${VERSION}" ]]; then
  echo "VERSION of image need to be set"
  exit 1
fi

docker build -m 4g -t kmetric/nginx:$VERSION .

docker tag kmetric/nginx:$VERSION cloud.canister.io:5000/chipgata/kmetric-nginx:$VERSION

docker push cloud.canister.io:5000/chipgata/kmetric-nginx:$VERSION
