from openai import OpenAI
from flask import Flask, render_template, request,request
import pypdf
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    output="" 
    replay=""
    if request.method=="POST":
        user=request.form.get("user")
        file=request.files.get("file")
        pdf_reader=pypdf.PdfReader(file)
        text=""
        for page in pdf_reader.pages:
            text+=page.extract_text()
        output=text 
        client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key="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",
            )
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1",
            messages=[
                {
                    "role": "user",
                    "content": f"document information {output}, user query {user}."
                    }
                ],
           )
        replay=completion.choices[0].message
    return render_template("index.html", output=output, replay=replay)

if __name__ == '__main__':
    app.run()



