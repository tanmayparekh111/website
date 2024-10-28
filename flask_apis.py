from flask import Flask, jsonify, render_template, redirect
from models.index_tick_models import db, TickNifty, TickBankNifty, TickFinNifty

app = Flask(__name__)
app.config.from_object("configuration.Config")
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/selected_service/indexes")
def indexes():
    # return render_template("backup_index.html")
    return render_template("backup_index.html")

# @app.route("/api/latest_ticks")
# def latest_ticks():
#     latest_nifty = TickNifty.query.order_by(TickNifty.timestamp.desc()).first()
#     latest_banknifty = TickBankNifty.query.order_by(TickBankNifty.timestamp.desc()).first()
#     latest_finnifty = TickFinNifty.query.order_by(TickFinNifty.timestamp.desc()).first()
    
#     return jsonify({
#         "nifty": {
#             "value": latest_nifty.closeprice if latest_nifty else None,
#             "timestamp": latest_nifty.timestamp.strftime('%H:%M:%S') if latest_nifty else None  # Formatting to HH:MM:SS
#         },
#         "banknifty": {
#             "value": latest_banknifty.closeprice if latest_banknifty else None,
#             "timestamp": latest_nifty.timestamp.strftime('%H:%M:%S') if latest_nifty else None  # Formatting to HH:MM:SS
#         },
#         "finnifty": {
#             "value": latest_finnifty.closeprice if latest_finnifty else None,
#             "timestamp": latest_nifty.timestamp.strftime('%H:%M:%S') if latest_nifty else None  # Formatting to HH:MM:SS
#         }
#     })
@app.route("/api/latest_ticks")
def latest_ticks():
    nifty_data = TickNifty.query.order_by(TickNifty.timestamp.desc()).limit(100).all()
    banknifty_data = TickBankNifty.query.order_by(TickBankNifty.timestamp.desc()).limit(100).all()
    finnifty_data = TickFinNifty.query.order_by(TickFinNifty.timestamp.desc()).limit(100).all()

    def format_data(data):
        return [{"timestamp": tick.timestamp.strftime('%H:%M:%S'), "value": tick.closeprice} for tick in data]

    return jsonify({
        "nifty": format_data(nifty_data[::-1]),  # Reverse for chronological order
        "banknifty": format_data(banknifty_data[::-1]),
        "finnifty": format_data(finnifty_data[::-1])
    })


@app.route("/selected_service/powerbi", methods=["GET"])
def get_message():
    redirect_url = "https://app.powerbi.com/view?r=eyJrIjoiZjZmMmU5ZjgtMDA0Yy00ZjZmLTg1YTYtMzRmZDRlMWMyNzMyIiwidCI6IjkwODI1ZGI3LTBiOTYtNDNiYi05NjRhLWMxZjc2Nzg0Yjk2YSJ9"
    return redirect(redirect_url)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create the tables
    app.run(host="0.0.0.0", port=5000, debug=True)
