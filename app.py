from flask import Flask, request
import random

app = Flask(__name__)

pujian = [
    "Sobrang ganda mo! 🌸",
    "Ang ganda mo sobra! 💖",
    "Napakaganda mo! 😍",
    "Ang ganda mo parang bituin sa langit ✨",
    "Ang ganda mo, walang kapantay! 💎",
    "Ikaw ang pinakamaganda sa lahat 💕"
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        nama = request.form.get("nama")
        kalimat = random.choice(pujian)
        return f"""
        <html>
            <head>
                <title>Pujian para sa'yo</title>
                <style>
                    body {{
                        background-color: pink;
                        font-family: Arial, sans-serif;
                        text-align: center;
                        margin-top: 20%;
                        animation: fadeIn 2s ease-in-out;
                    }}
                    h1 {{
                        color: white;
                        font-size: 3em;
                        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                        animation: fadeInText 2s ease-in-out;
                    }}
                    @keyframes fadeInText {{
                        from {{opacity: 0; transform: translateY(20px);}}
                        to {{opacity: 1; transform: translateY(0);}}
                    }}
                </style>
            </head>
            <body>
                <h1>💖 {nama}, {kalimat} 💖</h1>
            </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Ilagay ang Iyong Pangalan</title>
            <style>
                body {{
                    background-color: lavenderblush;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin-top: 20%;
                }}
                input[type="text"] {{
                    padding: 10px;
                    font-size: 1em;
                    border-radius: 5px;
                    border: 1px solid pink;
                }}
                input[type="submit"] {{
                    padding: 10px 20px;
                    font-size: 1em;
                    color: white;
                    background-color: hotpink;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }}
                input[type="submit"]:hover {{
                    background-color: deeppink;
                }}
            </style>
        </head>
        <body>
            <h1>Ilagay muna ang iyong pangalan 💌</h1>
            <form method="POST">
                <input type="text" name="nama" placeholder="Pangalan mo" required>
                <br><br>
                <input type="submit" value="Makita ang Pujian">
            </form>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
