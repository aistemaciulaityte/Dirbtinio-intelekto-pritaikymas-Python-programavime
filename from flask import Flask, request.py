from flask import Flask, request
from fractions import Fraction
import re
import math

app = Flask(__name__)

# Sudetis
def sudetis(x, y):
    return x + y

# Atimtis
def atimtis(x, y):
    return x - y

# Daugyba
def daugyba(x, y):
    return x * y

# Dalyba
def dalyba(x, y):
    if y != 0:
        return x / y
    else:
        return "Dalyba iš nulio negalima"

# Trupmenų sudėtis
def trupmenu_sudetis(x, y):
    return x + y

# Trupmenų atimtis
def trupmenu_atimtis(x, y):
    return x - y

# Trupmenų daugyba
def trupmenu_daugyba(x, y):
    return x * y

# Trupmenų dalyba
def trupmenu_dalyba(x, y):
    if y != 0:
        return x / y
    else:
        return "Dalyba iš nulio negalima"

@app.route("/")  # Route1
def hello_world():
    return """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
        color: #333;
        margin: 0;
        padding: 0;
    }
    h1 {
        color: #009688;
    }
    h3 {
        color: #03a9f4;
    }
    label {
        font-weight: bold;
        color: #795548;
    }
    input[type="text"] {
        padding: 8px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    input[type="submit"] {
        padding: 10px 20px;
        background-color: #03a9f4;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    input[type="submit"]:hover {
        background-color: #039be5;
    }
    p {
        color: #607d8b;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        margin-bottom: 5px;
    }
    </style>
    <h1>Skaičiuotuvas</h1>
    <form action="/skaicius" method="post">
        <label for="expression">Veiksmas (įveskite veiksmą, pvz., 2-4, sqrt(25), 25 + 15%, 2/4 + 4/3):</label><br>
        <input type="text" id="expression" name="expression"><br><br>
        <input type="submit" value="Skaičiuoti">
    </form>
    <br>
    <h3>Veiksmų paaiškinimai:</h3>
    <ul>
        <li><strong>Sudėtis</strong> - 2 + 4</li>
        <li><strong>Atimtis</strong> - 10 - 5</li>
        <li><strong>Daugyba</strong> - 3 * 7</li>
        <li><strong>Dalyba</strong> - 8 / 2</li>
        <li><strong>Šaknies traukimas</strong> - sqrt(25)</li>
        <li><strong>Procentų skaičiavimas</strong> - 25 + 15%</li>
        <li><strong>Veiksmai su trupmenomis</strong> - 2/4 + 4/3</li>
    </ul>
    """

@app.route("/skaicius", methods=["POST"])  # Route 3
def skaiciavimo():
    expression = request.form.get("expression")

    # Veiksmai su naujais įvesties laukais
    if expression:
        expression = expression.lower().strip()
        try:
            result = eval(expression, {"sqrt": math.sqrt})
            return f"<p>{expression} = {result}</p>"
        except Exception as e:
            return f"<p style='color: red;'>Klaida: {e}</p>"

    return """
    <p style='color: red;'>Įveskite veiksmą.</p>
    """


if __name__ == "__main__":
    app.run()
