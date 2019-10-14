import constraint as con
import pandas as p
import numpy as n

problem = con.Problem()

### Import course rotations and prereqs to DataFrames. Default columns "Course", "Type", and rotations ("1" through "6")
df = p.read_excel('csp_course_rotations.xlsx', sheet_name="course_rotations")
preq_df = p.read_excel('csp_course_rotations.xlsx', sheet_name="prereqs")
schedule = p.read_excel('csp_course_rotations.xlsx', sheet_name='schedule')

problem.addVariables(df['Course'].tolist(), range (1,19))

#### Prereq Constraint
def preq_constraint(a, b):
    if a < b:
        return True
for index, row in preq_df.iterrows():
    problem.addConstraint(preq_constraint, [row['prereq'], row['course']])

#### Capstone constraint
def capstone_constraint(x):
    if x == 12: ##12 is max number of classes required
        return True
for index, row in df.iterrows():
    if row['Type'] == "capstone":
        problem.addConstraint(capstone_constraint, [row['Course']])

#### foundation / core  constraint
def foundcore_constraint(x):
    if x <11 : ##11 is max number of classes before capstone
        return True
for index, row in df.iterrows():
    if row['Type'] == "foundation" or row['Type'] == "core":
        problem.addConstraint(foundcore_constraint, [row['Course']])


### Attempted to run rotation constraint (based on class availability). Could not get constant to work
# def rotation_constraint(x, y):
#     problem.addConstraint(x, y)
#
# dfr = df.drop(['Type'], axis = 1)
# dfr.apply(lambda row: rotation_constraint(row['Course'], n.arange(2*len(row[1:]))[n.tile((row[1:]==1),2)]+1), axis=1)

#### Restrict to one class per block
problem.addConstraint(con.AllDifferentConstraint())

sample = problem.getSolution()

print ('CLASS: Artificial Intelligence, Lewis University')
print ('NAME: Scott Carrington')
print ('\nSTART TERM = Year 1 Fall 1')

## Had difficulty mapping to correct term. Tried following code but did not work
#new_sample = dict([(value, key) for key, value in sample.items()])
# new_schedule = schedule['value'].map(sample)
print(sample)
print(schedule.to_string(header=False,index=False))

### Program stalls out when attempt is made for max # of solutions
solutions = problem.getSolutions()
length = len(solutions)
print ('Number of Possible Degree Plans is ' + str(length)+ '\n')

