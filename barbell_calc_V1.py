def barbell_calc(weight):
    # Subtract the weight of the bar
    # Divide by 2 for one side of barbell
    weight = (weight-45)/2.0
    
    Fourty_Five = int(weight)/45
    weight = weight - (45.0*Fourty_Five)
    
    Twenty_Five = int(weight)/25
    weight = weight - (25.0*Twenty_Five)
    
    Ten = int(weight)/10
    weight = weight - (10.0*Ten)
    
    Five = int(weight)/5
    weight = weight - (5.0*Five)
    
    Two_Point_Five = weight/2.5
    weight = weight - (2.5*Two_Point_Five)
    
    One_Point_Two_Five = weight/1.25
    weight = weight - (1.25*One_Point_Two_Five)
    
    print "Required weights on each side of barbell:"
    print "45's:  ", Fourty_Five
    print "25's:  ", Twenty_Five
    print "10's:  ", Ten
    print "5's:   ", Five
    print "2.5's: ", int(Two_Point_Five)
    print "1.25's:", int(One_Point_Two_Five)
    
barbell_calc(305)