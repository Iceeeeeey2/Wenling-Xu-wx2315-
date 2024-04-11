def getBondPrice(y, face, couponRate, m, ppy):
    pvcfsum = 0
    cf = couponRate / ppy * face
    for t in range(1, m * ppy+1):
        pv = (1 + y/ppy) ** (-t)  
        pvcf = pv * cf
        pvcfsum += pvcf
    bondprice = pvcfsum + (1 + y/ppy) ** (-m*ppy) * face  
    return (bondprice)

