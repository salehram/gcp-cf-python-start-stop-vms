import googleapiclient.discovery

def stop_vm(request):
    compute = googleapiclient.discovery.build('compute', 'v1')
    result = compute.instances().stop(project='PROJECT_ID', zone='ZONE_NAME', instance='VM_NAME').execute()
    return result
