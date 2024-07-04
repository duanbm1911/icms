import requests
import urllib3
import json
urllib3.disable_warnings()


base_url = 'https://52.220.6.65:8443/'
username = 'admin'
password = 'Minhduan@123'

def get_session_token(base_url, username, password):
    api = 'mgmt/shared/authn/login'
    url = base_url + api
    data = {
        'username': username,
        'password': password,
        'loginProviderName': 'tmos'
    }
    res = requests.post(url=url, json=data, verify=False)
    if res.ok:
        token = json.loads(res.text)['token']['token']
        return {'status': 'success', 'token': token}
    else:
        error = json.loads(res.text)['message']
        return {'status': 'failed', 'error': error}

def get_node_name(base_url, token, node_ip):
    node_name = None
    api = 'mgmt/tm/ltm/node'
    url = base_url + api
    headers = {
        'X-F5-Auth-Token': token
    }
    res = requests.get(url=url, headers=headers, verify=False)
    if res.ok:
        list_node = json.loads(res.text)['items']
        checklist = [i['name'] for i in list_node if i['address'] == node_ip]
        if len(checklist) == 1:
            node_name = checklist[0]
        return {'status': 'success', 'node_name': node_name}
    else:
        error = json.loads(res.text)['message']
        return {'status': 'failed', 'error': error}
    
def get_list_irule_profile(base_url, token):
    api = 'mgmt/tm/ltm/rule'
    url = base_url + api 
    headers = {
        'X-F5-Auth-Token': token
    }
    res = requests.get(url=url, headers=headers, verify=False)
    if res.ok:
        res_data = json.loads(res.text)['items']
        datalist = list()
        if res_data:
            datalist = [i['name'] for i in res_data]
        return {'status': 'success', 'datalist': datalist}
    else:
        error = json.loads(res.text)['message']
        return {'status': 'failed', 'error': error}

def get_list_waf_profile(base_url, token):
    api = 'mgmt/tm/security/bot-defense/asm-profile'
    url = base_url + api 
    headers = {
        'X-F5-Auth-Token': token
    }
    res = requests.get(url=url, headers=headers, verify=False)
    if res.ok:
        res_data = json.loads(res.text)['items']
        datalist = list()
        if res_data:
            datalist = [i['name'].replace('ASM_','') for i in res_data if 'ASM_' in i['name']]
        return {'status': 'success', 'datalist': datalist}
    else:
        error = json.loads(res.text)['message']
        return {'status': 'failed', 'error': error}
    
def get_list_client_ssl_profile(base_url, token):
    api = 'mgmt/tm/ltm/profile/client-ssl'
    url = base_url + api 
    headers = {
        'X-F5-Auth-Token': token
    }
    res = requests.get(url=url, headers=headers, verify=False)
    if res.ok:
        res_data = json.loads(res.text)['items']
        datalist = list()
        if res_data:
            datalist = [i['name'] for i in res_data]
        return {'status': 'success', 'datalist': datalist}
    else:
        error = json.loads(res.text)['message']
        return {'status': 'failed', 'error': error}
    
def get_list_server_ssl_profile(base_url, token):
    api = 'mgmt/tm/ltm/profile/server-ssl'
    url = base_url + api 
    headers = {
        'X-F5-Auth-Token': token
    }
    res = requests.get(url=url, headers=headers, verify=False)
    if res.ok:
        res_data = json.loads(res.text)['items']
        datalist = list()
        if res_data:
            datalist = [i['name'] for i in res_data]
        return {'status': 'success', 'datalist': datalist}
    else:
        error = json.loads(res.text)['message']
        return {'status': 'failed', 'error': error}

def get_list_pool_monitor(base_url, token):
    list_protocol_based = ['http', 'tcp', 'udp']
    datalist = list()
    error = str()
    for protocol in list_protocol_based:
        api = f'mgmt/tm/ltm/monitor/{protocol}'
        url = base_url + api 
        headers = {
            'X-F5-Auth-Token': token
        }
        res = requests.get(url=url, headers=headers, verify=False)
        if res.ok:
            res_data = json.loads(res.text)['items']
            if res_data:
                datalist.extend([i['name'] for i in res_data])
        else:
            error = json.loads(res.text)['message']
    if not error:
        return {'status': 'success', 'datalist': datalist}
    else:
        return {'status': 'failed', 'error': error}


def create_node(base_url, token, node_ip):
    api = 'mgmt/tm/ltm/node'
    url = base_url + api
    headers = {
        'X-F5-Auth-Token': token
    }
    data = {
        'name': node_ip,
        'address': node_ip
    }
    res = requests.post(url=url, json=data, headers=headers, verify=False)
    if res.ok:
        return {'status': 'success'}
    else:
        error = json.loads(res.text)['message']
        return {'status': 'failed', 'error': error}

def create_pool(base_url, token, vs_data):
    api = 'mgmt/tm/ltm/pool'
    url = base_url + api
    headers = {
        'X-F5-Auth-Token': token
    }
    pool_items = list()
    list_new_pool_member = list()
    list_pool_member = vs_data['pool_member']
    check_node_name_error = ""
    for pool_member in list_pool_member:
        member_ip = pool_member.split(':')[0]
        member_port = pool_member.split(':')[1]
        get_node_name_result = get_node_name(base_url=base_url, token=token, node_ip=member_ip)
        if get_node_name_result['status'] == 'success':
            node_name = get_node_name_result['node_name']
            if node_name is not None:
                member_ip = node_name
                list_new_pool_member.append(f'{node_name}:{member_port}')
            else:
                list_new_pool_member.append(f'{member_ip}:{member_port}')
        else:
            check_node_name_error = get_node_name_result['error']
    if not check_node_name_error:
        for pool_member in list_new_pool_member:
            pool_items.append({
                'name': pool_member
            })
        data = {
            'name': vs_data['pool_name'],
            'monitor': f'/Common/{vs_data["pool_monitor"]}',
            'loadBalancingMode': vs_data['pool_lb_method'],
            'membersReference': {
                'items': pool_items
            }
        }
        res = requests.post(url=url, json=data, headers=headers, verify=False)
        if res.ok:
            return {'status': 'success'}
        else:
            error = json.loads(res.text)['message']
            return {'status': 'failed', 'error': error}
    else:
        return {'status': 'failed', 'error': check_node_name_error}


def create_vs(base_url, token, vs_data):
    api = 'mgmt/tm/ltm/virtual'
    url = base_url + api
    headers = {
        'X-F5-Auth-Token': token
    }
    profile_list = list()
    if vs_data['client_ssl_profile']:
        profile_list.append({
            'name': vs_data['client_ssl_profile'],
            'context': 'clientside'
        })
    if vs_data['server_ssl_profile']:
        profile_list.append({
            'name': vs_data['server_ssl_profile'],
            'context': 'serverside'
        })
    if vs_data['client_protocol_profile']:
        profile_list.append({
            'name': vs_data['client_protocol_profile'],
            'context': 'all'
        })
    if vs_data['server_protocol_profile'] != vs_data['client_protocol_profile']:
        profile_list.append({
            'name': vs_data['server_protocol_profile'],
            'context': 'all'
        })
    if vs_data['client_http_profile']:
        profile_list.append({
            'name': vs_data['client_http_profile'],
            'context': 'all'
        })
    if vs_data['server_http_profile'] != vs_data['client_http_profile']:
        profile_list.append({
            'name': vs_data['server_http_profile'],
            'context': 'all'
        })
    if vs_data['http_analytics_profile']:
        profile_list.append({
            'name': vs_data['http_analytics_profile'],
            'context': 'all'
        })
    if vs_data['tcp_analytics_profile']:
        profile_list.append({
            'name': vs_data['tcp_analytics_profile'],
            'context': 'all'
        })
    if vs_data['http_compression_profile']:
        profile_list.append({
            'name': vs_data['http_compression_profile'],
            'context': 'all'
        })
    if vs_data['web_acceleration_profile']:
        profile_list.append({
            'name': vs_data['web_acceleration_profile'],
            'context': 'all'
        })
    if vs_data['waf_profile']:
        profile_list.append({
            'name': 'websecurity',
            'context': 'all'
        })
    data = {
        'name': vs_data['vs_name'],
        'partition': vs_data['partition'],
        'destination': f'/{vs_data["partition"]}/{vs_data["vs_ip"]}:{vs_data["vs_port"]}',
        'ipProtocol': vs_data['protocol'],
        'pool': vs_data['pool_name'],
        'profilesReference': {
            'items': profile_list
        }
    }
    if vs_data['irules']:
        data['rules'] = vs_data['irules']
    if vs_data['snat_name'] == 'automap':
        data['sourceAddressTranslation'] = {'type': 'automap'}
    else:
        data['sourceAddressTranslation'] = {'type': 'automap', 'pool': f'/Common/{vs_data["snat_name"]}'}
    if vs_data['waf_profile']:
        data['policiesReference'] = {'items': [{'name': f'asm_auto_l7_policy__{vs_data["vs_name"]}'}]}
    res = requests.post(url=url, json=data, headers=headers, verify=False)
    if res.ok:
        return {'status': 'success'}
    else:
        error = json.loads(res.text)['message']
        return {'status': 'failed', 'error': error}


def create_asm_policy(base_url, token, vs_data):
    api = 'mgmt/tm/ltm/policy'
    url = base_url + api
    headers = {
        'X-F5-Auth-Token': token
    }
    data = {
        "name": f"asm_auto_l7_policy__{vs_data['vs_name']}",
        "partition": "/Common/Drafts/",
        "controls": [
            "asm"
        ],
        "requires": [
            "http"
        ],
        "status": "legacy",
        "strategy": "/Common/first-match",
        "rules": [
            {
            "name": "default",
            "fullPath": "default",
            "ordinal": 1,
            "actions": [
                {
                "name": "1",
                "fullPath": "1",
                "asm": True,
                "code": 0,
                "enable": True,
                "expirySecs": 0,
                "length": 0,
                "offset": 0,
                "policy": vs_data['waf_profile'],
                "port": 0,
                "request": True,
                "status": 0,
                "timeout": 0,
                "vlanId": 0
                }
            ]}
        ]}
    res = requests.post(url=url, json=data, headers=headers, verify=False)
    if res.ok:
        return {'status': 'success'}
    else:
        error = json.loads(res.text)['message']
        return {'status': 'failed', 'error': error}

def publish_asm_policy(base_url, token, vs_data):
    api = 'mgmt/tm/ltm/policy'
    url = base_url + api
    headers = {
        'X-F5-Auth-Token': token
    }
    data = {
        'command': 'publish', 
        'name': f'/Common/Drafts/asm_auto_l7_policy__{vs_data["vs_name"]}'
        }
    res = requests.post(url=url, json=data, headers=headers, verify=False)
    if res.ok:
        return {'status': 'success'}
    else:
        error = json.loads(res.text)['message']
        return {'status': 'failed', 'error': error}

if __name__ == '__main__':
    vs_data = {
      "task_id": 11,
      "f5_device_ip": "10.29.10.44",
      "vs_name": "ocp-1.1.1.1-443-vs",
      "vs_ip": "1.1.1.1",
      "vs_port": 443,
      "pool_name": "ocp-test-1.1.1.1-443-pool",
      "pool_member": [
        "1.1.1.1:443",
        "1.1.1.3:443"
      ],
      "pool_monitor": "http",
      "pool_lb_method": "ratio-member",
      "client_ssl_profile": "client-ssl-01",
      "server_ssl_profile": "server-ssl-profile-02",
      "protocol": "",
      "client_protocol_profile": "",
      "server_protocol_profile": "",
      "client_http_profile": "",
      "server_http_profile": "",
      "snat_name": "",
      "http_analytics_profile": "",
      "tcp_analytics_profile": "",
      "http_compression_profile": "",
      "web_acceleration_profile": "",
      "waf_profile": "waf-profile-01",
      "irules": [
        "irule-01",
        "irule-02"
      ]
    }
    token = get_session_token(base_url, username, password)['token']
    result = get_list_pool_monitor(base_url, token)
    print(result)