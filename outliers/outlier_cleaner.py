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
    residual = abs(predictions - net_worths)[:, 0]
    a = ages[:, 0]
    n = net_worths[:, 0]
    keepN = len(ages) - len(ages)*0.1
    partition = numpy.argpartition(residual, keepN)
    return zip(a[partition][:keepN], n[partition][:keepN], residual[partition][:keepN])
    
