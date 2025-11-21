import unittest
import math
import class_eval

class TestSplitTrainingTesting(unittest.TestCase):
    """Tests split_training_testing function in class_eval."""

    def test_split_even_list(self):

        # Test splitting for even length list
        data = [1,2,3,4,5,6]
        train, test = class_eval.split_training_testing(data, 50)
        self.assertEqual(len(test), 3, "The even list test failed.")
        self.assertEqual(len(train), 3, "The even list test failed.")

    def test_split_odd_list(self):

        # Test splitting for odd length list with even percentage
        data = [1,2,3]
        train, test = class_eval.split_training_testing(data, 50)
        self.assertEqual(len(test), 1, "The odd list test failed.")
        self.assertEqual(len(train), 2, "The odd list test failed.")

    def test_split_zeros(self):

        # Test splitting for list of zeros
        data = [0,0,0,0,0,0]
        train, test = class_eval.split_training_testing(data, 50)
        self.assertEqual(len(test), 3, "The zeros list test failed.")
        self.assertEqual(len(train), 3, "The zeros list test failed.")

    def test_split_floats(self):

        # Test splitting for list of floats
        data = [1.2, 1.3, 1.4, 1.5]
        train, test = class_eval.split_training_testing(data, 25)
        self.assertEqual(len(test), 1, "The floats list test failed.")
        self.assertEqual(len(train), 3, "The floats list test failed.")

    def test_split_empty(self):

        # Test splitting for empty list
        data = []
        with self.assertRaises(AssertionError, msg="Empty list test failed."):
            class_eval.split_training_testing(data, 25)
        
    def test_split_strings(self):

        # Test splitting for string list
        data = ['a', 'b', 'c']
        train, test = class_eval.split_training_testing(data, 50)
        self.assertEqual(len(test), 1, "The string list test failed.")
        self.assertEqual(len(train), 2, "The string list test failed.")

    def test_split_invalid(self):

        # Test splitting for one invalid entry
        data = [1, 2, 'z']
        train, test = class_eval.split_training_testing(data, 50)
        self.assertEqual(len(test), 1, "Mixed type list test failed.")
        self.assertEqual(len(train), 2, "Mixed type list test failed.")

    def test_split_zero_percent(self):
        # 0% test set - all data should go to training
        data = [1, 2, 3, 4]
        train, test = class_eval.split_training_testing(data, 0)
        self.assertEqual(len(test), 0, "The zero percent test failed.")
        self.assertEqual(len(train), 4, "The zero percent test failed.")

    def test_split_hundred_percent(self):
        # 100% test set - all data should go to testing
        data = [1, 2, 3, 4]
        train, test = class_eval.split_training_testing(data, 100)
        self.assertEqual(len(test), 4, "The hundred percent test failed.")
        self.assertEqual(len(train), 0, "The hundred percent test failed.")

class TestConfusionMatrix(unittest.TestCase):
    """Tests confusion_matrix function in class_eval.
    """

    def test_basic_case(self):
        # Test for basic case

        predicted = [1,0,1,0]
        actual = [1,0,0,1]
        TP, FP, TN, FN = class_eval.confusion_matrix(predicted, actual, 1)
        self.assertEqual((TP, FP, TN, FN), (1,1,1,1), "Basic Confusion Matrix Test failed.")

    def test_unequal_lengths(self):
        # Test for case with unequal list lengths

        predicted = [1,0,1]
        actual = [1,0]
        with self.assertRaises(AssertionError,msg="Mismatched lengths confusion matrix test failed to raise AssertionError."):
            class_eval.confusion_matrix(predicted, actual, 1)

    def test_strings_case(self):
        # Test for string contents
        predicted = ['y', 'n', 'y']
        actual = ['y', 'y', 'n']
        TP, FP, TN, FN = class_eval.confusion_matrix(predicted, actual, 'y')
        self.assertEqual((TP, FP, TN, FN), (1,1,0,1), "Strings data confusion matrix test failed.")


    def test_all_positives(self):
        # Tests for all data in positive class

        predicted = [1,1,1,1,1]
        actual = [1,1,1,1,1]
        TP, FP, TN, FN = class_eval.confusion_matrix(predicted, actual, 1)
        self.assertEqual((TP, FP, TN, FN), (5,0,0,0), "All-positives Confusion Matrix Test failed.")

    def test_all_negatives(self):
        # Tests for all data not in positive class

        predicted = [0,0,0,0,0]
        actual = [0,0,0,0,0]
        TP, FP, TN, FN = class_eval.confusion_matrix(predicted, actual, 1)
        self.assertEqual((TP, FP, TN, FN), (0,0,5,0), "All-negatives Confusion Matrix Test failed.")

    def test_opposites(self):
        # Tests for predicted values opposite actual values

        predicted = [1, 0, 1, 0]
        actual = [0, 1, 0, 1]
        TP, FP, TN, FN = class_eval.confusion_matrix(predicted, actual, 1)
        self.assertEqual((TP, FP, TN, FN), (0,2,0,2), "Opposite predicted and actual values confusion matrix test failed.")

    def test_empty_lists(self):
        # Tests for empty lists data 

        predicted = []
        actual    = []
        with self.assertRaises(AssertionError, msg="Empty lists should raise AssertionError."):
            class_eval.confusion_matrix(predicted, actual, 1)

class TestEvalMetrics(unittest.TestCase):
    """Tests Evaluation Metric functions in class_eval:
    accuracy, sensitivity, specificity, pos_pred_value, and neg_pred_value functions.
    """

    # Accuracy Tests
    def test_accuracy_basic(self):

        # Tests for standard case in accuracy
        acc = class_eval.accuracy(1, 2, 4, 5)
        self.assertAlmostEqual(acc, 5/12, "Accuracy basic test failed.")

    def test_accuracy_zeros(self):

        # Tests for zero division in accuracy
        acc = class_eval.accuracy(0, 0, 0, 0)
        self.assertTrue(math.isnan(acc), "Accuracy zeros test failed.")

    def test_accuracy_negatives(self):

        # Tests for negative error in accuracy
        with self.assertRaises(AssertionError):
            class_eval.accuracy(0,1,-1,0)

    # Sensitivity Tests
    def test_sensitivity_basic(self):

        # Tests for standard case in sensitivity
        sens = class_eval.sensitivity(3, 1)
        self.assertAlmostEqual(sens, 3/4, "Sensitivity basic test failed.")

    def test_sensitivity_zeros(self):

        # Tests for zero division case in sensitivity
        sens = class_eval.sensitivity(0, 0)
        self.assertTrue(math.isnan(sens), "Sensitivity zeros test failed.")

    def test_sensitivity_negatives(self):
       
        # Tests for negatives case in sensitivity
        with self.assertRaises(AssertionError):
            class_eval.sensitivity(-1, 2)

    # Specificity Tests 
    def test_specificity_basic(self):

        # Test for basic case in specificity
        spec = class_eval.specificity(5, 7)
        self.assertAlmostEqual(spec, 7/12, "Specificity basic test failed.")

    def test_specificity_zeros(self):

        # Test for zero division case in specificity
        spec = class_eval.specificity(0, 0)
        self.assertTrue(math.isnan(spec), "Specificity zeros test failed.")
    
    def test_specificity_negatives(self):
        
        # Test for negative value in specificity
        with self.assertRaises(AssertionError):
            class_eval.specificity(-4, 5)
    
    # Positive Predictive Value Tests
    def test_ppv_basic(self):

        # Test for basic case in positive predictive value
        ppv = class_eval.pos_pred_val(5,10)
        self.assertAlmostEqual(ppv, 5/15, "The basic test for positive predictive value failed.")

    def test_ppv_zeros(self):

        # Test for zero case in positive predictive value
        ppv = class_eval.pos_pred_val(0,0)
        self.assertTrue(math.isnan(ppv), "The zeros test for positive predictive value failed.")
    
    def test_ppv_negatives(self):

        # Test for negative value case in positive predictive value
        with self.assertRaises(AssertionError):
            class_eval.pos_pred_val(2, -1)   

    # Negative Predictive Value Tests
    def test_npv_basic(self):

        # Test for basic case in negative predictive value
        npv = class_eval.neg_pred_val(3,12)
        self.assertAlmostEqual(npv, 3/15, "The basic test for negative predictive value failed.")

    def test_npv_zeros(self):

        # Test for zero division case in negative predictive value
        npv = class_eval.neg_pred_val(0, 0)
        self.assertTrue(math.isnan(npv), "The zeros test for negative predictive value failed.")

    def test_npv_negatives(self):

        # Test for basic case in negative predictive value
        with self.assertRaises(AssertionError):
            class_eval.neg_pred_val(-2, 1)

class TestPrintEvalMetrics(unittest.TestCase):
    """Tests print_eval_metrics test in class_eval."""

    def test_print_unequal(self):

        # Tests that unequal lengths will raise error
        predicted = [1, 0, 1]
        actual = [0, 1]
        with self.assertRaises(AssertionError):
            class_eval.print_eval_metrics(predicted, actual, 1)

    def test_print_empty_lists(self):
        
        # Tests that empty lists will raise an error
        predicted = []
        actual = []
        with self.assertRaises(AssertionError):
            class_eval.print_eval_metrics(predicted, actual, 1)

if __name__ == '__main__':
    unittest.main()