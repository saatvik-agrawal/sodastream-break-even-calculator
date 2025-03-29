
# SodaStream Break-Even Calculator

This tool helps you figure out how many bottles of soda you need to make with your SodaStream before it starts saving you money compared to buying bottled soda. Just enter a few costs – the machine, CO2 cartridges, syrup mix, and store-bought soda – and it will calculate the break-even point in 800ml bottles. It’s fast, easy, and runs right in your browser using Python.

## Features

- **Python-Powered Calculations**: Leverages Pyodide to execute Python logic in the browser.
- **User Inputs**: Enter the cost of the SodaStream machine, CO2 cartridges, cartridge lifespan (in liters), syrup mix cost (per 9 liters), and bottled soda cost (per liter).
- **Instant Results**: Calculates and displays the break-even number of 800ml bottles.
- **Interactive Web Interface**: A simple web form for entering your data.

## How to Use

1. Visit the calculator on GitHub Pages: [SodaStream Break-Even Calculator](https://saatvik-agrawal.github.io/sodastream-break-even-calculator/)
2. Fill in the following details:
   - Cost of the SodaStream machine
   - Cost of CO2 cartridges
   - Lifespan of a cartridge in liters
   - Cost of syrup mix per 9 liters
   - Cost of bottled soda per liter
3. Click the "Calculate" button to view the results.

## Running Locally

If you prefer to run the calculator on your computer, follow these steps:

1. Clone the repository:

```
git clone https://github.com/saatvik-agrawal/sodastream-break-even-calculator.git
```

2. Navigate to the repository:

```python-repl
cd sodastream-break-even-calculator
```

3. Open the `index.html` file in your web browser (an internet connection is required to load Pyodide from the CDN).

## Technologies Used

- **HTML & JavaScript**: For building the interactive web interface.
- **Python & Pyodide**: Executes Python code in the browser via WebAssembly.

## Contributions

Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- This project was inspired by the need for a simple tool to compare the cost-effectiveness of using a SodaStream versus buying bottled soda.

---

Developed with ❤️ by [Saatvik Agrawal](https://github.com/saatvik-agrawal)
