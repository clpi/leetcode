#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
import heapq

class Twitter(object):

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.time += 1
        self.tweets[userId].append((-self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        if userId in self.tweets:
            heap.extend(self.tweets[userId][-10:])
        if userId in self.follows:
            for followeeId in self.follows[userId]:
                if followeeId in self.tweets:
                    heap.extend(self.tweets[followeeId][-10:])
        heapq.heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            feed.append(heapq.heappop(heap)[1])
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

