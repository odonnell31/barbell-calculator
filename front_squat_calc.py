#this function gives the user a quick and dirty plan to achieve their goal front squat
def front_squat_calc(current_lift, goal_lift, body_weight):
    difference = float(goal_lift - current_lift)
    #weeks = difference/2.5
    
    week_num = 1
    while difference > 0.0:
        print "Week:",week_num
        print "5x5 front squat:",(float(current_lift)*0.8)
        print "====="
        print "Week:",week_num+1
        print "5x3 front squat:",(float(current_lift)*0.88)
        print "====="
        current_lift = current_lift + 5
        difference = difference - 5
        week_num = week_num + 2
        #print int(weeks)
    print "go for it, 1 rep!:",goal_lift

print front_squat_calc(200, 225, 168)