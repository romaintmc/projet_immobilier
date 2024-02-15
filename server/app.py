from flask import Flask, jsonify
import server.search as sc
import server.search_bdd as bd

app = Flask(__name__)
#PATH = '/Users/romaintmc/Desktop/prix_immobilier_fictif.csv'

@app.route('/villes')
def vil():
    #city_list = sc.villes(PATH)
    city_list = bd.select_data("SELECT * FROM ville")
    city_list = [element[0] for element in city_list]
    return jsonify(city_list)

@app.route('/quartiers/<ville>')
def quart(ville):
    #quartier_list = sc.quartier(ville, PATH)
    quartier_list = bd.select_data("SELECT * from quartier")
    quartier_list = [element[0] for element in quartier_list]
    return jsonify(quartier_list)

@app.route('/prix/<quartier>/<ville>')
def prix(ville, quartier):
    #prix = sc.prix(ville, quartier, PATH)
    query = "SELECT prix from ville_quartier WHERE nom = %s AND nom_ville = %s"
    prix = bd.select_data_price(query, (quartier,ville))
    #if prix is None:
    #    return jsonify({"prix": "Indisponible"})
    print(prix)
    prix = [element[0] for element in prix]
    return jsonify({"prix": prix})

if __name__ == '__main__':
    app.run(debug=True)
