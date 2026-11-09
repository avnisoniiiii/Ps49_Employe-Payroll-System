# Employee Payroll System

**PS No.: 49**

This is a Python 3 payroll program for calculating employee and manager salaries. It uses classes, inheritance, methods, input validation and file handling.

## Salary rules used

- Overtime pay = overtime hours × Rs. 200
- Employee gross salary = basic pay + overtime pay
- Manager bonus = 10% of basic pay
- Manager gross salary = basic pay + overtime pay + bonus
- PF deduction = 12% of basic pay
- Tax = 10% of gross salary when gross salary is above Rs. 50,000; otherwise tax is zero
- Net salary = gross salary − PF − tax

## Requirements

- Python 3
- No extra library is required.

## How to run

1. Open this folder in VS Code or a terminal.
2. Run:

   ```bash
   python one.py
   ```

3. Choose `E` for Employee or `M` for Manager.
4. Enter the employee ID, name, basic salary and overtime hours.
5. The payslip will be displayed and saved in `payroll.txt`.
6. Enter `Y` to add another employee or `N` to finish.

## Files

- `one.py` — main Python program
- `README.md` — project information and instructions
- `payroll.txt` — sample payslip records from the supplied test cases; running the program appends new payslips
- `Test_cases_passed.pdf` — test case calculation report
- `Project_Details.png` — screenshot of the PS No. 49 project allocation

## Important

The sample payroll.txt is included to show the expected format. For your own submission, run the program and check that your own entries are added to the file. Keep your own screenshots if your instructor asks for proof that the program ran.
