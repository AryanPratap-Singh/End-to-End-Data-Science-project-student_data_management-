import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from flask import Flask, jsonify, render_template, request

from student_dashboard.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "scoresense"})


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("Home.html")

    try:
        data = CustomData(
            gender=request.form.get("gender", ""),
            race_ethnicity=request.form.get("ethnicity", ""),
            parental_level_of_education=request.form.get(
                "parental_level_of_education", ""
            ),
            lunch=request.form.get("lunch", ""),
            test_preparation_course=request.form.get(
                "test_preparation_course", ""
            ),
            reading_score=int(request.form.get("reading_score", "")),
            writing_score=int(request.form.get("writing_score", "")),
        )
        prediction = PredictPipeline().predict(data.get_data_as_data_frame())
        return render_template("Home.html", results=prediction[0])
    except (TypeError, ValueError) as exc:
        return render_template("Home.html", error=f"Invalid input: {exc}"), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
