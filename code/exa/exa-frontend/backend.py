from os import environ

import requests


class Backend:

    def __init__(self):
        self.__backend_name__ = environ["BACKEND_NAME"]
        self.__backend_port__ = environ["BACKEND_PORT"]
        self.__timeout__ = 5

    def __get_endpoint__(self, resource=""):
        return "http://" + self.__backend_name__ + ":" + self.__backend_port__ + "/" + resource

    def list_pods(self, namespace=""):
        endpoint = self.__get_endpoint__("pods/" + namespace)
        r = requests.get(endpoint, timeout=self.__timeout__)
        pods = r.json()

        return pods

    def list_replica_sets(self, namespace=""):
        endpoint = self.__get_endpoint__("replicasets/" + namespace)
        r = requests.get(endpoint, timeout=self.__timeout__)
        try:
            replica_sets = r.json()
            return replica_sets
        except:
            return "Error: " + r.text

    def scale_replica_set(self, name, namespace, scale):
        endpoint = self.__get_endpoint__("replicasets/" + namespace + "/" + name + "/")
        form_data = {"replicas": scale}

        r = requests.post(endpoint, data=form_data, timeout=self.__timeout__)
        data = r.json()
        if data["status"] == "ok":
            return self.list_replica_sets()
        else:
            return "Erreur"
