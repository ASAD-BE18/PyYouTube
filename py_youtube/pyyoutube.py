"""
(C) @mrlokaman 
All rights reserved by LN Technical

"""

"""
MIT License

Copyright (c) 2021 Lntechnical

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


# This Modules Helps To Get Youtube Video Data




import re
import urllib.request
import json
class Data:

    """
      Get YouTube Video Data 

    """

    def __init__(self, link):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
                     'Accept-Language': 'en-US,en;q=0.5'}
        res = urllib.request.Request(link, headers=headers)
        html = urllib.request.urlopen(res)
        self.source = html.read().decode('utf8')
        with open('source.json', 'w') as f:
            json.dump(self.source, f, indent=4)
    # Get Video id

    def id(self):
        try:
            videodetails = re.findall(
                "\"videoDetails\":\{(.+?),\"isOwnerViewing", self.source)[0]
        except:
            return None
        try:
            # Get id , title From videodetails variable
            id = re.findall("\"videoId\":\"(\S{11})", videodetails)[0]
            return id
        except:
            return None

    # Get Video Title

    def title(self):
        try:
            videodetails = re.findall(
                "\"videoDetails\":\{(.+?),\"isOwnerViewing", self.source)[0]
        except:
            return None
        try:
            # Get id , title From videodetails variable
            title = re.findall("\"title\":\"(.+?)\",", videodetails)[0]
            return title
        except:
            return None

    # Get Thumbnails Link From Youtube Video

    def thumb(self):
        try:
            thumb = re.findall(
                "\"thumbnails\":\[\{\"url\":\"(.+?)\",\"width", self.source)[0]
            return thumb
        except:
            return None

     # Get Video Publish Date

    def publish_date(self):
        try:
            publish_date = re.findall(
                "\"publishDate\":\"(\d{4}-\d{2}-\d{2})", self.source)[0]
            return publish_date
        except:
            return None

    # Get Views Of the Video

    def views(self):
        try:
            views = re.findall("\"viewCount\":\"(\d+)", self.source)[0]
            return views
        except:
            return None

    # Get Category Of The Video

    def category(self):
        try:
            category = re.findall("\"category\":\"(.+?)\",", self.source)[0]
            return category
        except:
            return None

    # Get Channel Name

    def channel_name(self):
        try:
            channelName = e.findall(
                "\"channelName\":\"(.+?)\",", self.source)[0]
            return channelName
        except:
            try:
                channelName = re.findall(
                    "\"ownerChannelName\":\"(.+?)\",\"uploadDate", self.source)[0]
                return channelName
            except:
                return None

    # Get likes Of The Video

    def likes(self):

        try:
            likes = re.findall("accessibilityData\":{\"label\":\"(\S+) likes", self.source)[0]
            return likes
        except:
            pass

        try:
            likes = re.findall(
                "iconType\":\"LIKE\"},\"defaultText\":{\"accessibility\":{\"accessibilityData\":{\"label\":\"(.+?)\"}}", self.source)[0]
            likes = likes.split(" ")[0]
            return likes
        except:
            return None

    # Get dislikes Of The Video

    def dislikes(self):
        try:
            dislikes = re.findall(
                "accessibilityData\":{\"label\":\"(\S+) dislike", self.source)[0]
            return dislikes
        except:
            return None

    # Get YouTube Videos tag
    def tags(self):
        try:
            tags = re.findall(
                "\<meta name=\"keywords\" content=\"(.+?)\">", self.source)[0]
            return tags
        except:
            return None

    # Get Subscriber of The video

    def subscriber(self):
        try:
            sub = re.findall(
                "subscriberCountText\":{\"accessibility\":{\"accessibilityData\":{\"label\":\"(.+?)\"}}", self.source)[0]
            return sub
        except:
            try:
                sub = re.findall(
                    "accessibilityData\":{\"label\":\"(\S+) subscribers", self.source)[0]
                return sub
            except:
                return None

    def data(self):
        try:
            # Get Video Details
            videodetails = re.findall(
                "\"videoDetails\":\{(.+?),\"isOwnerViewing", self.source)[0]
        except:
            videodetails = None
        try:
            # Get id , title From videodetails variable
            id = re.findall("\"videoId\":\"(\S{11})", videodetails)[0]
            title = re.findall("\"title\":\"(.+?)\",", videodetails)[0]
        except:
            title = None
            id = None
        try:
            # Get Thumbnails Link From Youtube Video
            thumb = re.findall(
                "\"thumbnails\":\[\{\"url\":\"(.+?)\",\"width", self.source)[0]
        except:
            thumb = None
        try:
            # Get Video Publish Date
            publish_date = re.findall(
                "\"publishDate\":\"(\d{4}-\d{2}-\d{2})", self.source)[0]
        except:
            publish_date = None
        try:
            # Get Views Of the Video
            views = re.findall("\"viewCount\":\"(\d+)", self.source)[0]
        except:
            views = None
        try:
            # Get Category Of The Video
            category = re.findall("\"category\":\"(.+?)\",", self.source)[0]
        except:
            category = None
        try:
            # Get Channel Name
            channelName = e.findall(
                "\"channelName\":\"(.+?)\",", self.source)[0]
        except:
            try:
                channelName = re.findall(
                    "\"ownerChannelName\":\"(.+?)\",\"uploadDate", self.source)[0]
            except:
                channelName = None

        likes = None
        try:
            likes = re.findall("accessibilityData\":{\"label\":\"(\S+) likes", self.source)[0]
        except:
            pass
        
        if likes is None:
            try:
                # Get likes Of The Video
                likes = re.findall(
                    "iconType\":\"LIKE\"},\"defaultText\":{\"accessibility\":{\"accessibilityData\":{\"label\":\"(.+?)\"}}", self.source)[0]
            except:
                likes = None

        try:
            # Get dislikes Of The Video
            dislikes = re.findall(
                "accessibilityData\":{\"label\":\"(\S+) dislike", self.source)[0]
        except:
            dislikes = None
        try:
            # Get Subscriber of The video
            sub = re.findall(
                "accessibilityData\":{\"label\":\"(\S+) subscribers", self.source)[0]
        except:
            try:
                sub = re.findall(
                    "subscriberCountText\":{\"accessibility\":{\"accessibilityData\":{\"label\":\"(.+?)\"}}", self.source)[0]
            except:
                sub = None
            # kewords(tag)
        try:
            tags = re.findall(
                "\<meta name=\"keywords\" content=\"(.+?)\">", self.source)[0]
        except:
            tags = None

        DATA = {
            "id": id,
            "title": title,
            "thumbnails": thumb,
            "views": views,
            "likes": likes,
            "dislikes": dislikes,
            "publishdate": publish_date,
            "category": category,
            "channel_name": channelName,
            "subscriber": sub,
            "keywords": tags
        }
        return DATA
