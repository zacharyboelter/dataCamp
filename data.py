# # np_baseball is available

# # Import numpy
# import numpy as np

# # Print mean height (first column)
# avg = np.mean(np_baseball[:,0])
# print("Average: " + str(avg))

# # Print median height. Replace 'None'
# med = np.median(np_baseball[:, 0])
# print("Median: " + str(med))

# # Print out the standard deviation on height. Replace 'None'
# stddev = np.std(np_baseball[:, 0])
# print("Standard Deviation: " + str(stddev))

# # Print out correlation between first and second column. Replace 'None'
# corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])    #compare the first and second columns to see the correlation READ THE INSTRUCTIONS DUMMY


# # heights and positions are available as lists

# # Import numpy
# import numpy as np

# # Convert positions and heights to numpy arrays: np_positions, np_heights
# np_postitions = np.array(positions)
# np_heights = np.array(heights)


# # Heights of the goalkeepers: gk_heights
# gk_heights = np_heights[np_postitions == 'GK']

# # Heights of the other players: other_heights
# other_heights = np_heights[np_postitions != 'GK']

# # Print out the median height of goalkeepers. Replace 'None'
# print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# # Print out the median height of other players. Replace 'None'
# print("Median height of other players: " + str(np.median(other_heights)))

# #Assign fifa roles and heights to numpy arrays.
# #assign goalkeep hights and other heights
# #average of both to see if one is higher than other


# ~~~~~~~~~~~~~~~~~~~~~~~Transportation on vacation ~~~~~~~~~~~~~~~~~~~~~~

# #  After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

# Write a code that gives out the total amount for different days(d).


# def rental_car_cost(d):
#     total = d * 40
    
#     if d > 0 and d < 3:
#         return total
#     elif d >= 7:
#         return total - 50
#     else:
#         return total - 20
        

# ~~~~~~~~~~~ remove every second element from list ~~~~~~~~~~~~

def remove_every_other(my_list):
    return my_list[::2]             #this 
    pass




# seq[::n] is a sequence of each n-th item in the entire sequence.

# Example:

# >>> range(10)[::2]
# [0, 2, 4, 6, 8]

# The syntax is:

# seq[start:end:step]

# So you can do (in Python 2):

# >>> range(100)[5:18:2]
# [5, 7, 9, 11, 13, 15, 17]


