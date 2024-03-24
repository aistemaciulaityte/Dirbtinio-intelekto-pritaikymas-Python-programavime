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
    <form action="/skaicius" method="post">
        <label for="expression">Veiksmas (įveskite veiksmą, pvz., 2-4, sqrt(25), 25 + 15%, 2/4 + 4/3):</label><br>
        <input type="text" id="expression" name="expression"><br><br>
        <input type="submit" value="Skaičiuoti">
    </form>
    <br>
    <h3>Veiksmų paaiškinimai:</h3>
    <ul>
        <li>Sudėtis - 2 + 4</li>
        <li>Atimtis - 10 - 5</li>
        <li>Daugyba - 3 * 7</li>
        <li>Dalyba - 8 / 2</li>
        <li>Šaknies traukimas - sqrt(25)</li>
        <li>Procentų skaičiavimas - 25 + 15%</li>
        <li>Veiksmai su trupmenomis - 2/4 + 4/3</li>
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
            return f"<p>Klaida: {e}</p>"

    return """
    <p>Įveskite veiksmą.</p>
    """


if __name__ == "__main__":
    app.run()

