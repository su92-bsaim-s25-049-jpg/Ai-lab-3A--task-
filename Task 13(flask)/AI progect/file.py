from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        name = request.form.get('name', '')
        roll = request.form.get('roll', '')

        gender = request.form.get('gender', 'male')
        parent = request.form.get('parent_edu', 'high school')
        lunch = request.form.get('lunch', 'standard')
        test = request.form.get('test_prep', 'none')

        math = int(request.form.get('math', 50))
        reading = int(request.form.get('reading', 50))
        writing = int(request.form.get('writing', 50))

        # input dataframe
        input_data = pd.DataFrame({
            "Gender": [gender],
            "ParentEduc": [parent],
            "LunchType": [lunch],
            "TestPrep": [test],
            "ReadingScore": [reading],
            "WritingScore": [writing],
            "NrSiblings": [0]
        })

        input_data = pd.get_dummies(input_data)

        input_data = input_data.reindex(
            columns=model.feature_names_in_,
            fill_value=0
        )

        result = model.predict(input_data)[0]

        avg = (result + reading + writing) / 3

        status = "PASS " if avg >= 50 else "FAIL "

        level = "High " if avg > 75 else "Medium " if avg > 50 else "Low "

        return render_template(
            "index.html",
            result=round(result, 2),
            avg=round(avg, 2),
            status=status,
            level=level,
            name=name,
            roll=roll,
            reading=reading,
            writing=writing
        )

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
