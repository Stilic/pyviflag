import requests


def __init__(self, BaseUrl="https://flag.riverside.rocks/", userToken=""):
    self.baseUrl = BaseUrl
    self.userToken = userToken


def getVideoComments(self, id):
    """Returns all comments of a video."""
    res = requests.get(self.baseUrl + "api/v1/comments", params={"id": id})
    return res.json()


def getUserInfo(self, username):
    """Returns infos about a user."""
    res = requests.get(self.baseUrl + "api/v1/users",
                       params={"username": username})
    return res.json()


def getVideoInfo(self, id):
    """Returns infos about a video."""
    res = requests.get(self.baseUrl + "api/v1/videos", params={"id": id})
    return res.json()


def searchVideos(self, q):
    """Returns all results for a search."""
    res = requests.get(self.baseUrl + "api/v1/videos", params={"q": q})
    return res.json()


def getVideoStats(self, id):
    """Returns stats of a video."""
    res = requests.get(self.baseUrl + "api/v1/stats", params={"id": id})
    return res.json()


def deleteVideo(self, id):
    """Deletes a video and return the server's response."""
    res = requests.post(self.baseUrl + "api/v1/delete",
                        data={"user_token": self.userToken, "id": id})
    return res.json()


def setUserParams(self, announce=True, comments="", current=""):
    """Sets user's params."""
    res = requests.post(self.baseUrl + "api/v1/settings",
                        data={"annouce": announce, "comments": comments, "current": current})
    return res.json()
