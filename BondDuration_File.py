def getBondDuration(y, face, couponRate, m, ppy):
    pvcfsum = 0
    cf = couponRate / ppy * face
    for t in range(1, m * ppy + 1):
        pv = (1 + y / ppy) ** (-t)
        pvcf = pv * cf
        pvcfsum += pvcf
    bondprice = pvcfsum + (1 + y / ppy) ** (-m * ppy) * face

    weighted_sum = 0
    cf = couponRate / ppy * face
    for t in range(1, m * ppy + 1):
        pv = (1 + y / ppy) ** (-t)
        pvcf = pv * cf
        weighted_sum += t * pvcf + (1 + y / ppy) ** (-m * ppy) * face
    
    bondDuration = weighted_sum / bondprice
    return(bondDuration)
