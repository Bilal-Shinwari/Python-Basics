'''Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. 
   For the sake of their friendship, any candies left over will be smashed. For example, 
   if they collectively bring home 91 candies, they'll take 30 each and smash 1.'''

alice=13
bob=17
carol=23

total_candies=alice+bob+carol
candies_to_smash=total_candies%3

print(f"candies to smash = {candies_to_smash} ")
