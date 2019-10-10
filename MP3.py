import constraint as con
import pandas as p

problem = con.Problem()

### Import course rotations and prereqs to DataFrames. Default columns "Course", "Type", and rotations ("1" through "6")
df = p.read_excel('csp_course_rotations.xlsx', sheet_name="course_rotations")
preq_df = p.read_excel('csp_course_rotations.xlsx', sheet_name="prereqs")

problem.addVariables(df['Course'].tolist(), range (1,14))
print ('variables loaded')

#### Prereq Constraint
def preq_constraint(a, b):
    if a < b:
        return True
for index, row in preq_df.iterrows():
    problem.addConstraint(preq_constraint, [row['prereq'], row['course']])

#### Capstone constraint
def capstone_constraint(x):
    if x == 13:
        return True
for index, row in df.iterrows():
    if row['Type'] == "capstone":
        problem.addConstraint(capstone_constraint, [row['Course']])

####Rotation constraint
rotations = df.drop(columns = ['Type'])
rotations = rotations.set_index('Course')
#print(rotations.to_dict('index'))

#### Restrict to one class per sem
problem.addConstraint(con.AllDifferentConstraint())
print ("constraints set")

sample = problem.getSolution()
print(sample)
solutions = problem.getSolutions()
length = len(solutions)
print ('CLASS: Artifical Intelligence, Lewis University')
print ('NAME: Scott Carrington')
print ('\nSTART TERM = Year 1 Fall 1')
print ('Number of Possible Degree Plans is ' + str(length)+ '\n')
