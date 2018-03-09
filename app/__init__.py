from flask import Flask, render_template
import models
import stores
import dummy_data
from views import *

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = post_store.get_all())


member_store = stores.MemberStore()
post_store = stores.PostStore()

if __name__  == "__main__":
    dummy_data.seed_stores(member_store, post_store)
    app.run()
