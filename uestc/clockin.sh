# source from https://gist.github.com/SteveCharlesYang/f158963413666f3ae0ff1006f5abf78a

COOKIE=`cat cookie.txt`
TIMEARRAY=("%E6%97%A9%E4%B8%8A" "%E4%B8%AD%E5%8D%88" "%E6%99%9A%E4%B8%8A")

STUID="202021140209"
STUNAME="张津馗"

DPTID="1008"
DPTNAME="生命科学与技术"

doCURL(){
    curl -s 'http://eportal.uestc.edu.cn/jkdkapp/sys/lwReportEpidemicStu/modules/tempReport/T_REPORT_TEMPERATURE_YJS_SAVE.do' \
    -H 'Connection: keep-alive' \
    -H 'Pragma: no-cache' \
    -H 'Cache-Control: no-cache' \
    -H 'Accept: application/json, text/javascript, */*; q=0.01' \
    -H 'DNT: 1' \
    -H 'X-Requested-With: XMLHttpRequest' \
    -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4292.2 Safari/537.36' \
    -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
    -H 'Origin: http://eportal.uestc.edu.cn' \
    -H 'Referer: http://eportal.uestc.edu.cn/jkdkapp/sys/lwReportEpidemicStu/index.do' \
    -H 'Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7' \
    -H $"${COOKIE}" \
    --data-raw "WID=&CZZ=&CZZXM=&CZRQ=&USER_ID=$STUID&USER_NAME=$STUNAME&DEPT_CODE=$DPTID&DEPT_NAME=$DPTNAME&NEED_DATE=2020-$1-$2&DAY_TIME_DISPLAY=${TIMEARRAY[$3]}&DAY_TIME=$3&TEMPERATURE=36.5&CREATED_AT=2020-$1-$2+00%3A00" \
    --compressed \
    --insecure \
    > /dev/null
}

for i in $(seq 11 12)  
do   
    for j in $(seq 1 30)  
    do   
        for k in $(seq 1 3)  
        do   
            echo "Do for $i-$j $k"
            doCURL $i $j $k
            sleep 0.5
        done   
    done   
done