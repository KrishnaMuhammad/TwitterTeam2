from flask import render_template
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')
    # if request has args (?tweet=some_tweet)
    #if request.args:

        # get the value of the arg
        # tweet = request.args.get('tweet')   
        


@app.route('/about')
def about():

    about_text = """
    Fill in some info about the project here.
    """
    return about_text
    
if __name__=='__main__':

    app.run(debug=True)

