import requests
from flask import Flask, request, url_for, jsonify

from k8s import K8S

app = Flask(__name__)
k8s = K8S()


# taken from https://stackoverflow.com/questions/13317536/get-list-of-all-routes-defined-in-the-flask-app
@app.route("/")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and \
                len(rule.defaults if rule.defaults is not None else ()) >= \
                len(rule.arguments if rule.arguments is not None else ()):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append(url)
    return jsonify(links)


@app.route('/pods')
@app.route('/pods/')
@app.route('/pods/<namespace>')
def pods(namespace=""):
    return_pods = list()

    for pod in k8s.list_pods(namespace):
        return_pods.append({
            "name": pod.metadata.name,
            "phase": pod.status.phase,
            "namespace": pod.metadata.namespace,
            "ip": pod.status.pod_ip
        })

    return jsonify(return_pods)


@app.route('/replicasets')
@app.route('/replicasets/')
@app.route('/replicasets/<namespace>')
def replicaSets(namespace=""):
    return_replica_sets = list()

    for rs in k8s.list_replica_sets(namespace):
        return_replica_sets.append({
            "name": rs.metadata.name,
            "desired": rs.status.replicas,
            "available": rs.status.available_replicas,
            "ready": rs.status.ready_replicas,
            "namespace": rs.metadata.namespace
        })

    return jsonify(return_replica_sets)


@app.route('/replicasets/<namespace>/<name>/', methods=['POST'])
def editReplicaSetScale(namespace, name):
    scale = request.form["replicas"]

    k8s.scale_replica_set(name, namespace, int(scale))

    return jsonify({"status": "ok"})


@app.route('/outside')
def helloOutside():
    try:
        host = "https://tugraz.at"
        r = requests.get(host, timeout=5)
        return jsonify({
            "message": "ok",
            "status": r.status_code,
            "host": host
        })
    except Exception as e:
        return jsonify({
            "message": "error",
            "error": str(e)
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0')
