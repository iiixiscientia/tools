// ==UserScript==1
// @name         若离雨课堂助手
// @namespace    若离
// @version      3.0.1.100
// @description  若离雨课堂助手，为您完美解决雨课堂、长江雨课堂、黄河雨课堂、荷塘雨课堂的考试！
// @author       若离
// @connect      ykt.ruoli.cc
// @connect      localhost
// @match        *://*.yuketang.cn/*
// @match        *://*.xuetangx.com/*
// @icon         https://q1.qlogo.cn/g?b=qq&nk=2909998156&s=100
// @resource cs1 https://unpkg.com/element-ui/lib/theme-chalk/index.css
// @resource cs2 https://pan.ruoli.cc/E5/cdn/ruoli_rainclass.min.css
// @require      https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.min.js
// @require      https://cdn.jsdelivr.net/npm/vue/dist/vue.js
// @require      https://unpkg.com/element-ui/lib/index.js
// @require      https://cdn.bootcdn.net/ajax/libs/limonte-sweetalert2/10.16.3/sweetalert2.all.js
// @run-at       document-end
// @grant        GM_xmlhttpRequest
// @grant        GM_addStyle
// @grant        GM_getResourceText
// ==/UserScript==111
 
// 定义配置信息 对象
let config = {
    'baseUrl': 'ykt.ruoli.cc',
    'logs': ['当前脚本版本：V3.0', '初始化脚本界面完成'],
    'datas': []
}
 
// 定义日志 方法
let log = (obj)=>{
    config.logs.unshift(obj);
}
 
// 定义界面初始化 方法
let initView = ()=>{
    let $rl_div = $(`
        <div id="rlBox">
			<el-card class="box-card">
				<el-row>
				  <el-col :span="24"><div class="center"><b style="color: #E6A23C; font-size: 20px;">若离雨课堂助手</b></div></el-col>
				</el-row>
				<el-divider></el-divider>
				<el-row>
					<a href ="https://pay.ruoli.cc/" target="_blank"><el-button type="primary" plain size="mini">我要赞助</el-button></a> 
                    <el-button type="warning" id="rl_searchAnswer" plain size="mini">搜索答案</el-button>
					<a href ="https://jq.qq.com/?_wv=1027&k=6NEZkACS" target="_blank"><el-button type="success" plain size="mini">加入群聊</el-button></a>
				</el-row>
				<el-divider></el-divider>
				<el-row class = "log_list">
					<el-col :span="3"><span class="gray small">日志</span></el-col>
					<el-col :span="21">
						<el-row class = "log_list">
							<el-col :span="24">
								<div class="gray small" v-for="log in logs">{{ log }}</div>
							</el-col>
						</el-row>
					</el-col>
				</el-row>
				<el-divider></el-divider>
			  <template>
			    <el-table
			      :data="tableData"
			      border
                  empty-Text = "脚本交流群：1124936860"
				  size="mini"
			      style="width: 100%">
			      <el-table-column
			        prop="id"
			        label="题号"
			        width="48"
					align="center">
			      </el-table-column>
			      <el-table-column
			        prop="answer"
			        label="答案"
			        width="120">
			      </el-table-column>
			      <el-table-column
			        prop="options"
			        label="选项">
			      </el-table-column>
			    </el-table>
			  </template>
			</el-card>
		</div>
    `);
    $("body").append($rl_div);
    GM_addStyle(GM_getResourceText("cs1"));
    GM_addStyle(GM_getResourceText("cs2"));
    let vue = new Vue({
        el: '#rlBox',
			data:{
				logs: config.logs,
				tableData: config.datas
			},
    })
}
 
let searchAnswer = ()=>{
    let pageUrl = location.href;
    //如果是旧版本的考试界面
    if(pageUrl.match(/studentQuiz\/(.*?)\//) !== null){
        let examId = pageUrl.match(/studentQuiz\/(.*?)\//)[1];
        let examType = 4;
        let host = pageUrl.match(/\:\/\/(.*?)\./)[1];
        log('正在为您获取答案中...');
        setTimeout(oldRainAnswer,3500,examId,examType,host);
    }else if (pageUrl.match(/exam\/(.*?)\?isFrom/) !== null){
        let examId = pageUrl.match(/exam\/(.*?)\?isFrom/)[1];
        let examType = 5;
        let host = pageUrl.match(/\:\/\/(.*?)\./)[1];
        host = host == 'examination'? 'www': host;
        host = host.replace("-exam", "");
        log('正在为您获取答案中...');
        setTimeout(getWebPage,3500,examId,examType,host);
    }else{
        log('还未匹配过当前页面');
        log('如果您确保这是考试页面请反馈哦');
    }
}
let getWebPage = (examId,examType,host)=>{
    let webUrl = location.origin + '/exam_room/show_paper?exam_id=' + examId;
     GM_xmlhttpRequest({
        method: "get",
        url: webUrl,
        headers: {
             'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        },
        onload: function(res){
            if(res .status == 200){
                let obj = $.parseJSON(res.responseText);
                let questionList = obj.data.problems
                newRainAnswer(examId, examType, host, questionList);
            }else{
                log('服务器异常，请检查更新脚本或联系作者')
            }
        }
    });
}
let newRainAnswer = (examId,examType,host,questionList)=>{
    GM_xmlhttpRequest({
        method: "post",
        url: 'http://'+config.baseUrl + '/new/pro/'+examId+'/'+examType+'/'+host,
        data: JSON.stringify(questionList),
        headers: {
             'Content-type': 'application/json; charset=utf-8',
        },
        onload: function(res){
            if(res .status == 200){
                let obj = $.parseJSON(res.responseText);
                if(obj.status == 200){
                    obj.data.forEach((item)=>{
                        config.datas.push(item);
                    })
                    log('答案获取完成');
                }else{
                    log(obj.message)
                }
            }else{
                log('服务器异常，请检查更新脚本或联系作者')
            }
        }
    });
}
 
let oldRainAnswer = (examId,examType,host)=>{
    GM_xmlhttpRequest({
        method: "post",
        url: 'http://'+config.baseUrl + '/old/pro/'+examId+'/'+examType+'/'+host,
        headers: {
             'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        },
        onload: function(res){
            if(res .status == 200){
                let obj = $.parseJSON(res.responseText);
                if(obj.status == 200){
                    obj.data.forEach((item)=>{
                        config.datas.push(item);
                    })
                    log('答案获取完成');
                }else{
                    log(obj.message)
                }
            }else{
                log('服务器异常，请检查更新脚本或联系作者')
            }
        }
    });
 
}
// 定义脚本入口
let main= ()=>{
    let pageUrl = location.href;
    if(pageUrl.match('answer/quiz') !== null){
    }else if(pageUrl.match('quiz/quiz_result') !== null || pageUrl.match('/quiz/quiz_info/') != null){
    }else{
        initView();
        $('#rl_searchAnswer').click(()=>{
            searchAnswer();
        })
    }
}
main();
