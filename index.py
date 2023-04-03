from flask import Flask, request, render_template, jsonify
import openai
import tiktoken

app = Flask(__name__)

openai.api_key = "[OPEN AI API]"

@app.get("/")
def homepage():
    return render_template('homepage.html')
@app.post('/')
def generateEmail():
    subject = openai.Completion.create(
        model="text-davinci-003",
        prompt="Write an Email subject with the following prompt: " + request.json["subject"]
    )
    text = openai.Completion.create(
        model="text-davinci-003",
        prompt="Write an Email with the following prompt: " + request.json["subject"] + "(DONT generate the subject)",
        max_tokens=4096-num_tokens_from_string("Write an Email with the following prompt: " + request.json["subject"] + "(DONT generate the subject)")
    )
    return jsonify(subject = subject['choices'][0]['text'], text = text['choices'][0]['text'])

def num_tokens_from_string(string):
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model("text-davinci-003")
    num_tokens = len(encoding.encode(string))
    return num_tokens