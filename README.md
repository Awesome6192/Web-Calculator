# Calculator Application

This is a web-based calculator application built using **Django** for the backend and **HTML/CSS/JavaScript** for the frontend. The calculator supports basic arithmetic operations, square root calculations, exponentiation, and the use of Euler's number (`e`).

---

## Features

- **Basic Arithmetic**: Addition, subtraction, multiplication, and division.
- **Advanced Operations**:
  - Square root (`√`).
  - Exponentiation (`^` for raising to a power).
  - Euler's number (`e`) for exponential calculations.
- **Parentheses Support**: Handles complex expressions with parentheses.
- **BODMAS Rule**: Ensures calculations follow the correct order of operations.
- **Responsive Design**: Frontend is styled using Tailwind CSS for a clean and responsive UI.

---

## Screenshots

Here are some screenshots of the calculator application:

### Calculator Interface

![Calculator Interface](images/screenshot_28.png)

### Example Calculation

![Example Calculation](images/screenshot_29.png)

---

## Technologies Used

### Backend

- **Django**: Python-based web framework for handling requests and processing calculations.
- **Python**: Core language for backend logic.

### Frontend

- **HTML**: Structure of the calculator interface.
- **CSS (Tailwind CSS)**: Styling for the calculator.
- **JavaScript**: Handles user interactions and communicates with the backend.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 4.x
- Node.js (optional, for Tailwind CSS compilation)

### Steps

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd calculator
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   ```

   - **On Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **On macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Open the application in your browser:
   ```
   http://127.0.0.1:8000/
   ```

---

## Project Structure

```
calculator/
├── my_calculator/
│   ├── views.py          # Backend logic for calculations
│   ├── urls.py           # URL routing for the application
│   ├── templates/
│   │   └── index.html    # Frontend template for the calculator
│   └── static/
│       └── src/output.css # Tailwind CSS styles
├── manage.py             # Django management script
└── README.md             # Project documentation
```

---

## Usage

### Calculator Buttons

- **AC**: Clears the display.
- **←**: Deletes the last character.
- **%**: Calculates percentages.
- **÷, ×, -, +**: Basic arithmetic operations.
- **√**: Calculates the square root.
- **^**: Raises a number to a power.
- **e**: Uses Euler's number for exponential calculations.
- **(, )**: Supports grouping with parentheses.

### Example Calculations

1. **Basic Arithmetic**:

   - Input: `2 + 3`
   - Output: `5`

2. **Exponentiation**:

   - Input: `2^3`
   - Output: `8`

3. **Square Root**:

   - Input: `√16`
   - Output: `4`

4. **Euler's Number**:

   - Input: `e^2`
   - Output: `7.389`

5. **Complex Expressions**:
   - Input: `(2 + 3) * (4 - 1)`
   - Output: `15`

---

## API Endpoints

### `/calculate/`

- **Method**: `POST`
- **Description**: Processes mathematical expressions and returns the result.
- **Request Body**:
  ```json
  {
    "expression": "2^3"
  }
  ```
- **Response**:
  ```json
  {
    "result": 8
  }
  ```

---

## Known Issues

- Validation errors may occur for unsupported characters in expressions.
- Ensure proper spacing and syntax when entering complex expressions.

---

## Future Enhancements

- Add support for trigonometric functions (e.g., `sin`, `cos`, `tan`).
- Implement history tracking for previous calculations.
- Add unit tests for backend logic.
- Improve error handling for invalid inputs.

---

## Contributing

Contributions are welcome! To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push your changes to your forked repository:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request to the main repository.

Please ensure your code follows the project's coding standards and includes appropriate documentation.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- **Django**: For providing a robust backend framework.
- **Tailwind CSS**: For the clean and responsive UI.
- **MDN Web Docs**: For JavaScript and frontend references.
