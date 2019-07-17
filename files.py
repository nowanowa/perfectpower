import json

files = []
lines = []

with open('files.csv') as f:
  lines = f.readlines();

print '['

for line in lines:
  fil = line.strip()
  with open('perfect/'+fil) as j:
    l = json.load(j)
    print '  {"min": '+str(int(fil[0:-5])*100000)+', "max": '+str(l[-1]['a'])+', "len": '+str(len(l))+'},'

print ']'

# ls | sort -n | head -n 40 >../files.json

