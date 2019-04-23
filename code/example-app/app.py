from flask import Flask, render_template
from os import environ
from k8s import K8S

app = Flask(__name__)


@app.route('/')
def hello():
    runningLocally = environ["LOCAL_CLUSTER"] == '1'

    k8s = K8S(runningLocally)

    pods = k8s.list_pods()
    return render_template('main.html', pods=pods)


if __name__ == '__main__':
    app.run()
