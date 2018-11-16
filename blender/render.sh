#!/bin/sh
blender -b $SCENE -E CYCLES -t $THREADS -P gpu.py
