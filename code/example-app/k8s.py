from kubernetes import client, config


class K8S:
    def __init__(self, runningLocally):
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

    def list_pods(self):
        v1 = client.CoreV1Api()

        ret = v1.list_pod_for_all_namespaces(watch=False)

        return ret.items
