from requests_html import HTMLSession
import json


def main_data():
    from kubernetes import client, config

    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


with HTMLSession() as session:
    response = session.get("http://localhost:8080/api/")


def jprint(response):
    api = json.dumps(response, sort_keys=True, indent=4)
    unpack = json.loads(api)
    for key in unpack:
        if key == 'versions':
            print('Minikube version is: ', unpack[key])


jprint(response.json())
