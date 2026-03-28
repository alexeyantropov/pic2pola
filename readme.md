<!-- TOC -->

- [pic2pola](#pic2pola)
- [How to run](#how-to-run)
- [Develop](#develop)

<!-- /TOC -->

# pic2pola

A simple script for getting Polaroid-style image for printing. Requires Pillow and loguru.

# How to run
It's only tested on mac os with miniconda, you need to install Python with Pillow before.

An example:
```bash
./tests/example.sh
```

Process a real image image:
```bash
./pic2pola --img tests/IMG_0654.jpeg
```

How to add additional info on the picture, see help:
```bash
$ ./pic2pola -h
usage: main.py [-h] --img IMG [--date DATE] [--geo GEO] [--hashtags HASHTAGS] [--caption CAPTION]

Convert a picture into a Polaroid-style photo with optional captions.

options:
  -h, --help           show this help message and exit
  --img IMG            Path to the input image file.
  --date DATE          Date of the event.
  --geo GEO            Geolocation information (e.g. "Paris, France"
  --hashtags HASHTAGS  Comma-separated list of hashtags (e.g. "vacation,travel,photo")
  --caption CAPTION    Additional caption text
```

# Develop
Python setup:
```sh
curl -o /tmp/m.sh -s https://repo.anaconda.com/miniconda/Miniconda3-py311_26.1.1-1-MacOSX-arm64.sh && bash /tmp/m.sh -b -p $HOME/miniconda && rm -rf /tmp/m.sh
```

Env create or update:
```sh
~/miniconda/bin/conda env create -f ./develop/miniconda.yml
```
```sh
~/miniconda/bin/conda env update -f ./develop/miniconda.yml
```