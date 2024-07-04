from f5 import get_list_irule_profile
from f5 import get_session_token
from requests.auth import HTTPBasicAuth
import requests
import urllib3
import json
urllib3.disable_warnings()



username = 'admin'
password = 'Minhduan@123'

icms_base_url = 'http://127.0.0.1:8000/'
icms_username = 'admin'
icms_password = 'admin@123'


def get_list_f5_device():
    api = 'api/cm/f5/get-list-device'
    url = icms_base_url + api
    res = requests.get(url=url, auth=HTTPBasicAuth(icms_username, icms_password), verify=False)
    if res.ok:
        
        datalist = json.loads(res.text)['datalist']
        return {'status': 'success', 'datalist': datalist}
    else:
        error = res.text
        return {'status': 'failed', 'error': error}
    

def update_irule_profile(datalist):
    api = 'api/cm/f5/update-irule-profile'
    url = icms_base_url + api
    res = requests.post(url=url, json=datalist, auth=HTTPBasicAuth(icms_username, icms_password), verify=False)
    if res.ok:
        return {'status': 'success'}
    else:
        return {'status': 'failed'}


def main():
    get_list_f5_device_result = get_list_f5_device()
    if get_list_f5_device_result['status'] == 'success':
        list_f5_device_ip = get_list_f5_device_result['datalist']
        for f5_device_ip in list_f5_device_ip:
            base_url = f'https://{f5_device_ip}:8443/'
            get_session_token_result = get_session_token(
                base_url=base_url,
                username=username,
                password=password
            )
            if get_session_token_result['status'] == 'success':
                token = get_session_token_result['token']
                get_list_irule_profile_result = get_list_irule_profile(
                    base_url=base_url,
                    token=token
                )
                if get_list_irule_profile_result['status'] == 'success':
                    list_irule_profile = get_list_irule_profile_result['datalist']
                    update_data = dict()
                    update_data[f5_device_ip] = list_irule_profile
                    update_irule_profile_result = update_irule_profile(update_data)
                    if update_irule_profile_result['status'] == 'success':
                        print('Update server irule to ICMS success')
                    else:
                        error = update_irule_profile_result['error']
                        print(f'Update server irule to ICMS failed - error: {error}')
            else:
                error = get_session_token_result['error']
                print(f'Update server irule to ICMS failed - error: {error}')
    else:
        error = get_list_f5_device_result['error']
        print(f'Update server irule to ICMS failed - error: {error}')

if __name__ == '__main__':     
    main()