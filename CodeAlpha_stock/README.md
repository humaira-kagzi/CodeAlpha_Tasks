# Stock Portfolio Tracker 📈

A simple Python project that helps users calculate their stock investments and visualize them using a bar chart.

The program:

* Takes stock names and quantities from the user
* Calculates total investment
* Saves the result in a text file
* Displays a graph using Matplotlib

---

## 📌 Features

* User input for stock quantity
* Predefined stock prices
* Investment calculation
* File handling (`portfolio.txt`)
* Data visualization with bar chart

---

## 🛠 Requirements

Install Python and Matplotlib before running the project.

### Install Matplotlib

```bash id="1y2x3z"
pip install matplotlib
```

---

## ▶️ How to Run

1. Save the code in a file named `portfolio.py`
2. Open terminal or command prompt
3. Run the program:

```bash id="2b4n6m"
python portfolio.py
```

---

## 📄 Example Input

```text id="k9l0p1"
How Many Stocks Do You Want To Enter? 2

Enter Stock Name: GOOGLE
Enter Quantity: 3

Enter Stock Name: TSLA
Enter Quantity: 2
```

---

## 📄 Example Output

```text id="v7c8x2"
Total Investment: 1140
```

A bar chart will also appear showing investment values for each stock.

---

## 📚 Stock Prices Used

```python id="s3d5f7"
stocks = {
    "GOOGLE":180,
    "RELIANCE":350,
    "AMAZON":140,
    "TSLA":300
}
```

---

## 📂 Output File

The program creates a file named:

```text id="a8b9c0"
portfolio.txt
```

It stores:

```text id="n4m5b6"
Total Investment = 1140
```

---

## 📊 Technologies Used

* Python
* Matplotlib
* File Handling

---

## 🧠 Concepts Used

* Dictionary
* Loops
* Conditional Statements
* File Handling
* Data Visualization
* User Input

---

## 🚀 Future Improvements

* Add more stocks
* Real-time stock prices
* Pie chart visualization
* Profit/Loss calculation
* Save complete portfolio details

---

## ⚠️ Note

In your code, the variable name is written as:

```python id="d2f4g6"
protfolio
```

Correct spelling should be:

```python id="h7j8k9"
portfolio
```

You can rename it for better readability.

---

## 👨‍💻 Author
Humaira Kagzi


Python Mini Project - Stock Portfolio Tracker
