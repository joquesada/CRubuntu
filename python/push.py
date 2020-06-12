#!/usr/bin/env python 
 
def get_commands(vlan, name):
    commands.append('vlan ' + vlan)


def get_commands(vlan, name):
    commands = []
    commands.append('vlan ' + vlan)
    commands.append('name ' + name)
    return commands


def push_commands(device, commands):
    print('Connecting to device: ' + device)
    for cmd in commands:
        print('Sending command: ' + cmd)


if __name__ == "__main__":

    devices = ['10.10.10.10','10.10.10.11']
 
    vlans =[{'id': '10', 'name': 'USERS'},{'id': '20', 'name': 'VOICE'}]
 
 
    for vlan in vlans:
        id = vlan.get('id')
        name = vlan.get('name')
        print('\n')
        print('Configuring VLAN:' + id)
        commands = get_commands(id,name)
        for device in devices:
            push_commands(device, commands)
            print('\n')
