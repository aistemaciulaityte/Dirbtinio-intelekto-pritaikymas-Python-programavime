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
        <label for="test">Skaicius 1</label><br>
        <input type="text" id="test" name="test" value="0"><br><br>


        <label for="test2">Skaicius 2</label><br>
        <input type="text" id="test2" name="test2" value="0"><br><br>


        <label for="frac1">Trupmena 1 (pvz., 1/2)</label><br>
        <input type="text" id="frac1" name="frac1" value="0"><br><br>


        <label for="frac2">Trupmena 2 (pvz., 3/4)</label><br>
        <input type="text" id="frac2" name="frac2" value="0"><br><br>


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
    skaicius1 = float(request.form.get("test"))
    skaicius2 = float(request.form.get("test2"))
    frac1 = request.form.get("frac1")
    frac2 = request.form.get("frac2")


    # Parskaičiuoja trupmenas
    frac1_parts = frac1.split('/')
    frac2_parts = frac2.split('/')
    frac1_val = Fraction(int(frac1_parts[0]), int(frac1_parts[1]))
    frac2_val = Fraction(int(frac2_parts[0]), int(frac2_parts[1]))


    suma = sudetis(skaicius1, skaicius2)
    skirtumas = atimtis(skaicius1, skaicius2)
    sandauga = daugyba(skaicius1, skaicius2)
    dalmuo = dalyba(skaicius1, skaicius2)


    # Trupmenų skaiciavimas
    trupmenu_suma = trupmenu_sudetis(frac1_val, frac2_val)
    trupmenu_skirtumas = trupmenu_atimtis(frac1_val, frac2_val)
    trupmenu_sandauga = trupmenu_daugyba(frac1_val, frac2_val)
    trupmenu_dalmuo = trupmenu_dalyba(frac1_val, frac2_val)


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
