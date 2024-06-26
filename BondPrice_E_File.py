def getBondPrice_E(face, couponRate, m, yc):
    pvcfsum = 0
    cf = couponRate * face
    for t, yc_rate in enumerate(yc, start=1):  
        pv = (1 + yc_rate) ** (-t)  
        pvcf = pv * cf
        pvcfsum += pvcf
    bondprice = pvcfsum + (1 + yc[-1]) ** (-m) * face 
    return bondprice
