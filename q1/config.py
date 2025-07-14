from collections import OrderedDict

# proxy pool
proxies = []

headers_list = [
    {
        # Windows 10 上 Chrome
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0.5790.102 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    },
    {
        # macOS 上 Firefox
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.5; rv:117.0) "
                      "Gecko/20100101 Firefox/117.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    },
    {
        # iPhone 上 Safari
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) "
                      "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                      "Version/17.5 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    },
    {
        # Windows 11 上 Edge
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0.5790.110 Safari/537.36 Edg/115.0.1901.203",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    },
    {
        # Android 上 Chrome
        "User-Agent": "Mozilla/5.0 (Linux; Android 14; Pixel 8) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0.5790.102 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    },
]

main_tabs: list[str] = [
    "sellwell-marathon", "JP-marathon", "mountain", "int-marathon", "int-bike", "int-golf"
]


tabs = OrderedDict([
    ("sellwell-marathon",  ["Hotsalecompetition", "PRrunner", "newrunner", "Seniorrunner", "Hotsaleproject"]),
    ("JP-marathon",        ["autumn-jpmarathon", "winter-jpmarathon", "spring-jpmarathon", "summer-jpmarathon", "super-marathon", "all-JPmarathon"]),
    ("mountain",           ["jp-mountain", "SoutheastAsia-mountain"]),
    ("int-marathon",       ["kr-marathon", "hk-marathon", "vn-marathon"]),
    ("int-bike",           []),
    ("int-golf",           ["th-golf", "jp-golf", "kr-golf"]),
])


# 展平成 (main, sub) tuple 的清單
tab_pairs = [
    (main, sub)
    for main, subs in tabs.items()
    for sub in (subs if subs else [None])
]

# tabs :dict[str, list[str]]= {
#     "sellwell-marathon":[
#         "Hotsalecompetition", "PRrunner", "newrunner", "Seniorrunner", "Hotsaleproject"
#     ],
#     "JP-marathon":[
#         "autumn-jpmarathon", "winter-jpmarathon", "spring-jpmarathon", "summer-jpmarathon", "super-marathon", "all-JPmarathon"
#     ],
#     "mountain":[
#         "jp-mountain", "SoutheastAsia-mountain"
#     ],
#     "int-marathon":[
#         "kr-marathon", "hk-marathon", "vn-marathon"
#     ],
#     "int-bike":[],
#     "tw-marathon":[
#         "tw-marathon"
#     ],
#     "int-golf":[
#         "th-golf", "jp-golf", "kr-golf"
#     ]
# }