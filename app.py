from flask import Flask, render_template

app = Flask('__name__',  static_url_path='',
            static_folder='assets',
            template_folder='templates')

# put the content of the site here


@app.route('/')
def home():
    return render_template('projects.html')


if __name__ == "__main__":
    app.run(debug=True)
