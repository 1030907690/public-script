
import requests
import json

if __name__ == '__main__':
    # res = requests.get('')
    # print(res.text)

    data = {

    }
    res = requests.post('',data=json.dumps(data),
                        headers={"Content-Type": "application/json; charset=UTF-8"})
    print(res.text)

    # requests.put()
