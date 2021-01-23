import requests

class PyViFlag:
    def __init__(self, BaseUrl="https://flag.riverside.rocks/", userToken=""):
        self.baseUrl = BaseUrl
        self.userToken = userToken

    def getVideoComments(self, id):
        res = requests.get(self.baseUrl + "api/v1/comments", params = {"id": id})
        return res.json()

    def getUserInfo(self, username):
        res = requests.get(self.baseUrl + "api/v1/users", params = {"username": username})
        return res.json()

    def getVideoInfo(self, id):
        res = requests.get(self.baseUrl + "api/v1/videos", params = {"id": id})
        return res.json()

    def searchVideos(self, q):
        res = requests.get(self.baseUrl + "api/v1/videos", params = {"q": q})
        return res.json()

    def getVideoStats(self, id):
        res = requests.get(self.baseUrl + "api/v1/stats", params = {"id": id})
        return res.json()

    def deleteVideo(self, id):
        requests.post(self.baseUrl + "api/v1/delete", data = {"user_token": self.userToken, "id": id})
        return res.json()

    def setUserParams(self, announce = True, comments = "", current = ""):
        requests.post(self.baseUrl + "api/v1/settings", data = {"annouce": announce, "comments": comments, "current": current})
        return res.json()