from kubernetes import client, config
from os import environ

class K8S:
    def __init__(self):
        runningLocally = environ["LOCAL_CLUSTER"] == '1'

        if runningLocally:
            # use this for local kubectl config
            try:
                config.load_kube_config()
            except:
                print("Couldn't load local kubectl config")
        else:
            # use this for config in the cluster (using service account)
            try:
                config.incluster_config.load_incluster_config()
            except config.ConfigException:
                print("Couldn't load incluster config")

    def list_pods(self, namespace):
        v1 = client.CoreV1Api()

        if namespace:
            ret = v1.list_namespaced_pod(namespace, watch=False)
        else:
            ret = v1.list_pod_for_all_namespaces(watch=False)

        return ret.items


    def list_replica_sets(self, namespace):
        v1 = client.AppsV1Api()

        if namespace:
            ret = v1.list_namespaced_replica_set(namespace, watch=False)
        else:
            ret = v1.list_replica_set_for_all_namespaces(watch=False)

        return ret.items

    def scale_replica_set(self, name, namespace, replicas):
        v1 = client.AppsV1Api()

        body = {"spec": {"replicas": replicas}}

        v1.patch_namespaced_replica_set_scale(name, namespace, body)
