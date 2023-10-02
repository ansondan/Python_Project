#!/usr/bin/env python
import sys

next(sys.stdin)

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')
    if len(fields) == 4:
        EmployeeID, Name, Salary, Department = fields
        if int(Salary) > 70000:
            print(line)
