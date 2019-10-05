import numpy as n
import constraint as con
import pandas as p


problem = con.Problem()

## Define variables
## prerequisites - position in list has to come before the postrequisite class
## some classes can only be in positions
## list of classes in the range (Fall 1 = 1, Fall 2 = 2, Spring 1 = 0, etc..)
## Year 3 Fall 2 is the max schedulelist size (14 half-semesters total - array size should be 13)
## schedulelist will be the array that holds all of the schedule for the student
## Must take 2 foundation courses
## Must take all core courses
## Must take 3 of the eight elective courses