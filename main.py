import json
from lib.ecs import *

service_arns = get_service_arns(cluster_name="maehachi08")
response = get_describe_services(cluster_name="maehachi08", service_arns=service_arns)

if response is not None:
    for service_arn in service_arns:
        print(get_service_running_count(cluster_name="maehachi08", service_arn=service_arn))
        task_definition = get_service_taskdefinition(cluster_name="maehachi08", service_arn=service_arn)

        print(task_definition)
        print(get_taskdefinition_image(task_definition))

