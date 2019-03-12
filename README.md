# circleci-python-playing

[![CircleCI](https://circleci.com/gh/tna0y/circleci-python-playing.svg?style=svg)](https://circleci.com/gh/tna0y/circleci-python-playing)

This repo is an attempt to set the following steps up, all using **CircleCI**

1. Build and run docker-compose, make it accessible from the original CI machine ;
2. Run pytest on the original machine for unit tests;
3. Run pytest to connect to the docker-compose containers and test remote functionality;
4. If all goes well, upload the images to the docker hub.