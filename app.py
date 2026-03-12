# app.py
from flask import Flask
from config import supabase  # import supabase from config

app = Flask(__name__)  # app is defined HERE first

@app.route("/api/cities")  # routes go here, not in config.py
def get_cities():
    result = supabase.table("cities").select("*").execute()
    return {"data": result.data}

if __name__ == "__main__":
    app.run(debug=True)