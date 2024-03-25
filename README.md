# Image API

This is a API I need for a project. It's generic enough so I made it public.

## Why Python?

Because OpenCV is way easier to use in Python.

## Should I use this?

If you really want, no guarantees though.

## Usage

You need to have [poppler](https://poppler.freedesktop.org/) installed.

```bash
pip3 install -r requirements.txt
python3 main.py
```

The easies way is docker:

```SH
docker build -t image-api .
docker run -d -p 8000:8000 image-api
```

## Configuration

If you want to restrict access you can set the API_KEY environment variable. <br /> This key will then  be required for every request.
