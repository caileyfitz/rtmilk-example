from app import app
from flask import render_template, request
from mekk.rtm import RtmClient, create_and_authorize_connector_prompting_for_api_key

APP_NAME = "rtm api test"
API_KEY = '8d1ab5ffd284dfa3fcddf93bb8027041'
SHARED_SECRET = '5584e57c68dfd482'

connector = create_and_authorize_connector_prompting_for_api_key(APP_NAME)
client = RtmClient(connector)


@app.route('/', methods=['GET', 'POST'])
def additem():
    task = request.form.get('addtask')

    web_list = client.find_or_create_list(u"Web List")

    if request.method == 'POST':
        if task:
            client.create_task(
                str(task),
                list_id=web_list.id)
    try:
        webtasklist = list(client.find_tasks(list_id=web_list.id))
    except KeyError:
        webtasklist = []

    # import pdb; pdb.set_trace()

    weblist_str = []

    # if webtasklist.name:
    for t in webtasklist:
        x = 10
        tname = t.name
        if tname:
            weblist_str.append(tname)

    print weblist_str
    return render_template('addtask.html',
                           title='Add',
                           weblist_str=weblist_str)
    return render_template('addtask.html',
                           title='Add',
                           weblist_str=weblist_str)
