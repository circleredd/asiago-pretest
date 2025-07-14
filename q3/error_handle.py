import requests

# A
url = "https://api.schedule.asiayo.com/"
headers = {
    "channel": "CP",
    "user": "rpa",
    "contentType": "application/JSON"
}

payload = {
    "price": "abc" 
}

response = requests.post(url, headers=headers, json=payload)



# B. 取出並顯示 errors

# 模擬拿到的回應 JSON：
resp_json = {
  "status": {
    "code": 500,
    "msg": "Validation failed."
  },
  "data": {
    "errors": "price: The price must be numeric"
  }
}


errors = resp_json.get("data", {}).get("errors")
print("Errors:", errors)


# C. 請說明什麼原因會造成 The price must be numeric

'''只要price 欄位不是一個可以直接轉成整數或浮點數的純數字字串，就會觸發「必須為數字」的驗證錯誤。'''
'''例如： 空字串, "abc", null ...等等'''