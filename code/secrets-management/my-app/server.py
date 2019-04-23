from http.server import BaseHTTPRequestHandler
from kubernetes import client, config


class Server(BaseHTTPRequestHandler):

    def list_pods(self):
        runningLocally = True

        if runningLocally:
            # use this for local kubectl config
            try:
                config.load_kube_config()
            except:
                self.println("Couldn't load local kubectl config")
        else:
            # use this for config in the cluster (using service account)
            try:
                config.incluster_config.load_incluster_config()
            except config.ConfigException:
                self.println("Couldn't load incluster config")

        v1 = client.CoreV1Api()

        # pods with ips
        self.println("Pods with their IPs:")
        ret = v1.list_pod_for_all_namespaces(watch=False)
        for i in ret.items:
            self.println("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

        # roles
        self.println("\nRoles:")


    def println(self, string):
        self.wfile.write(bytes(string, 'utf-8'))
        self.wfile.write(b"\n")

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.list_pods()
        return
