import requests



req = "https://graph.facebook.com/v11.0/oauth/access_token?  \
    grant_type=fb_exchange_token&          \
    client_id=535783100778046& \
    client_secret=121f28a430e922b06a52c53eacf72b75& \
    fb_exchange_token=EAAHnSrlmBj4BAECQcPPrewnbkZAmoq6PVRkRscIPhLZByJpZCeM1vrJWGQ4MrasAnjN4Ua4PksjpUCm9HIhJCDjiGsxvaAiiR7cWcQnXKSOyatJDxW0GHGDBrZBPxak9jYc8qYZCbJTYTKSIi4a8VHsY8sICO4WfMjGS6QBO8UVeHqNeQQvef7hRrs7nZAhTqiaekBif8c48H45o43feypAd7dEvxtFxowpWn9AMsVcMGMXf1HQMMc" 

requests.get(req)

token = "EAAHnSrlmBj4BAECQcPPrewnbkZAmoq6PVRkRscIPhLZByJpZCeM1vrJWGQ4MrasAnjN4Ua4PksjpUCm9HIhJCDjiGsxvaAiiR7cWcQnXKSOyatJDxW0GHGDBrZBPxak9jYc8qYZCbJTYTKSIi4a8VHsY8sICO4WfMjGS6QBO8UVeHqNeQQvef7hRrs7nZAhTqiaekBif8c48H45o43feypAd7dEvxtFxowpWn9AMsVcMGMXf1HQMMc"
token2 = "EAAHnSrlmBj4BAFrV5gZA3GCQzmZArK1NfhJIjYH9Dxe28l67cUltNN49eHdo5NUGRN3ulrXEinwsmHeZBenbSa9PaXksLY0HnTBry9j2c7VENZCsDef8kSYfFkCjI1BRG8WxmxCGmlXgWGNk41jmZB6P2gmoDTGtjmF2MX2eCniKIDLPwb088uLyi9529XFgLRATIQ8yhJzgZBUZCAh14ahyYkJMBwM0tCwOBZBKmUh7ksrVho4xE9Bc"
token2 = "EAAHnSrlmBj4BAE1bZCev2rYjwPjDKv6Lcl7E45WDzkqyKbtFDlnxQeU2d2P6AbEFsNSywpF23iywhN9Imxt55PvqIOHNTZADGzZBUL1BqxIetsiutUcZCe3G1AKJTVEDGKBIFAGFCznoZBZBW2ZBGVvXBmTJuU5rx0KaynPztJ8xao4oAS6Y33tDBKBh2H61zbGHJac23GHyIoIYw3fdljLIhFVvKpvD7IQSseGjZBLCJXW7hpVi9OEk"


req2 = "https://graph.facebook.com/v11.0/me/accounts?access_token=" + token2


print(requests.get(req2).text)


req3 =  "https://graph.facebook.com/v11.0/107090291604237?fields=instagram_business_account&access_token=" + token2
print(requests.get(req3).text)

IGID = '17841447991814103'


req4 = "https://graph.facebook.com/v11.0/17841447991814103?fields=business_discovery.username(cristiano){followers_count,media_count}&access_token=" + token2
    
print(requests.get(req4).text)

info = '{biography,id,followers_count,media_count,username,website}'

req5 = "https://graph.facebook.com/v11.0/17841447991814103?fields=business_discovery.username(cristiano)" + info + "&access_token=" + token2
print(requests.get(req5).text)

import facebook

graph = facebook.GraphAPI(access_token=token2, version="3.1")



req = "https://graph.facebook.com/v9.0/me/accounts?access_token=" + token2

requests.get(req).text
