from flask import Flask, request
from fractions import Fraction

app = Flask(__name__)

skaicius = 0

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
        <label for="test">skaicius 1</label><br>
        <input type="text" id="test" name="test" value="0"><br><br>

        <label for="test2">skaicius 2</label><br>
        <input type="text" id="test2" name="test2" value="0"><br><br>

        <input type="submit" value="Submit">
    </form>
    """


@app.route("/labas")  # Route2
def sakyk_labas():
    global skaicius
    skaicius = skaicius + 1
    return f"Labas {skaicius}"


@app.route("/skaicius", methods=["POST"])  # Route 3
def skaiciavimo():
    skaicius1 = int(request.form.get("test"))
    skaicius2 = int(request.form.get("test2"))

    suma = sudetis(skaicius1, skaicius2)
    skirtumas = atimtis(skaicius1, skaicius2)
    sandauga = daugyba(skaicius1, skaicius2)
    dalmuo = dalyba(skaicius1, skaicius2)

    # Trupmenų skaiciavimas
    trupmenu_suma = trupmenu_sudetis(Fraction(skaicius1), Fraction(skaicius2))
    trupmenu_skirtumas = trupmenu_atimtis(Fraction(skaicius1), Fraction(skaicius2))
    trupmenu_sandauga = trupmenu_daugyba(Fraction(skaicius1), Fraction(skaicius2))
    trupmenu_dalmuo = trupmenu_dalyba(Fraction(skaicius1), Fraction(skaicius2))

    return f"""
    <p>Sudetis: {suma}</p>
    <p>Atimtis: {skirtumas}</p>
    <p>Daugyba: {sandauga}</p>
    <p>Dalyba: {dalmuo}</p>
    <hr>
    <p>Trupmenų Sudėtis: {trupmenu_suma}</p>
    <p>Trupmenų Atimtis: {trupmenu_skirtumas}</p>
    <p>Trupmenų Daugyba: {trupmenu_sandauga}</p>
    <p>Trupmenų Dalyba: {trupmenu_dalmuo}</p>
    """


if __name__ == "__main__":
    app.run()
