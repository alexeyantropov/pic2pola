#!/bin/bash -x -e

PYTHON="${HOME}/miniconda/envs/pic2pola/bin/python"

$PYTHON ./src/main.py --img ./tests/IMG_0654.jpeg --date "Nov 2025" --geo "Turkie, the Pear " --hashtags "vacation,travel" --caption "Amazing trip!"

open polaroid_IMG_0654.jpeg
