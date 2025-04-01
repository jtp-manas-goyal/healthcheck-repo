# this is for the test thing website actions 
listOfWebsites = [
    "https://bizsapo.ai.smrj.go.jp/",
    "https://startup-chat.ai.smrj.go.jp/"    
]
listOfAllActions =  [
    {
        "actions" : {
            "actions" : [
                {"action" : "goto" , "url" : "https://bizsapo.ai.smrj.go.jp/" , "errorval" : 1} ,
                {"action" : "click" , "selector" : "//*[@id='chatArea']/div/div[2]/div/p/p[2]/input[1]" , "errorval" : 2} ,
                {"action" : "click" , "selector" : "//*[@id='chatArea']/div[3]/div[2]/div/p/p[2]/input[1]" , "errorval" : 3} ,
                {"action" : "check_text" , "selector" : "//*[@id='chatArea']/div[5]/div[2]/div/p/p[1]", "expected_text" :  "中小企業向け支援策についてのご質問ですね。ご質問内容をお選びください。" , "errorval" : 4}
            ]
        }
    }
    ,
    {
        # 2 #the second website - startup-chat 
        "actions" : {
            "actions" : [
                {"action" : "goto" , "url" : "https://startup-chat.ai.smrj.go.jp/" , "errorval" : 1} ,
                {"action" : "click" , "selector" : "//*[@id='chatArea']/div[1]/div[2]/div/p/p[2]/input[1]" , "errorval" : 2} ,
                {"action" : "click" , "selector" : "//*[@id='chatArea']/div[4]/div[2]/div/p/p[2]/input[1]" , "errorval" : 3} ,
                {"action" : "check_text" , "selector" : "//*[@id='chatArea']/div[6]/div[2]/div/p/p", "expected_text" : "起業は、やりたいことや夢が実現できる反面、リスクがあるのも事実だ。失敗はすべて自己責任だし、収入だってどうなるか分からない。それでも、起業する人がいるのは、リスクを超える魅力や成し遂げたい夢があるからだ。君にとっての起業の魅力や大変さを見極めて、起業がベストな選択肢なのかを判断するといいぞ。" , "errorval" : 4}
            ]
        }
    }
    ]


# To make listOfAllActions accessible, you can use it as a module-level variable.
listOfAllActions