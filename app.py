from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_body_type', methods=['POST'])
def calculate_body_type():
    if request.method == 'POST':
        shoulders = float(request.form['shoulders'])
        bust = float(request.form['bust'])
        waist = float(request.form['waist'])
        hips = float(request.form['hips'])

        body_type = determine_body_type(shoulders, bust, waist, hips)
        recommendations = get_dress_recommendations(body_type)

        return render_template('result.html', body_type=body_type, recommendations=recommendations)

def determine_body_type(shoulders, bust, waist, hips):
    shoulder_to_waist_ratio = shoulders / waist
    bust_to_waist_ratio = bust / waist
    waist_to_hips_ratio = waist / hips
    hips_to_shoulders_ratio = hips / shoulders

    if 0.9 <= shoulder_to_waist_ratio <= 1.1 and 0.9 <= waist_to_hips_ratio <= 1.1:
        return "Rectangle"
    elif hips_to_shoulders_ratio > 1.05 and waist_to_hips_ratio < 0.85:
        return "Triangle/Pear"
    elif shoulder_to_waist_ratio > 1.05 and 0.75 <= waist_to_hips_ratio < 0.95:
        return "Inverted Triangle"
    elif shoulders / hips >= 0.9 and shoulders / hips <= 1.1 and waist / shoulders < 0.75 and waist / hips < 0.75:
        return "Hourglass"
    elif bust / hips > 1.05 and waist_to_hips_ratio > 0.75:
        return "Round/Apple"
    else:
        return "Undefined body type"

def get_dress_recommendations(body_type):
    recommendations = {
        "Rectangle": "Mandarin Collar, Square Neck, Round Neck, Keyhole Neck, Boat Neck, V-Neck, Sweetheart Neck, Shirt Collar, Scoop Neck, Tie-Up Neck, Cowl Neck, Band Collar, Halter Neck, Shoulder Straps, U-Neck, One Shoulder, Shawl Neck, High Neck, Off-Shoulder, Peter Pan Collar, Choker Neck, Jewel Neck, Hood, Strapless, Above the Keyboard Collar, Polo Collar, Turtle Neck, Mock Collar, Shawl Collar, Lapel Collar",
        "Triangle/Pear": "A-Line Dresses, Fit-and-Flare Dresses, Off-the-Shoulder Dresses, Boat Neck Dresses, Empire Waist Dresses",
        "Inverted Triangle": "A-Line Dresses, V-Neck Dresses, Wrap Dresses, Peplum Dresses, Fit-and-Flare Dresses",
        "Hourglass": "Wrap Dresses, Bodycon Dresses, Sheath Dresses, Fit-and-Flare Dresses, Peplum Dresses",
        "Round/Apple": "Empire Waist Dresses, A-Line Dresses, V-Neck Dresses, Wrap Dresses, Shift Dresses"
    }
    return recommendations.get(body_type, "No recommendations available for this body type.")

if __name__ == '__main__':
    app.run(debug=True)
