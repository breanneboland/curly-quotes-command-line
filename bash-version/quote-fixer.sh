#!/bin/bash

input=$1

input1=${input//“/\"}
input2=${input1//”/\"}
input3=${input2//‘/\'}
input4=${input3//’/\'}

echo $input4
# First version: echo fixed string.
# Next version: have handler for submitted file
# and having a new file as output, new file name
# as $3
