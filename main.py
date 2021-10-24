from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    home = "this is my home page"
    return render_template('index.html', home1= home)
@app.route("/textanalyzer",methods=['GET','POST'])
def textAnalyze():
    text = request.args.get('text')
    # print(text)
    analyzed = text
    params = {'task':'Word Counting','analyzed_text':analyzed}
    return render_template('analyze.html',params=params)
  



if __name__ == "__main__":
    app.run(debug=True)