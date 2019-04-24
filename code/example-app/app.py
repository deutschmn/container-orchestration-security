from flask import Flask, render_template, request
from os import environ
from k8s import K8S

app = Flask(__name__)
k8s = K8S()

@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/pods')
@app.route('/pods/<namespace>')
def pods(namespace=""):
    pods = k8s.list_pods(namespace)

    return render_template('pods.html', namespace=namespace, pods=pods)


@app.route('/replicasets')
@app.route('/replicasets/<namespace>')
def replicaSets(namespace=""):
    replicaSets = k8s.list_replica_sets(namespace)

    return render_template('replica-sets.html', namespace=namespace, replicaSets=replicaSets)


@app.route('/replicasets/<namespace>/<name>/', methods=['POST'])
def editReplicaSetScale(namespace, name):
    scale = request.form["replicas"]

    k8s.scale_replica_set(name, namespace, int(scale))

    return replicaSets(namespace)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
