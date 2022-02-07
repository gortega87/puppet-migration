import subprocess


def format(array):
    array = array.splitlines()
    inventory = []
    for insta in array:
        inventory.append({'id': insta.split()[0], 'ip': insta.split()[1]})
    return inventory


class Inventory:

    def jarvis_terrain():
        terrain = input('Terrain to migrate: ')
        try:
            command = subprocess.run(['jarvis', 'ec2', 'find', '-t', terrain, '-o', 'id,private_ip', '-st', 'running', '--headless', ],
                                     stdout=subprocess.PIPE)
            return format(command.stdout.decode('utf-8'))

        except Exception as err:
            print(err)
            return None

    def jarvis_account():
        account = input('Account to migrate: ')
        try:
            command = subprocess.run(['jarvis', 'ec2', 'find', '-a', account, '-o', 'id,private_ip','-st', 'running', '--headless', ],
                                     stdout=subprocess.PIPE)
            return format(command.stdout.decode('utf-8'))
        except Exception as err:
            print(err)
            return None

    def jarvis_instance():
        ip = input('instance ip to migrate: ')
        try:
            command = subprocess.run(['jarvis', 'ec2', 'find', '-ip', ip, '-o', 'id,private_ip','-st', 'running', '--headless',],
                                     stdout=subprocess.PIPE)
            return format(command.stdout.decode('utf-8'))
        except Exception as err:
            print(err)
            return None


if __name__ == "__main__":
    print(Inventory.jarvis_terrain())
