#!/usr/bin/env bash

set -e

SCRIPT_PATH=`dirname $0`
ROOT_PATH=`( cd $SCRIPT_PATH && cd .. && pwd )`
DATA_PATH="$ROOT_PATH/data"
echo $SCRIPT_PATH
echo $ROOT_PATH
echo $DATA_PATH

[[ -d $DATA_PATH ]] || mkdir $DATA_PATH

cd $DATA_PATH
wget http://files.grouplens.org/datasets/movielens/ml-10m.zip
unzip ml-10m.zip
mv ml-10M100K/* .
rm -rf ml-10M100K
cd ..
