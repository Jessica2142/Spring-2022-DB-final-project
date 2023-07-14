num=0
y=[]

#在url里key后面的******换为高德开放平台自己申请的key

with open("NJ_sight.csv", 'r') as f: #写入将要转换的地址的文件路径,此处为默认文件路径（要先将文件提前导入）（注意是csv格式文件）
        r = csv.reader(f, delimiter=',')
        for row in r:
            #print(row[0])
            add = row[1] + '入口'
            url = "http://restapi.amap.com/v3/geocode/geo?key=cc0a4408de88eabb7cfb45534964afde&address=" + add
            dat = {
                'count': "1",
                }
            r = requests.post(url, data=json.dumps(dat))
            s = r.json()
            try:
                b = s['geocodes']
                text = str(b)
                #print(text)
            except:
                text = 'none'
            

            # 经纬度
            try:
                pat4 = "'location': '(.*?)',"
                res3 = re.compile(pat4).findall(text)[0]
                # print(res3)
                lon_lat = res3.split(',')
                lon = float(lon_lat[0])
                lat = float(lon_lat[1])
                #print("经度：",lon)
                #print("纬度：",lat)
            except:
                lon = 'none'
                lat = 'none'
                #print("经度：",lon)
                #print("纬度：",lat)

            num += 1
            #print("第" + str(num) + "条地址转换成功")
            #print('**************************************')
            y.append([num, add, lon, lat])
        result = pd.DataFrame(y)
        result.columns = ['id', 'address', 'lon', 'lat']
        result.to_csv('result.csv', encoding='utf-8-sig', index=False)
        print("全部地址转换成功")
