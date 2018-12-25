import bpy
import os
import random
import sys
from os.path import isfile

def format_from_fname(fname):
  _, ext = os.path.splitext(fname)
  ext = ext.lower()
  if ext=='.exr':
    return 'OPEN_EXR_MULTILAYER'
  elif ext=='.png':
    return 'PNG'
  sys.exit(1)

def frame_done(n):
  return isfile(output_fname_tpl % n)

def frames_todo():
  all_frames = range(bpy.context.scene.frame_start, bpy.context.scene.frame_end+1)
  return [n for n in all_frames if not frame_done(n)]

def render(frame):
  bpy.context.scene.frame_set(frame)
  bpy.context.scene.render.filepath = output_fname_tpl % (frame)
  bpy.ops.render.render(write_still=True)


output_fname_tpl = os.getenv('FRAME_FNAME','frame%04d.png')

bpy.context.user_preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'
bpy.context.scene.cycles.device = 'GPU'
bpy.context.scene.render.use_file_extension = False
bpy.context.scene.render.image_settings.file_format = os.getenv('FORMAT', format_from_fname(output_fname_tpl))

random.seed()
strict = random.randrange(3)==0
frames = frames_todo()
while len(frames)>(0 if strict else 3):
  start = random.randrange(0,len(frames))
  queue = frames[start:]+frames[0:start-1]
  for n in queue if strict else queue[:-3]:
    if frame_done(n):
      break
    render(n)
  frames = frames_todo()

