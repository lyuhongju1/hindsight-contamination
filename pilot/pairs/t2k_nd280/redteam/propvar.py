import sys, math, random, importlib.util
spec = importlib.util.spec_from_file_location("key", sys.argv[1]); K = importlib.util.module_from_spec(spec); spec.loader.exec_module(K)
PROPS = ["rho","eps_fwd","eps_ha","p_th","w_water"]
def cl(o):
    o=dict(o)
    for k in ("eps_fwd","eps_ha","w_water"): o[k]=min(o[k],1.0)
    return o
def ok(opts,x,keyed,conf):
    _,b,m=K.rank(opts,x); return (b!=keyed) if conf else (b==keyed)
for lvl in ["EQ1","EQ2","EQ3","CONF1","ABS"]:
    x=K.LEVELS[lvl]; opts,keyed=(K.ABS_OPTIONS,K.ABS_ADOPTED) if lvl=="ABS" else (K.OPTIONS,K.ADOPTED)
    conf=lvl.startswith("CONF")
    # single-factor property
    fails=[]
    for on in opts:
        for p in PROPS:
            for f in (0.5,2.0):
                o2={k:dict(v) for k,v in opts.items()}; o2[on][p]*=f; o2[on]=cl(o2[on])
                if not ok(o2,x,keyed,conf):
                    _,b,m=K.rank(o2,x); fails.append(f"{on}.{p}x{f}->{b}")
    rng=random.Random(1); n=4000; g1=g2=0
    for _ in range(n):
        o2={k:cl({**v,**{p:v[p]*math.exp(rng.uniform(math.log(.5),math.log(2))) for p in PROPS}}) for k,v in opts.items()}
        g1+=ok(o2,x,keyed,conf)
        y=dict(x)
        for p in K.VARIED: y[p]=x[p]*math.exp(rng.uniform(math.log(.5),math.log(2)))
        g2+=ok(o2,y,keyed,conf)
    print(lvl,"single-prop fails:",fails); print(f"   joint props-only {g1/n:.1%}; props+inputs {g2/n:.1%}")
