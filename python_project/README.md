A Semester Project Submitted for Course Completion
of
COMPUTER PROGRAMMING II


DEPARTMENT OF SOFTWARE ENGINEERING
COLLEGE OF COMPUTING AND INFORMATICS
HARAMAYA UNIVERSITY


Project Title:
--------------
Volume Conversion System


Group Members:
--------------
No.   Full Name                    ID
1     Abel Ukuni Pacifico          3472/17
2     Andinet Mengesha             0546/17
3     Beka Demerew                 0663/17
4     Bereket Michael              0684/17
5     Daniel Peter Riakchuol       4035/17
6     Yonas Legesse                3402/17


Submission Date:
----------------
January 2025


PROJECT DOCUMENTATION
======================
Volume Conversion System


1. Introduction
---------------
The Volume Conversion System is a Python-based desktop application developed
to convert volume values from one unit to another accurately. The system uses
the Tkinter library to provide a simple graphical user interface (GUI), making
it easy for users to perform conversions without requiring command-line
interaction. This project demonstrates fundamental Python programming concepts
and basic GUI development.


2. Objectives of the Project
----------------------------
The objectives of this project are:
- To design and implement a Python program for converting volume units.
- To provide a user-friendly graphical interface using Tkinter.
- To demonstrate the use of dictionaries for data storage.
- To apply functions and error handling techniques in Python.
- To ensure accurate and reliable unit conversions.


3. Scope of the Project
-----------------------
The project focuses exclusively on volume unit conversion. It supports selected
metric units and US customary units. The application runs locally on a computer
and does not require internet connectivity.


4. Tools and Technologies Used
------------------------------
Programming Language : Python
GUI Library          : Tkinter
Development Environment : PyCharm / IDLE
Operating System     : Windows


5. Supported Units
------------------
The system supports the following volume units:
- Liter (L)
- Milliliter (mL)
- Centiliter (cL)
- Deciliter (dL)
- Hectoliter (hL)
- Kiloliter (kL)
- Cubic centimeter (cm³)
- Cubic decimeter (dm³)
- Cubic meter (m³)
- US gallon
- US quart
- US pint
- US cup
- Fluid ounce


6. System Design
----------------
6.1 Conversion Logic
All volume values are first converted into a base unit (liter). After conversion
to liters, the value is converted into the selected target unit. This two-step
approach improves accuracy and simplifies the conversion process.

6.2 Data Structure
A Python dictionary is used to store conversion factors for each supported unit
relative to one liter. This allows efficient access and makes it easy to add or
modify units in the future.

6.3 Graphical User Interface
The GUI consists of:
- A text entry field for volume input
- A dropdown menu for selecting the source unit
- A dropdown menu for selecting the target unit
- A Convert button
- A label for displaying the conversion result


7. Functional Requirements
--------------------------
- The system shall accept a numeric volume value from the user.
- The system shall allow selection of source and destination units.
- The system shall perform correct volume conversion.
- The system shall display the conversion result clearly.
- The system shall display error messages for invalid inputs.


8. Non-Functional Requirements
------------------------------
- The system should be easy to use and understand.
- The system should provide fast response time.
- The system should handle errors gracefully without crashing.


9. Input Validation and Error Handling
-------------------------------------
The program validates user input and handles the following cases:
- Empty input fields
- Non-numeric input values
- Negative volume values

Error messages are displayed using dialog boxes to inform the user of invalid
input.


10. Algorithm Description
-------------------------
1. Start the application.
2. Display the GUI window.
3. Accept volume input from the user.
4. Validate the input value.
5. Convert the input value to liters.
6. Convert the liter value to the selected target unit.
7. Display the conversion result.
8. Terminate the program when the window is closed.


11. Testing
-----------
The system was tested using:
- Valid numeric inputs
- Alphabetic and symbol inputs
- Negative values
- Multiple unit conversion combinations

The application produced correct results and appropriate error messages in all
cases.


12. Limitations
---------------
- The system supports only volume conversions.
- Output formatting is basic.
- Conversion history is not stored.


13. Future Enhancements
-----------------------
- Add additional volume units.
- Improve result formatting and rounding options.
- Include conversion history.
- Convert the application into a standalone executable.


14. Conclusion
--------------
The Volume Conversion System successfully demonstrates the use of Python for
developing a practical GUI-based application. The project applies essential
programming concepts such as dictionaries, functions, and error handling, and
provides a solid foundation for more advanced software development projects.


15. References
--------------
- Python Official Documentation
- Tkinter Official Documentation


