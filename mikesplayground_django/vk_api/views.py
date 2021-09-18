from django.shortcuts import render
import requests
import json


# Create your views here.
def socials_view(request, *args, **kwargs):
    context = {}
    return render(request, "socials.html", context)


def socials_view2(request, *args, **kwargs):
    # проходим авторизацию и получаем access_token
    code = request.GET.get('code')
    url = 'https://oauth.vk.com/access_token'
    parameters = {'client_id': 7780087, 'client_secret': 'Mm041e5HhGvVXmkTm9l2', 'redirect_uri': 'http://127.0.0.1:8000/socials2', 'code': code}
    # parameters = {'client_id': os.environ.get("client_id"), 'client_secret': os.environ.get("client_secret"), 'redirect_uri': 'https://rolliesplayground.herokuapp.com/socials2', 'code': code}
    response = requests.get(url, params = parameters)
    result = json.loads(response.content)
    access_token = result['access_token']
    #TODO {"error":"invalid_grant","error_description":"Code is expired."}
    
    # TODO период
    timestamp_from = 1609459200
    timestamp_to = 1615456104

    # узнаем ID и названия администрируемых групп
    vk_groups_request = requests.get(f'https://api.vk.com/method/groups.get?v=5.86&filter=admin,editor,moder&extended=1&access_token={access_token}')
    groups_reply = json.loads(vk_groups_request.content)

    groups_database = {}

    for group in range(groups_reply["response"]["count"]):
        # получаем лайки и репосты по ID каждой группы
        group_stats_request = requests.get(f'https://api.vk.com/method/stats.get?v=5.86&group_id={groups_reply["response"]["items"][group]["id"]}&access_token={access_token}&timestamp_from={timestamp_from}&timestamp_to={timestamp_to}&interval=all')
        reply = json.loads(group_stats_request.content)
        # получаем число подписчиков VK !на данный момент!
        members_request = requests.get(f'https://api.vk.com/method/groups.getById?v=5.86&group_id={groups_reply["response"]["items"][group]["id"]}&fields=members_count&access_token={access_token}')
        members_reply = json.loads(members_request.content)

        group_name = groups_reply["response"]['items'][group]["name"]
        group_members = members_reply["response"][0]["members_count"]

        if "activity" not in reply["response"][0]:
            group_likes, group_reposts = 0, 0
        else:
            group_likes = 0 if "likes" not in reply["response"][0]["activity"] else reply["response"][0]["activity"]["likes"]
            group_reposts = 0 if "copies" not in reply["response"][0]["activity"] else reply["response"][0]["activity"]["copies"]

        groups_database[groups_reply["response"]["items"][group]["id"]] = {"Groupname": group_name, "group_likes": group_likes, "group_reposts": group_reposts, "group_members": group_members}
    context = {'groups_database': groups_database}        
    return render(request, "socials2.html", context)
