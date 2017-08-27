#!/Users/poudel/anaconda/bin/python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 19, 2017 Sat
# Last update :
# Est time    :

# Imports
# Import `tensorflow`
import tensorflow as tf

def tf_eg1():
    """"""
    # Initialize two constants
    x1 = tf.constant([1,2,3,4])
    x2 = tf.constant([5,6,7,8])

    # Multiply
    result = tf.multiply(x1, x2)

    # Print the result
    print(result)

    return None

def main():
    """Run main function."""
    tf_eg1()

if __name__ == "__main__":
    main()
