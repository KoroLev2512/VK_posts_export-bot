import requests


class VkApi:
    def __init__(self, access_token, version):
        self.base_url = f"https://api.vk.com/method"
        self.access_token = access_token
        self.version = version

    def wall_get_by_id(self, posts):
        method_name = self.base_url + "/wall.getById"
        data = {"posts": posts, "access_token": self.access_token, "v": self.version}
        response = requests.post(method_name, data=data)
        return response.json()
