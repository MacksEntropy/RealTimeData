# Overview

This is an application that mocks a stream of data coming from a gas pipeline. 

# Usage

First you need to start up zookeeper / kafka configured to run on localhost with the default ports. Then run `producer.py` which starts the stream of data. Running `main.py` will then tap into that stream of data, allowing for analysis.