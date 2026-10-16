# Takes three resistance values from star network and convert them into delta network

def star_to_delta(ra, rb, rc):
    numerator = ra * rb + rb * rc + rc * ra
    rab = numerator / rc
    rbc = numerator / ra
    rca = numerator / rb
    return (round(rab, 2), round(rbc, 2), round(rca, 2))

print(star_to_delta(10, 20, 30))