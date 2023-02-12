from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>REST API & Data Manager App (Python) - The Nucleus Stack</h1>'


@app.route('/vehicle/<vin>')
def vehicle_vin(vin):
    return f"<h1>Vehicle with VIN#: {vin}</h1>"


@app.route('/clientinfo')
def client_info():
    out = "<h2>/clientinfo</h2>\n<hr />\n" + f"<h3>User-Agnet: {request.user_agent}</h3>" + \
        f"<h3>remote_addr: {request.remote_addr}</h3>" + \
        f"<h3>remote_user (authenticated): {request.remote_user}</h3>" + \
        f"<h3>url: {request.url}</h3>" + \
        f"<h3>cache_control: {request.cache_control}</h3>" + \
        f"<h3>accept_languages: {request.accept_languages}</h3>" + \
        f"<h3>access_route: {request.access_route}</h3>" + \
        f"<h3>raw WSGI environ: {request.environ}</h3>" + \
        f"<h3>headers: {request.headers}</h3>" + "\n<br />\n" + "\n<hr />\n"
    return out


print(f"app.url_map:\n{app.url_map}\n")

# Request hooks: before_request, before_first_request, after_request, teardown_request - p.46
# Use g context global to share data between these and views.
