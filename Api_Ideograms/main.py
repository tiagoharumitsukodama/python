from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():

    dictionaryKaji = {}
    translated = ''

    try:
        f = open('ideograms.json', 'r')
        dictionaryKaji = json.load(f)
        f.close()
    except:
        return Response(status=500)

    try:
        romaji = request.args.get('romaji')
    except:
        return Response(status=401)

    try:
        currentLetter = ''
        for letter in romaji:
            currentLetter = currentLetter + letter

            if currentLetter in dictionaryKaji:
                translated = translated + dictionaryKaji[currentLetter]
                currentLetter = ''

        translated = translated + currentLetter

    except:
        return Response(status=404)

    return jsonify(translated), 200


if __name__ == '__main__':
    app.run(debug=True, port=5500)
