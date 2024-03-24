from flask import Flask, request, session
import math

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/")  
def hello_world():
    previous_expressions = session.get('previous_expressions', [])
    previous_expressions_html = "<ul>"
    for item in previous_expressions:
        previous_expressions_html += f"<li>{item}</li>"
    previous_expressions_html += "</ul>"
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Skaičiuotuvas</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                background-color: {'black' if session.get('page_color') == 'black' else 'white'};
                color: {'white' if session.get('page_color') == 'black' else 'black'};
            }}
            #content {{
                display: flex;
                flex-direction: column;
                align-items: flex-start;
                margin-top: 20px;
                width: 80%;
            }}
            #theme-selection {{
                margin-top: 20px;
                align-self: flex-end;
            }}
            #theme-selection label {{
                margin-right: 10px;
            }}
            #theme-selection input[type="submit"] {{
                padding: 5px 10px;
                background-color: #03a9f4;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            #theme-selection input[type="submit"]:hover {{
                background-color: #039be5;
            }}
        </style>
    </head>
    <body>
        <h1>Skaičiuotuvas</h1>
        <div id="content">
            <form action="/skaicius" method="post">
                <label for="expression">Veiksmas (įveskite veiksmą, pvz., 2-4, sqrt(25), 25 + 15%, 2/4 + 4/3):</label><br>
                <input type="text" id="expression" name="expression"><br><br>
                <input type="submit" value="Skaičiuoti">
            </form>
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
            <h3>Ankstesni veiksmai:</h3>
            {previous_expressions_html}
        </div>
        <form id="theme-selection" action="/change_color" method="post">
            <label for="color">Pasirinkite temą:</label>
            <input type="submit" name="color" value="Juoda">
            <input type="submit" name="color" value="Balta">
        </form>
    </body>
    </html>
    """

@app.route("/skaicius", methods=["POST"])  
def skaiciavimo():
    expression = request.form.get("expression")

    if expression:
        expression = expression.lower().strip()
        try:
            result = eval(expression, {"sqrt": math.sqrt})
            previous_expressions = session.get('previous_expressions', [])
            previous_expressions.append(expression)
            session['previous_expressions'] = previous_expressions
            return f"<p>{expression} = {result}</p>"
        except Exception as e:
            return f"<p style='color: red;'>Klaida: {e}</p>"

    return """
    <p style='color: red;'>Įveskite veiksmą.</p>
    """

@app.route("/change_color", methods=["POST"])
def change_color():
    color = request.form.get("color")
    if color == "Juoda":
        session['page_color'] = 'black'
    elif color == "Balta":
        session['page_color'] = 'white'
    return hello_world()

if __name__ == "__main__":
    app.run()
