import random

def split_training_testing(ls, p_test):
    """Splits a list into training and testing sets based on the given percentage.
    Returns a training set list and testing set list."""

    # Checking data types, non-negative value for percent, and list length
    assert type(ls) == list, "Input for data must be a list."
    assert isinstance(p_test, (int, float)), "Percentage must be numeric."
    assert 0 <= p_test <= 100, "Percentage must be between 0 and 100."
    assert len(ls) > 0, "List must be non-empty."

    # Designating test size from percentage given
    test_size = int((p_test / 100) * len(ls))

    # Making a copy of the list to avoid altering original
    ls_copy = ls[:]

    # Randomize list elements order
    random.shuffle(ls_copy)

    # Assign the test_size based off percentage to be test data
    # The remaining is the training data points
    testing_set = ls_copy[:test_size]
    training_set = ls_copy[test_size:]

    # Return both sets as lists
    return training_set, testing_set

def confusion_matrix(predicted, actual, pos_class):
    """Takes in a list of predicted values, actual value and the value of the positive
    class. 
    Any value not equal to pos_class is treated as belonging to the negative class.
    Returns the number of true positives, false positives, true negatives, and false negatives.
    """

    # Checking data types and list lengths
    assert type(predicted) == list, "Predicted must be a list."
    assert type(actual) == list, "Actual must be a list."
    assert len(predicted) == len(actual), "Lists must be the same length."
    assert len(predicted) > 0, "Lists cannot be empty."
    
    # Initialize all cases to 0
    TP = FP = TN = FN = 0

    # Iterate through each case in predicted
    for i in range(len(predicted)):

        p = predicted[i]
        a = actual[i]

        # If predicted value is in positive class
        if p == pos_class:
            # Add true positive if actual is also in positive
            if a == pos_class:
                TP += 1
            # False positive add if actual not in positive
            else:
                FP += 1
        # If predicted value not in positive class
        else:
            # Add false negative if actual is in positive                       
            if a == pos_class:
                FN += 1
            # Add true negative if actual is also not in positive class
            else:
                TN += 1

    return TP, FP, TN, FN

def accuracy(TP, FP, TN, FN):
    """Computes and returns the proportion of predictions that were correct. 
    """

    # Making sure all values non-negative
    assert TP >= 0 and FP >= 0 and TN >= 0 and FN >= 0

    denom = TP + TN + FP + FN

    # Returning nan if denominator is 0
    try:
        return (TP + TN) / denom
    except ZeroDivisionError:
        return float('nan')

def sensitivity(TP, FN):
    """ Computes and returns the portion of positives that are correctly identified.
    """

    # Making sure all values non-negative
    assert TP >= 0 and FN >= 0, "Inputs must be non-negative."
    
    denom = TP + FN
    
    # Returning nan if denominator is 0
    try:
        return TP / denom 
    except ZeroDivisionError:
        return float('nan')   

def specificity(FP, TN):
    """Computes and returns the proportion of negatives that are correctly identified.
    """

    # Making sure all values non-negative
    assert FP >= 0 and TN >= 0, "Inputs must be non-negative."
    
    denom = TN + FP

    # Returning nan if denominator is 0
    try:
        return TN / denom 
    except ZeroDivisionError:
        return float('nan')  

def pos_pred_val(TP, FP):
    """Computes and returns the probability that a data point identified as 
    positive is truly positive.
    """

    # Making sure all values non-negative
    assert TP >= 0 and FP >= 0, "Inputs must be non-negative."
    
    denom = TP + FP

    # Returning nan if denominator is 0
    try:
        return TP / denom 
    except ZeroDivisionError:
        return float('nan')  

def neg_pred_val(TN, FN):
    """Computes and returns the probability that a data point identified as 
    negative is truly negative.
    """

    # Making sure all values non-negative
    assert TN >= 0 and FN >= 0, "Inputs must be non-negative."

    denom = TN + FN

    # Returning nan if denominator is 0
    try:
        return TN / denom 
    except ZeroDivisionError:
        return float('nan')  

def print_eval_metrics(pred_vals, actual_vals, pos_class):
    """Takes in a list of predicted values, actual values and the positive class value.
    Prints each evaluation (accuracy, sensitivity, specificity, positive predictive value,
    and negative predictive value).
    """

    # Checking data types and list lengths
    assert type(pred_vals) == list, "Predicted vals must be a list."
    assert type(actual_vals) == list, "Actual vals must be a list."
    assert len(pred_vals) == len(actual_vals), "Lists must be same length."
    assert len(pred_vals) > 0, "List should be non-empty."

    TP, FP, TN, FN = confusion_matrix(pred_vals, actual_vals, pos_class)

    # Saving all evaluations
    acc = accuracy(TP, FP, TN, FN)
    sens = sensitivity(TP, FN)
    spec = specificity(FP, TN)
    ppv = pos_pred_val(TP, FP)
    npv = neg_pred_val(TN, FN)

    # Print output for evaluations
    print("Accuracy:", acc)
    print("Sensitivity:", sens)
    print("Specificity:", spec)
    print("Positive predictive value:", ppv)
    print("Negative predictive value:", npv) 