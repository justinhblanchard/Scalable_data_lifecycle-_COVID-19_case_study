#!/bin/bash
for file in */*.csv;
do head -1 $file >> headers.csv;
done