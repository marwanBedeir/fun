from flask import Flask, render_template
import os
from excel import excel

app = Flask(__name__)


@app.route('/img-to-excel', methods=['POST'])
def img_excel():
    img = ""
    out_path = ""
    excel.img_to_excel(img, out_path)
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)