class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.index = 0
        print("null")

    def visit(self, url: str) -> None:
        self.history = self.history[:self.index + 1]
        self.history.append(url)
        self.index += 1
        print("null")

    def back(self, steps: int) -> str:
        self.index -= steps
        if self.index <= 0:
            self.index = 0
        print("back :",self.history[self.index])
        return self.history[self.index]

    def forward(self, steps: int) -> str:
        self.index += steps
        if len(self.history) <= self.index:
            self.index =  len(self.history)-1
        # print("length :",len(self.history),self.index)
        print("forward :",self.history[self.index])
        return self.history[self.index]



# Your BrowserHistory object will be instantiated and called as such:

browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("linkedin.com")
browserHistory.forward(4)
# browserHistory.back(2)
# browserHistory.back(7)


# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

# [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]