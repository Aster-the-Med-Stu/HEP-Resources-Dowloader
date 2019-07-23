# 返回的 JSON 记录

## 登录

POST http://abook.hep.com.cn/loginMobile.action?loginUser.loginName={REDACTED}&loginUser.loginPassword={REDACTED} HTTP/1.1

可不带 Cookie 和 User-Agent 之类的，重点在于拿到的 icourse_SESSION。

### 返回的 JSON
```json
[
    {
        "message": "successful"
    }
]
```

如果，密码错误，返回 JSON：

```json
[
    {
        "message":"账号或密码错误"
    }
]
```

### 验证登录

拿着上面的 icourse_SESSION：

POST http://abook.hep.com.cn/verifyLoginMobile.action HTTP/1.1

登录成功：

```json
{"message":"已登录"}
```

如果登录失败：

```json
{"message":"未登录"}
```

## 列出课程列表

GET http://abook.hep.com.cn/selectMyCourseList.action?mobile=true&cur=1 HTTP/1.1

返回 JSON：

```json
[
    {
        "myMobileCourseList": [
            {
                "appPicUrl": "/courseImg/155410629359915541062952571554106295257.jpg",
                "applyDateTime": "2019-04-17 15:28:06.0",
                "beginCourseDate": "2019-04-17 15:28:06.0",
                "courseInfoId": 5000003302,
                "coursePrincipalName": "",
                "courseTitle": "病理生理学（第2版）",
                "descAttach": "<font style='font-size:17px;color:#2977A8;'>课程简介</font><br><p>&ldquo;病理生理学&rdquo;数字课程与纸质教材配套使用，是纸质教材的拓展和补充。数字课程内容包括教学课件、操作视频、拓展学习等，丰富知识的呈现形式，有助于提升教学效果，方便学生自主学习。</p><HR style='FILTER: alpha(opacity=100,finishopacity=0,style=3)' width='100%' color=#DBDBDB SIZE=1><font style='font-size:17px;color:#2977A8;'>版权信息</font><br><p>作品名称：病理生理学数字课程</p><p>出版时间：2019年02月</p><p>出&nbsp;&nbsp;&nbsp; 版：高等教育出版社 高等教育电子音像出版社</p><p>内容提供者：姜勇 等</p><p>策划编辑：杨兵</p><p>技术编辑：李翠玲</p><p>本网站资源的专有出版权归高等教育出版社所有，未经出版者预先书面许可，任何单位和个人不得为任何目的、以任何形式或手段复制和传播本课件的任何部分，出版者保留一切法律追究的权利。</p><HR style='FILTER: alpha(opacity=100,finishopacity=0,style=3)' width='100%' color=#DBDBDB SIZE=1><font style='font-size:17px;color:#2977A8;'>联系方式</font><br><p>内容编辑：张家琛</p><p>电话：010-58581974</p><p>E-mail：zhangjc@hep.com.cn</p><p>技术咨询：李翠玲</p><p>电话：010-58556656</p><p>E-mail：abook@hep.com.cn</p>",
                "endCourseDate": "",
                "indexPicUrl": "/MaterialsLibCovers/NZKTA3Q7KX.jpg",
                "isEndCourseDate": null,
                "loginName": "marchhappy",
                "picUrl": "/MaterialsLibCovers/NZKTA3Q7KX.jpg",
                "picUrl1": "/MaterialsLibCovers/NZKTA3Q7KX.jpg",
                "trueName": "{REDACTED}"
            },
            {
                "appPicUrl": "/courseImg/41524-00_front.jpg",
                "applyDateTime": "2019-03-18 11:12:42.0",
                "beginCourseDate": "2019-03-18 11:12:42.0",
                "courseInfoId": 5000000693,
                "coursePrincipalName": "tea41524",
                "courseTitle": "病理学",
                "descAttach": "<font style='font-size:17px;color:#2977A8;'>课程简介</font><br><p>病理学数字课程与纸质教材一体化设计，紧密配合。数字课程分图片、微视频、知识拓展、历代著名病理学家介绍、本章小结、自测题、教学PPT等资源。充分运 用多种形式媒体资源，极大地丰富了知识的呈现形式，拓展了教材内容。在提升课程教学效果同时，为学生学习提供思维与探索的空间。</p><HR style='FILTER: alpha(opacity=100,finishopacity=0,style=3)' width='100%' color=#DBDBDB SIZE=1><font style='font-size:17px;color:#2977A8;'>版权信息</font><br><p>作品名称：病理学数字课程（基础版）</p><p>出版时间：2015年12月</p><p>出 版 社：高等教育出版社&nbsp; 高等教育电子音像出版社</p><p>内容提供者：来茂德 申洪</p><p>策划编辑：杨兵</p><p>技术编辑：赵莉</p><p>本网站资源的专有出版权归高等教育出版社所有，未经出版者预先书面许可，任何单位和个人不得为任何目的、以任何形式或手段复制和传播本课件的任何部分，出版者保留一切法律追究的权利。</p><HR style='FILTER: alpha(opacity=100,finishopacity=0,style=3)' width='100%' color=#DBDBDB SIZE=1><font style='font-size:17px;color:#2977A8;'>联系方式</font><br><p>内容编辑：杨兵&nbsp;&nbsp;&nbsp; 电话：010-58581441&nbsp;&nbsp;&nbsp; E-mail：yangbing@hep.com.cn</p><p>技术咨询：赵莉&nbsp;&nbsp;&nbsp; 电话：010-58581431&nbsp;&nbsp;&nbsp; E-mail：zhaoli@hep.com.cn</p>",
                "endCourseDate": "",
                "indexPicUrl": "/MaterialsLibCovers/group1/M00/0D/9F/wKhLR1dx5RmAatd6AARuwDgpq18241.jpg",
                "isEndCourseDate": null,
                "loginName": "marchhappy",
                "picUrl": "/MaterialsLibCovers/group1/M00/0D/9F/wKhLR1dx5RmAatd6AARuwDgpq18241.jpg",
                "picUrl1": "/MaterialsLibCovers/group1/M00/0D/9F/wKhLR1dx5RmAatd6AARuwDgpq18241.jpg",
                "trueName": "{REDACTED}"
            },
            {
                "appPicUrl": "/courseImg/152489430759515248943095231524894309523.jpg",
                "applyDateTime": "2018-09-10 10:32:57.0",
                "beginCourseDate": "2018-09-10 10:32:57.0",
                "courseInfoId": 5000002983,
                "coursePrincipalName": "",
                "courseTitle": "局部解剖学（第3版） ",
                "descAttach": "<font style='font-size:17px;color:#2977A8;'>课程简介</font><br><p>局部解剖学（第3版）数字课程与纸质教材一体化设计，紧密配合。数字课程资源包括各章教学PPT、自测题，在提升课程教学效果的同时，为学生学习提供思维与探索的空间。</p><HR style='FILTER: alpha(opacity=100,finishopacity=0,style=3)' width='100%' color=#DBDBDB SIZE=1><font style='font-size:17px;color:#2977A8;'>版权信息</font><br><p><strong>作品名称：</strong>&ldquo;局部解剖学（第3版）&rdquo;数字课程</p><p><strong>出版时间：</strong>2018年5月</p><p><strong>出版：</strong>高等教育出版社 高等教育电子音像出版社</p><p><strong>内容提供者：</strong>欧阳钧</p><p><strong>策划编辑：</strong>瞿德竑</p><p><strong>技术编辑：</strong>赵莉</p><p>本网站资源的专有出版权归高等教育出版社所有，未经出版者预先书面许可，任何单位和个人不得为任何目的、以任何形式或手段复制和传播本课件的任何部分，出版者保留一切法律追究的权利。</p><HR style='FILTER: alpha(opacity=100,finishopacity=0,style=3)' width='100%' color=#DBDBDB SIZE=1><font style='font-size:17px;color:#2977A8;'>联系方式</font><br><p>内容编辑：瞿德竑</p><p>电话：010-58581034</p><p>E-mail：qudh@hep.com.cn</p><p>技术咨询：赵莉</p><p>电话：010-58581431</p><p>E-mail：abook@hep.com.cn</p>",
                "endCourseDate": "",
                "indexPicUrl": "/MaterialsLibCovers/group1/M00/16/E1/wKhLSFrkIRyAKSpqAAHif8BX_zs035.jpg",
                "isEndCourseDate": null,
                "loginName": "marchhappy",
                "picUrl": "/MaterialsLibCovers/group1/M00/16/E1/wKhLSFrkIRyAKSpqAAHif8BX_zs035.jpg",
                "picUrl1": "/MaterialsLibCovers/group1/M00/16/E1/wKhLSFrkIRyAKSpqAAHif8BX_zs035.jpg",
                "trueName": "{REDACTED}"
            }
        ],
        "page": {
            "cur": 1,
            "delta": 20,
            "endNum": 1,
            "pageCount": 1,
            "pageNum": 5
        }
    }
]
```

## 获取资源列表

POST http://abook.hep.com.cn/resourceStructure.action?courseInfoId=5000003302 HTTP/1.1

id 为首层，pId 为二层（Abook 这帮人……前面拼错 resource，后面大小写不统一，就算是驼峰也……）

```json
[{"id":5000340128,"pId":0,"name":"第一章","type":5,"haveMenu":false},{"id":5000340129,"pId":0,"name":"第二章","type":5,"haveMenu":false},{"id":5000340130,"pId":0,"name":"第三章","type":5,"haveMenu":false},{"id":5000340131,"pId":0,"name":"第四章","type":5,"haveMenu":false},{"id":5000340132,"pId":0,"name":"第五章","type":5,"haveMenu":false},{"id":5000340133,"pId":0,"name":"第六章","type":5,"haveMenu":false},{"id":5000340134,"pId":0,"name":"第七章","type":5,"haveMenu":false},{"id":5000340135,"pId":0,"name":"第八章","type":5,"haveMenu":false},{"id":5000340136,"pId":0,"name":"第九章","type":5,"haveMenu":false},{"id":5000340137,"pId":0,"name":"第十章","type":5,"haveMenu":false},{"id":5000340138,"pId":0,"name":"第十一章","type":5,"haveMenu":false},{"id":5000340139,"pId":0,"name":"第十二章","type":5,"haveMenu":false},{"id":5000340140,"pId":0,"name":"第十三章","type":5,"haveMenu":false},{"id":5000340141,"pId":0,"name":"第十四章","type":5,"haveMenu":false},{"id":5000340142,"pId":0,"name":"第十五章","type":5,"haveMenu":false},{"id":5000340143,"pId":0,"name":"第十六章","type":5,"haveMenu":false},{"id":5000340144,"pId":0,"name":"第十七章","type":5,"haveMenu":false},{"id":5000340145,"pId":0,"name":"第十八章","type":5,"haveMenu":false},{"id":5000340146,"pId":0,"name":"第十九章","type":5,"haveMenu":false},{"id":5000340150,"pId":5000340128,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340147,"pId":5000340128,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340148,"pId":5000340128,"name":"自测题","type":3,"haveMenu":false},{"id":5000340243,"pId":5000340128,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340151,"pId":5000340129,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340152,"pId":5000340129,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340154,"pId":5000340129,"name":"自测题","type":3,"haveMenu":false},{"id":5000340244,"pId":5000340129,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340155,"pId":5000340130,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340156,"pId":5000340130,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340158,"pId":5000340130,"name":"自测题","type":3,"haveMenu":false},{"id":5000340245,"pId":5000340130,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340159,"pId":5000340131,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340160,"pId":5000340131,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340162,"pId":5000340131,"name":"自测题","type":3,"haveMenu":false},{"id":5000340246,"pId":5000340131,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340163,"pId":5000340132,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340164,"pId":5000340132,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340166,"pId":5000340132,"name":"自测题","type":3,"haveMenu":false},{"id":5000340247,"pId":5000340132,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340167,"pId":5000340133,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340168,"pId":5000340133,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340170,"pId":5000340133,"name":"自测题","type":3,"haveMenu":false},{"id":5000340346,"pId":5000340133,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340171,"pId":5000340134,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340172,"pId":5000340134,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340174,"pId":5000340134,"name":"自测题","type":3,"haveMenu":false},{"id":5000340349,"pId":5000340134,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340175,"pId":5000340135,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340176,"pId":5000340135,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340178,"pId":5000340135,"name":"自测题","type":3,"haveMenu":false},{"id":5000340350,"pId":5000340135,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340179,"pId":5000340136,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340180,"pId":5000340136,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340182,"pId":5000340136,"name":"自测题","type":3,"haveMenu":false},{"id":5000340351,"pId":5000340136,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340183,"pId":5000340137,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340184,"pId":5000340137,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340186,"pId":5000340137,"name":"自测题","type":3,"haveMenu":false},{"id":5000340352,"pId":5000340137,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340187,"pId":5000340138,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340188,"pId":5000340138,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340190,"pId":5000340138,"name":"自测题","type":3,"haveMenu":false},{"id":5000340353,"pId":5000340138,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340191,"pId":5000340139,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340192,"pId":5000340139,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340194,"pId":5000340139,"name":"自测题","type":3,"haveMenu":false},{"id":5000340403,"pId":5000340139,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340195,"pId":5000340140,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340196,"pId":5000340140,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340198,"pId":5000340140,"name":"自测题","type":3,"haveMenu":false},{"id":5000340404,"pId":5000340140,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340199,"pId":5000340141,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340200,"pId":5000340141,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340202,"pId":5000340141,"name":"自测题","type":3,"haveMenu":false},{"id":5000340405,"pId":5000340141,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340203,"pId":5000340142,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340205,"pId":5000340142,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340206,"pId":5000340142,"name":"自测题","type":3,"haveMenu":false},{"id":5000340406,"pId":5000340142,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340207,"pId":5000340143,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340208,"pId":5000340143,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340210,"pId":5000340143,"name":"自测题","type":3,"haveMenu":false},{"id":5000340420,"pId":5000340143,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340211,"pId":5000340144,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340212,"pId":5000340144,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340214,"pId":5000340144,"name":"自测题","type":3,"haveMenu":false},{"id":5000340422,"pId":5000340144,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340215,"pId":5000340145,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340216,"pId":5000340145,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340218,"pId":5000340145,"name":"自测题","type":3,"haveMenu":false},{"id":5000340423,"pId":5000340145,"name":"补充章节","type":1,"haveMenu":false},{"id":5000340219,"pId":5000340146,"name":"教学课件","type":1,"haveMenu":false},{"id":5000340220,"pId":5000340146,"name":"本章小结","type":1,"haveMenu":false},{"id":5000340222,"pId":5000340146,"name":"自测题","type":3,"haveMenu":false},{"id":5000340424,"pId":5000340146,"name":"补充章节","type":1,"haveMenu":false}]
```

## 获取下载链接

POST http://abook.hep.com.cn/courseResourceList.action?courseInfoId=5000003302&treeId=5000340175&cur=1 HTTP/1.1

返回：

```json
[
    {
        "OSSURL": "http://abook1.hep.com.cn",
        "message": "加载成功",
        "myMobileResourceList": [
            {
                "downloadDeductScore": 0,
                "downloadNumber": 0,
                "mediaTypeName": "混合",
                "myresSize": "3MB",
                "picUrl": "/systemImg/builtIn/50ppt.png",
                "resAbstract": "暂无资源简介",
                "resBrowserUrl": null,
                "resFileUrl": "5000003302/resourses/2019/4/1/7a123508-0a6a-4c11-b7de-5e3ed9b04d1d.ppt",
                "resSortName": "教学PPT",
                "resTitle": "第八章 炎症",
                "resourceInfoId": 5000289307,
                "scanNumber": 4004,
                "viewer": 8
            }
        ],
        "page": {
            "cur": 1,
            "delta": 20,
            "endNum": 1,
            "pageCount": 1,
            "pageNum": 5
        },
        "returnType": 1
    }
]
```

## 下载

拼接 OSS 域名（abook1.hep.edu.cn）以及 resFileUrl，别忘了带上 icourse_SESSION，以及这里要带上 Referer ```http://*.appyun.com```