def barbell_calc_kg(weight):
    #weight = weight * 0.45359237
    # Subtract the weight of the bar
    # Divide by 2 for one side of barbell
    if weight >= 20:
        weight = (weight-20)/2.0
        
        Twenty_Five = int(weight)/25
        weight = weight - (25.0*Twenty_Five)
        
        Twenty = int(weight)/20
        weight = weight - (20.0*Twenty)
        
        Fifteen = int(weight)/15
        weight = weight - (15.0*Fifteen)
        
        Ten = int(weight)/10
        weight = weight - (10.0*Ten)
        
        Five = int(weight)/5
        weight = weight - (5.0*Five)
        
        Two_Point_Five = weight/2.5
        weight = weight - (2.5*Two_Point_Five)
        
        One_Point_Two_Five = weight/1.25
        weight = weight - (1.25*One_Point_Two_Five)
        
        Point_Five = weight/0.5
        weight = weight - (0.5*Point_Five)

        Point_Two_Five = weight/0.25
        weight = weight - (0.25*Point_Two_Five)
        
        print "Required weights on each side of barbell:"
        print "25's:  ", Twenty_Five
        print "20's:  ", Twenty
        print "15's:  ", Fifteen
        print "10's:  ", Ten
        print "5's:   ", Five
        print "2.5's: ", int(Two_Point_Five)
        print "1.25's:", int(One_Point_Two_Five)
        print "0.5's: ", int(Point_Five)
        print "0.25's:", int(Point_Two_Five)
        
    elif weight > 0:
        print "hit the dumbbells.."
    
    else:
        print "invalid weight.."

#test case 1
barbell_calc_kg(100)

#test case 2
#barbell_calc(20)

#test case 3
#barbell_calc(-5)