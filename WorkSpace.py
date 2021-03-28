from azureml.core import Workspace

def workspace(subscription_id,resource_group,workspace_name):
    try:
        ws = Workspace(subscription_id = subscription_id, resource_group = resource_group, workspace_name = workspace_name)
        ws.write_config()
        print('Library configuration succeeded')
    except:
        print('Workspace not found, will create a new one')
        ws = Workspace.create(subscription_id = subscription_id, resource_group = resource_group, workspace_name = workspace_name)
        ws.write_config()
    return ws