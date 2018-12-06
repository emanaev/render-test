#!/bin/sh
for blend in $BLEND_DIR/*.blend; do
  nvidia-smi
  blender -b $blend -E CYCLES -t $THREADS -y -P gpu.py
done
for blend in $BLEND_DIR/*.blend; do
  nvidia-smi
  blender -b $blend -E CYCLES -t $THREADS -y -P gpu.py
done
