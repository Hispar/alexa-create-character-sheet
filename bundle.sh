#!/usr/bin/env bash

cp -r ./lambda/py/* ./lambda/skill_env/

cp -r ./weasyprint_for_awslambda/* ./lambda/skill_env/

cd ./lambda/skill_env/

zip -r ../test.zip .