#!/Users/poudel/anaconda/bin/python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 19, 2017 Sat
# Last update :
# Est time    :

# Imports
# Import `tensorflow`
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

def tf_eg1():
    """"""
    # Initialize two constants
    x1 = tf.constant([1,2,3,4])
    x2 = tf.constant([5,6,7,8])

    # Multiply
    result = tf.multiply(x1, x2)

    # Intialize the Session
    sess = tf.Session()

    # Print the result
    print(sess.run(result))

    # Close the session
    sess.close()

def main():
    """Run main function."""
    tf_eg1()

if __name__ == "__main__":
    main()
