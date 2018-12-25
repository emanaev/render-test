import sys
from os.path import isfile
import zipfile
#from . import blender_info

tpl="frame%04d.exr"
#tpl = sys.argv[1]
#start = int(sys.argv[2])
#mode = 'scan'
#last = 638
#start=100
start = int(sys.argv[1])
last = int(sys.argv[2])

def search_seq(start):
  n = start
  while n<=last and isfile(tpl % n):
    n = n+1
  return n-1

def scan():
  res = []
  n = start
  while n<=last:
    while n<=last and not isfile(tpl % n):
      n = n+1
    end = search_seq(n)
    if end>=n:
      res.append((n,end))
    n = end+1
  return res

def arch(zipfn,start,end):
  print("Found files %s - %s" % (tpl%start, tpl%end) )
  zf = zipfile.ZipFile("frames%d-%d.zip" % (start,end), "w", zipfile.ZIP_STORED)
  for fname in [tpl%n for n in range(start,end+1)]:
    if not isfile(fname):
      continue
    print("Adding %s" % (fname,))
    zf.write(fname, fname)
  zf.close()

sqs = scan()
print(",".join(["%d-%d"%(sq[0],sq[1]) for sq in sqs]))
done = sum([sq[1]-sq[0]+1 for sq in sqs])
total = last-start+1
print("Rendered %d/%d(%d%%) frames, %d left"%(done, total, done*100/total, total-done))
if done==total:
  arch("frames%d-%d.zip", start, last)

#for sq in scan():
#  arch("frames%d-%d.zip", sq[0], sq[1])

