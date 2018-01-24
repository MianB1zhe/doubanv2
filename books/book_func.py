# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from books.models import DoubanUser
import utils

import requests
import json
from datetime import datetime

USER_INFO_API = 'https://api.douban.com/v2/user/{0}'

def get_user_info(user_id):
    # try to find user in database where id = userid 
    try:
        user = DoubanUser.objects.get(user_id=user_id)
        user.access_times = user.access_times + 1
        user.save()
        return user.user_id
    except DoubanUser.DoesNotExist:
        pass

    # try to find user in database where uid = userid
    try:
        user = DoubanUser.objects.get(user_uid=user_id)
        user.access_times = user.access_times + 1
        user.save()
        return user.user_id
    except DoubanUser.DoesNotExist:
        pass

    # if up fails, then get user info from douban.com
    res = requests.get(USER_INFO_API.format(user_id))
    user_info = json.loads(res.content)
    new_user = DoubanUser(
        user_id = user_info['id'],
        user_uid = user_info['uid'],
        name = user_info['name'],
        created_at_douban = utils.str2date(user_info['created']),
        loc_name = user_info['loc_name'],
        avatar = user_info['avatar'].split('com/')[1],
        signature = user_info['signature'],
        desc = user_info['desc'],
        created_at = datetime.now(),
        access_times = 1
        )
    new_user.save()
    return new_user.user_id