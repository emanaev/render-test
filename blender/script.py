import bpy
import os
import random
from os.path import isfile

output_fname_tpl = os.getenv('FRAME_FNAME','frame%06d')

def frame_done(n):
  return isfile(output_fname_tpl % n + ".png")

def frames_todo():
  all_frames = range(bpy.context.scene.frame_start, bpy.context.scene.frame_end+1)
  return [n for n in all_frames if not frame_done(n)]

def render(frame):
  bpy.context.scene.frame_set(frame)
  bpy.context.scene.render.filepath = output_fname_tpl % (frame)
  bpy.ops.render.render(write_still=True)

bpy.context.user_preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'
bpy.context.scene.cycles.device = 'GPU'

random.seed()
frames = frames_todo()
while len(frames):
  start = random.randrange(0,len(frames))
  queue = frames[start:]+frames[0:start-1]
  for n in queue:
    if frame_done(n):
      break
    render(n)
  frames = frames_todo()

