#!/bin/bash

kafka-console-consumer --bootstrap-server localhost:9092 --topic com.udacity.sfcrimes.v1 --from-beginning