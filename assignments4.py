

maths = int(input('Enter Maths marks: '))
physics = int(input('Enter Physics marks: '))
geo = int(input('Enter Geography marks: '))
chem = int(input('Enter Chemistry marks: '))


if any(mark < 0 or mark > 100 for mark in [maths, physics, geo, chem]):
    print("Unrecognized marks. Please enter valid marks between 0 and 100.")
else:
    # Calculate average
    avg_marks = (maths + physics + geo + chem) / 4

    # Grade
    if avg_marks >= 71:
        print("Grade: A")
    elif avg_marks >= 51:
        print("Grade: B")
    elif avg_marks >= 31:
        print("Grade: C")
    else:
        print("Grade: D")