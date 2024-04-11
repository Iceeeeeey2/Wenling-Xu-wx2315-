def getBondPrice_Z(face, couponRate, times, yc):
    pvcfsum = 0
    for t, yc_rate in zip(times, yc): 
        cf = couponRate * face if t != times[-1] else couponRate * face + face  
        pv = (1 + yc_rate) ** (-t)  
        pvcf = pv * cf
        pvcfsum += pvcf
    bondprice = pvcfsum
    return(bondprice)
    
