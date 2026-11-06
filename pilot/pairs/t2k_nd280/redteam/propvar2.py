import sys, math, random, importlib.util
spec = importlib.util.spec_from_file_location("key", sys.argv[1]); K = importlib.util.module_from_spec(spec); spec.loader.exec_module(K)
PROPS = ["rho","eps_fwd","eps_ha","p_th","w_water"]
cl=lambda o:{**o,**{k:min(o[k],1.0) for k in ("eps_fwd","eps_ha","w_water")}}
for lvl,keyed,opts in [("EQ1","cube_3view",K.OPTIONS),("CONF1","water_grid",K.OPTIONS),("ABS","korrin_array",K.ABS_OPTIONS)]:
    x=K.LEVELS[lvl]
    for f in (0.5,2.0):
      for on in opts:
        for p in PROPS:
            o2={k:dict(v) for k,v in opts.items()}; o2[on][p]*=f; o2[on]=cl(o2[on])
            _,b,m=K.rank(o2,x)
            if b!=keyed or m<3: print(lvl,f"{on}.{p}x{f}: winner {b} margin {m:.2f}")
    rng=random.Random(2); n=4000; w=w3=0
    for _ in range(n):
        o2={k:cl({**v,**{p:v[p]*math.exp(rng.uniform(math.log(.5),math.log(2))) for p in PROPS}}) for k,v in opts.items()}
        _,b,m=K.rank(o2,x); w+=b==keyed; w3+=(b==keyed and m>=3)
    print(lvl,f"props-only joint: {keyed} wins {w/n:.1%}, wins with margin>=3 {w3/n:.1%}")
