# Calculates theoretical voltage drop, and actual voltage drop when load is attached with the source.

def loaded_divider(vs, r1, r2, rl):
    
    v_unloaded = vs * r2 / (r1 + r2)

    rp = (r2 * rl) / (r2 + rl)

    v_loaded = vs * rp / (r1 + rp)

    return (round(v_unloaded, 2), round(v_loaded, 2))

print(loaded_divider(12, 1000, 1000, 500))