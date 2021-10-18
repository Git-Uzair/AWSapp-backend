import sys

sys.path.insert(1, "e:/Data/Internships/Gosaas/Project/Backend/database")
from Connection import Connection
import boto3


class Ec2DataManager:
    def __init__(self):
        self.__db = Connection.getConnection()

    def getAllInstances(self, client_name, region):
        try:
            Client = self.__db["clients"]
            result = Client.find_one({"name": client_name})
            session = boto3.Session(
                aws_access_key_id=result["aws_access_key_id"],
                aws_secret_access_key=result["aws_secret_access_key"],
                region_name=region,
            )
            ec2 = session.resource("ec2")
            instances = []
            for i in ec2.instances.all():
              
                instances.append(
                    {
                        "instanceId": i.id,
                        "state": i.state["Name"],
                        "instance_type": i.instance_type,
                        "launch_time": i.launch_time,
                        "name": i.tags[0]['Value'],
                        "key_name": i.key_name,
                        "public_ip": i.public_ip_address,
                        "public_dns": i.public_dns_name,
                    }
                )
            return instances
        except Exception as e:
            print(e)

    def stopInstance(self, instance_id, client_name, region):
        try:
            Client = self.__db["clients"]
            result = Client.find_one({"name": client_name})
            session = boto3.Session(
                aws_access_key_id=result["aws_access_key_id"],
                aws_secret_access_key=result["aws_secret_access_key"],
                region_name=region,
            )
            ec2 = session.resource("ec2")
            ec2 = ec2.Instance(instance_id)
            response = ec2.stop()
            if (
                response["StoppingInstances"][0]["CurrentState"]["Name"] == "stopping"
                or "stopped"
            ):
                return instance_id
            else:
                return None
        except Exception as e:
            print(e)

    def startInstance(self, instance_id, client_name, region):
        try:
            Client = self.__db["clients"]
            result = Client.find_one({"name": client_name})
            session = boto3.Session(
                aws_access_key_id=result["aws_access_key_id"],
                aws_secret_access_key=result["aws_secret_access_key"],
                region_name=region,
            )
            ec2 = session.resource("ec2")
            ec2 = ec2.Instance(instance_id)
            response = ec2.start()
            if (
                response["StartingInstances"][0]["CurrentState"]["Name"] == "starting"
                or "running"
            ):
                return instance_id
            else:
                return None
        except Exception as e:
            print(e)

    def restartInstance(self, instance_id, client_name, region):
        try:
            Client = self.__db["clients"]
            result = Client.find_one({"name": client_name})
            session = boto3.Session(
                aws_access_key_id=result["aws_access_key_id"],
                aws_secret_access_key=result["aws_secret_access_key"],
                region_name=region,
            )
            ec2 = session.client("ec2")
            response = ec2.reboot_instances(InstanceIds=[instance_id])
            
            if (response["ResponseMetadata"]["HTTPStatusCode"] == 200):
                return instance_id
            else:
                return None
        except Exception as e:
            print(e)