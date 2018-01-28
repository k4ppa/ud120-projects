#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    ### your code goes here

    data = [(age[0], net[0], pred[0] - net[0]) for pred, net, age in zip(predictions, net_worths, ages)]
    ordered_data = sorted(data, key=lambda tup: tup[2])
    print ordered_data
    cleaned_data = ordered_data[:81]
    print cleaned_data

    return cleaned_data

