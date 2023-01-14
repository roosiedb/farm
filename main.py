from flask import Flask
import power

app = Flask(__name__)

@app.route('/')
def index():
    html_top = '<html>'
    html_bottom = '</html>'
    
    html_head = \
        '<head>' + \
        '<title>Farm - Het nutteloze programma</title>' + \
        '<style>' + \
        '   body {' + \
        '       background-color: #E6E6FA;' + \
        '}' + \
        '</style>' + \
        '</head>'

    html_body = \
        '<body>' + \
        '<h1>Farm - voor al uw dieren</h1>' + \
        '<p>Farm is het programma waarmee de werking van een deploy pipeline wordt aangetoond.</p>' + \
        '<p>Laatste wijziging: 14-1-2023, 15:09.</p>'

    for y in range(1, 11):
        html_body = html_body + '<h2>Hoofdstuk ' + str(y) + '</h2>'
        for x in range(1, 6):
            html_body = html_body + 'Power functie voor ' + str(y) + '^' + str(x) + ' = ' + str(power.power(y,x)) + '.<br>'

    html_body = html_body + \
        '   </body>'

    return html_top + html_head + html_body + html_bottom

@app.route('/cow')
def cow():
    return "MOOOooo!"
