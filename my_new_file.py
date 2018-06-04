number_of_licks = int(input('Please enter the total number of licks: '))

if number_of_licks < 10:
    print('Not enough to the center of a tootsie pop - try again.')
elif number_of_licks >= 10:
    print('There are {} licks to the center of a tootsie pop.'.format(number_of_licks))
