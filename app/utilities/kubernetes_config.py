from kubernetes import client, config
#from app.setup import log


class KubernetesConfig:
    def __init__(self, log, service_name):
        self.log = log
        self.service_name = service_name
        config.load_incluster_config()  # This throws an exception on failure?
        self.client = client.CoreV1Api()
        self.namespace = open("/var/run/secrets/kubernetes.io/serviceaccount/namespace").read()
        log.info('Namespace: {}'.format(self.namespace))

    def get_ip(self):
        service = self.client.read_namespaced_service(namespace=self.namespace, name=self.service_name)
        return service.spec.cluster_ip

    def get_port(self):
        service = self.client.read_namespaced_service(namespace=self.namespace, name=self.service_name)
        return str(service.spec.ports[0].port)
