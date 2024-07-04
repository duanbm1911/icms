from f5 import get_session_token
from f5 import create_pool
from f5 import create_vs
from f5 import create_asm_policy
from f5 import publish_asm_policy
from requests.auth import HTTPBasicAuth
import requests
import urllib3
import json
urllib3.disable_warnings()


icms_base_url = 'http://127.0.0.1:8000/'
icms_username = 'admin'
icms_password = 'admin@123'


username = 'admin'
password = 'Minhduan@123'

def get_list_virtual_server():
    api = 'api/cm/f5/get-list-virtual-server'
    url = icms_base_url + api
    res = requests.get(url=url, auth=HTTPBasicAuth(icms_username, icms_password), verify=False)
    if res.ok:
        datalist = json.loads(res.text)['datalist']
        return {'status': 'success', 'datalist': datalist}
    else:
        error = json.loads(res.text)['error']
        return {'status': 'Failed', 'error': error}
    
def update_task_status(results):
    api = 'api/cm/f5/update-virtual-server-status'
    url = icms_base_url + api
    res = requests.post(url=url, json=results, auth=HTTPBasicAuth(icms_username, icms_password), verify=False)
    if res.ok:
        return {'status': 'success'}
    else:
        error = res.text
        return {'status': 'Failed', 'error': error}

def main():
    results = {}
    get_list_virtual_server_result = get_list_virtual_server()
    if get_list_virtual_server_result['status'] == 'success':
        datalist = get_list_virtual_server_result['datalist']
        for vs_data in datalist:
            task_id = vs_data['task_id']
            f5_device_ip = vs_data['f5_device_ip']
            waf_profile = vs_data['waf_profile']
            base_url = f'https://{f5_device_ip}:8443/'
            get_session_token_result = get_session_token(
                base_url=base_url,
                username=username,
                password=password
            )
            if get_session_token_result['status'] == 'success':
                token = get_session_token_result['token']
                create_pool_result = create_pool(
                    base_url=base_url,
                    token=token,
                    vs_data=vs_data
                )
                if create_pool_result['status'] == 'success':
                    if waf_profile:
                        create_asm_policy_result = create_asm_policy(
                            base_url=base_url,
                            token=token,
                            vs_data=vs_data
                        )
                        if create_asm_policy_result['status'] == 'success':
                            publish_asm_policy_result = publish_asm_policy(
                                base_url=base_url,
                                token=token,
                                vs_data=vs_data
                            )
                            if publish_asm_policy_result['status'] == 'success':
                                create_vs_result = create_vs(
                                    base_url=base_url,
                                    token=token,
                                    vs_data=vs_data
                                )
                                if create_vs_result['status'] == 'success':
                                    results[task_id] = ['success', '']
                                else:
                                    error = create_vs_result['error']
                                    results[task_id] = ['Failed', error]
                            else:
                                error = publish_asm_policy_result['error']
                                results[task_id] = ['Failed', error]
                        else:
                            error = create_asm_policy_result['error']
                            results[task_id] = ['Failed', error]
                    else:
                        create_vs_result = create_vs(
                            base_url=base_url,
                            token=token,
                            vs_data=vs_data
                        )
                        if create_vs_result['status'] == 'success':
                            results[task_id] = ['success', '']
                        else:
                            error = create_vs_result['error']
                            results[task_id] = ['Failed', error]
                else:
                    error = create_pool_result['error']
                    results[task_id] = ['Failed', error]
            else:
                error = get_session_token_result['error']
                results[task_id] = ['Failed', error]
        update_task_status_result = update_task_status(results=results)
        if update_task_status_result['status'] == 'success':
            print('Update to ICMS success')
        else:
            error = update_task_status_result['error']
            print(f'Update to ICMS failed - error: {error}')
    else:
        error = get_list_virtual_server_result['error']
        print(f'Get data from ICMS failed - error: {error}')
        
if __name__ == '__main__':
    main()