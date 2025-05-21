from flask import Flask, request, render_template, redirect
import pandas as pd
import os
from zoho import get_access_token, push_to_zoho_crm
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file:
            return "❌ No file uploaded", 400

        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)

        df = pd.read_excel(path)
        token = get_access_token()

        failures = []
        for i, row in df.iterrows():
            success = push_to_zoho_crm(token, row)
            if not success:
                failures.append(i)

        return f"""
        ✅ Upload completed.<br>
        {'❌ Failed at rows: ' + str(failures) if failures else '🎉 All rows uploaded successfully!'}
        """

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
