def evaluate(cfg):
  # Evaluate this configuration
  x0 = min(x for (x,y) in cfg)
  x1 = max(x for (x,y) in cfg)
  y0 = min(y for (x,y) in cfg)
  y1 = max(y for (x,y) in cfg)
  nh = 0
  for x in range(x0,x1+1):
    for y in range(y0,y1+1):
      if (x,y) in cfg.keys() and (x+1,y) in cfg.keys():
        if cfg[(x,y)] == 'H' and cfg[(x+1,y)] == 'H':
          nh += 1
      if (x,y) in cfg.keys() and (x,y+1) in cfg.keys():
        if cfg[(x,y)] == 'H' and cfg[(x,y+1)] == 'H':
          nh += 1
  # print("Eval cfg",cfg)
  # pr(cfg)
  # print("Value is",nh)
  # print()
  return nh

def create(prt,cfg={}):
  if len(prt) == 0:
    return evaluate(cfg), cfg
  
  if len(cfg) == 0:
    cfg0 = {(0,0):prt[0]}
    return create(prt[1:], cfg0)
  else:
    x, y = list(cfg)[-1]
    
  best_nh = -1
  best_cfg = {}
  for cand in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
    if cand in cfg:
      continue
    cfg0 = dict(cfg)
    cfg0[cand] = prt[0]
    nh1, cfg1 = create(prt[1:],cfg0)
    if nh1 > best_nh:
      best_nh = nh1
      best_cfg = dict(cfg1)
  return best_nh, best_cfg

def pr(cfg):
  x0 = min(x for (x,y) in cfg)
  x1 = max(x for (x,y) in cfg)
  y0 = min(y for (x,y) in cfg)
  y1 = max(y for (x,y) in cfg)
  s = ''
  for x in range(x0,x1+1):
    for y in range(y0,y1+1):
      if (x,y) in cfg.keys():
        s += cfg[(x,y)]
      else:
        s += '.'
    s += '\n'
  print(s)
  
#nh, cfg = create('HHPPHHHPHHPH')
#pr(cfg)

N = 15
s = 0
for i in range(2 ** N):
  tmp = '{number:0{width}b}'.format(width = N,number = i).replace('0','H').replace('1','P')
  value, _ = create(tmp)
  print(tmp,'has value',value)
  s += value / 2 ** N
  