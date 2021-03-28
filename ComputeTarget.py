import numpy as np
import matplotlib.pyplot as plt
import azureml.core
from azureml.core import Workspace, Experiment
from azureml.core.compute import AmlCompute, ComputeTarget

# load workspace configuration from the config.json file in the current folder.

def get_confit():
    ws = Workspace.from_config()
    print('Workspace Name: ',ws.name)
    print('Workspace Location: ',ws.location)
    print('Workspace Resource Group: ',ws.resource_group)
    return ws

# create a experiment
def create_experiment(name,ws):
    exp = Experiment(workspace=ws,name=name)
    print('Experiment {} created'.format(name))
    return exp

def compute_target(ws,compute_name='cpu-cluster-1',vm_size="STANDARD_D2_V2",compute_min_nodes=0,compute_max_nodes=4):
    if compute_name in ws.compute_targets:
        compute_target = ws.compute_targets[compute_name]
        if compute_target and type(compute_target) is AmlCompute:
            print('found compute target. just use it. ' + compute_name)
    else:
        print('Creating a new compute target')
        config = AmlCompute.provisioning_configuration(vm_size=vm_size,
                                                       min_nodes=compute_min_nodes,
                                                       max_nodes=compute_max_nodes)
        # create a cluster
        compute_target = ComputeTarget.create(ws,compute_name,config)
        compute_target.wait_for_completion(show_output=True)
    return compute_target

