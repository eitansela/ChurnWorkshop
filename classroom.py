import json

myurl = 'https://3nzierhu10.execute-api.us-east-1.amazonaws.com/prod/results'
person = None
is_call_home = True

def init_classroom(person_name, call_home=True):
    global person
    global is_call_home
    person = person_name
    is_call_home = call_home
    
def _post(post_type, value, extra_payload = None):
    if not is_call_home:
        return "skipped calling home"

    import time
    epoch_time = int(time.time())

    global person
    assert(person and person!='YOUR_NAME_HERE_AS_STRING')

    body = {
        "person":person,
        "type": post_type,
        "value":value,
        "extra_payload":extra_payload,
        "modify-epoch":epoch_time
    }

    #print(body)
    
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes

    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'Content-Length': len(jsondataasbytes)
    }

    from urllib.parse import urlencode
    from urllib.request import Request, urlopen

    req = Request(myurl, headers=headers)
    res = urlopen(req, jsondataasbytes).read().decode("utf-8")
    return res


def report_progress(progress_int):
    return _post("workshop progress", progress_int)


def report_algo_objective(objective_value, hyperparam_dict):
    return _post("algo.objective", objective_value, hyperparam_dict)
