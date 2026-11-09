class Employee:
    def __init__(self, emp_id, name, basic_pay, overtime_hours):
        self.emp_id = emp_id
        self.name = name
        self.basic_pay = basic_pay
        self.overtime_hours = overtime_hours

    def calculate_overtime(self):
        return self.overtime_hours * 200

    def calculate_bonus(self):
        # Regular employees do not get a bonus.
        return 0

    def calculate_gross(self):
        return self.basic_pay + self.calculate_overtime() + self.calculate_bonus()

    def calculate_pf(self):
        return self.basic_pay * 0.12

    def calculate_tax(self):
        gross = self.calculate_gross()
        if gross > 50000:
            return gross * 0.10
        return 0

    def calculate_net(self):
        return self.calculate_gross() - self.calculate_pf() - self.calculate_tax()

    def print_payslip(self):
        overtime = self.calculate_overtime()
        bonus = self.calculate_bonus()
        gross = self.calculate_gross()
        pf = self.calculate_pf()
        tax = self.calculate_tax()
        net = self.calculate_net()

        lines = [
            "----------------------------------------",
            "             EMPLOYEE PAYSLIP           ",
            "----------------------------------------",
            f"Employee ID   : {self.emp_id}",
            f"Name          : {self.name}",
            f"Employee Type : {self.__class__.__name__}",
            f"Basic Pay     : Rs.{self.basic_pay:.2f}",
            f"Overtime      : Rs.{overtime:.2f}",
        ]

        if bonus > 0:
            lines.append(f"Bonus         : Rs.{bonus:.2f}")

        lines.extend([
            f"Gross Salary  : Rs.{gross:.2f}",
            f"PF (12%)      : Rs.{pf:.2f}",
            f"Tax           : Rs.{tax:.2f}",
            f"Net Salary    : Rs.{net:.2f}",
            "----------------------------------------",
            ""
        ])

        payslip = "\n".join(lines)
        print("\n" + payslip)

        # Save each payslip in the same text file.
        with open("payroll.txt", "a", encoding="utf-8") as file:
            file.write(payslip)


class Manager(Employee):
    def calculate_bonus(self):
        return self.basic_pay * 0.10


def get_positive_number(message):
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print("Invalid basic salary. Enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Enter a valid number.")


def get_non_negative_number(message):
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("Invalid overtime hours. Enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid overtime hours. Enter a number.")


def main():
    print("===== EMPLOYEE PAYROLL SYSTEM =====")

    while True:
        emp_type = input("\nEnter employee type (E for Employee / M for Manager): ").strip().upper()
        while emp_type not in ("E", "M"):
            print("Please enter E for Employee or M for Manager.")
            emp_type = input("Enter employee type (E/M): ").strip().upper()

        emp_id = input("Enter employee ID: ").strip()
        name = input("Enter employee name: ").strip()

        while not emp_id or not name:
            print("Employee ID and name cannot be empty.")
            emp_id = input("Enter employee ID: ").strip()
            name = input("Enter employee name: ").strip()

        basic_pay = get_positive_number("Enter basic salary: Rs.")
        overtime_hours = get_non_negative_number("Enter overtime hours: ")

        if emp_type == "M":
            person = Manager(emp_id, name, basic_pay, overtime_hours)
        else:
            person = Employee(emp_id, name, basic_pay, overtime_hours)

        person.print_payslip()

        again = input("Do you want to add another employee? (Y/N): ").strip().upper()
        if again != "Y":
            print("\nPayslips have been saved in payroll.txt")
            break


if __name__ == "__main__":
    main()
