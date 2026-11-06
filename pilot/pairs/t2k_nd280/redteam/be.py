import sys, importlib.util
spec = importlib.util.spec_from_file_location("key", sys.argv[1]); K = importlib.util.module_from_spec(spec); spec.loader.exec_module(K)
for lvl,keyed,opts in [("EQ1","cube_3view",K.OPTIONS),("EQ2","cube_3view",K.OPTIONS),("EQ3","cube_3view",K.OPTIONS),("CONF1","water_grid",K.OPTIONS),("ABS","korrin_array",K.ABS_OPTIONS)]:
    x=K.LEVELS[lvl]; base=opts[keyed]["p_th"]; lose=m3=None
    for p in range(int(base),1500):
        o2={k:dict(v) for k,v in opts.items()}; o2[keyed]["p_th"]=p
        _,b,m=K.rank(o2,x)
        if m3 is None and (b!=keyed or m<3): m3=p
        if b!=keyed: lose=p; break
    print(lvl,keyed,"p_th",base,"margin<3 at",m3,"loses at",lose)
