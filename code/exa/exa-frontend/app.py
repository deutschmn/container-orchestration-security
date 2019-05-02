from flask import Flask, render_template, request
from backend import Backend

app = Flask(__name__)
backend = Backend()


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/pods')
@app.route('/pods/<namespace>')
def pods(namespace=""):
    return render_template('pods.html', namespace=namespace, pods=backend.list_pods(namespace))


@app.route('/replicasets')
@app.route('/replicasets/<namespace>')
def replicaSets(namespace=""):
    return render_template('replica-sets.html', namespace=namespace, replicaSets=backend.list_replica_sets(namespace))


@app.route('/replicasets/<namespace>/<name>/', methods=['POST'])
def editReplicaSetScale(namespace, name):
    scale = request.form["replicas"]

    backend.scale_replica_set(name, namespace, int(scale))

    return replicaSets(namespace)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
