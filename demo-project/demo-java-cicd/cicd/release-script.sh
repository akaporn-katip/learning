#!/bin/bash


$id=$(curl -X 'POST' \
  'http://gitea.local.katipwork.com/api/v1/repos/demo-dhiplaos/demo-project/releases' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: token a7ff1755d78b096e1028139f1491c206ac7f6b8b' \
  -d '{
  "body": "string",
  "draft": true,
  "name": "release-via-api",
  "prerelease": true,
  "tag_name": "test-release-tagname",
  "target_commitish": "test-release-commit"
}' | jq '.id')


echo 'test - $release_id'
