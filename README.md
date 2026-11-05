
# Python Conditions and Loops Assessment

## Project Overview
This project is developed as part of the Python Programming Assessment. It contains two console-based applications that demonstrate the use of conditional statements, loops, input validation, and basic calculations in Python.

## 1. Student Scholarship Eligibility System

This application checks whether a student is eligible for a scholarship based on three conditions:

- Marks must be 80% or above.
- Attendance must be 85% or above.
- Monthly family income must be Rs. 50,000 or less.

### Scholarship Categories
- **Full Scholarship:** Marks are 90% or above and all other conditions are met.
- **Partial Scholarship:** Marks are between 80% and 89% and all other conditions are met.
- **Not Eligible:** If any eligibility condition is not fulfilled, the program displays the reasons for ineligibility.

### Sample Execution

**Input:**
```text
Enter student name: Ali
Enter marks percentage: 95
Enter attendance percentage: 90
Enter monthly family income: 40000
```

**Output:**
```text
Student Name: Ali
Scholarship Status: Eligible
Scholarship Category: Full Scholarship
```

## 2. Pharmacy Inventory Management System

This application manages medicine stock and calculates sales revenue.

The program asks the user how many medicines they want to enter and collects the following information for each medicine:

- Medicine name
- Available stock
- Price per unit
- Quantity sold

### Main Features
- Checks whether sufficient stock is available.
- Calculates total sales for each medicine.
- Updates the remaining stock.
- Displays a low-stock warning when remaining stock is less than 10.
- Calculates total revenue using an accumulator.
- Counts medicines that need restocking.
- Displays a final inventory and sales report.

### Sample Execution

**Sample Input:**
```text
Number of medicines: 2

Medicine 1: Panadol
Available stock: 20
Price per unit: 50
Quantity sold: 5

Medicine 2: Syrup
Available stock: 8
Price per unit: 100
Quantity sold: 3
```

**Sample Output:**
```text
Medicine: Panadol
Sales Amount: Rs. 250.00
Remaining Stock: 15

Medicine: Syrup
Sales Amount: Rs. 300.00
Remaining Stock: 5
Warning: Low stock! Restocking required.

Total Medicines: 2
Total Revenue: Rs. 550.00
Medicines Requiring Restocking: 1
```

## 3. Python Concepts and Programming Techniques Used

The following Python concepts and techniques are used in this project:

- **Variables:** To store student and medicine information.
- **Input and Output:** Using `input()` and `print()` functions.
- **Conditional Statements:** Using `if`, `elif`, and `else` to make decisions.
- **Loops:** Using `while` loops for input validation and `for` loops to process medicines.
- **Range Function:** Using `range()` to repeat operations for a specific number of medicines.
- **Lists:** To store scholarship ineligibility reasons.
- **Try and Except:** To handle invalid inputs and prevent program errors.
- **Accumulators:** To calculate total pharmacy revenue.
- **Counters:** To count medicines requiring restocking.
- **Arithmetic Operators:** To calculate sales amounts and remaining stock.

## 4. Project Structure

```text
python-conditions-loops-assessment/
│
├── student_scholarship_system.py
├── pharmacy_inventory_system.py
└── README.md
```

## 5. How to Run the Programs

### Requirements
- Python 3.x installed on your computer.
- VS Code or any Python-supported editor.

### Run Student Scholarship System

Open the project folder in the terminal and execute:

```bash
py student_scholarship_system.py
```

### Run Pharmacy Inventory System

Execute the following command:

```bash
py pharmacy_inventory_system.py
```

Both programs run in the terminal and take input directly from the user.

## 6. Input Validation and Testing

Both applications include input validation to handle incorrect entries.

The programs were tested with different input scenarios, including:

- Eligible and ineligible students.
- Full and partial scholarship cases.
- Invalid marks, attendance, and income values.
- Medicines with sufficient and insufficient stock.
- Low-stock situations.
- Different medicine quantities and prices.

## 7. Conclusion

This project demonstrates the practical use of Python conditions, loops, input validation, and calculations through two real-world examples: a Student Scholarship Eligibility System and a Pharmacy Inventory Management System.
