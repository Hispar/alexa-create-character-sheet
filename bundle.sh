#!/usr/bin/env bash

cp -r ./lambda/py/* ./lambda/skill_env/

cd ./lambda/skill_env/

zip -r ../test.zip .