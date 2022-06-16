
import requests
import json

if __name__ == '__main__':
    # res = requests.get('http://127.0.0.1:25081/api/mars/base/sop/communicateRecord/code?parentCode=1')
    # print(res.text)

    data = {
        'employeeIds':['xx']
    }
    res = requests.post('http://127.0.0.1:25081/api/mars/base/groupChat/getCustomerList',data=json.dumps(data),
                        headers={"Content-Type": "application/json; charset=UTF-8"})
    print(res.text)
