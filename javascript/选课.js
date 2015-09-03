var jqueryLib=document.createElement("script");
jqueryLib.src="http://lib.sinaapp.com/js/jquery/1.8.3/jquery.min.js";
document.body.appendChild(jqueryLib);

var sCount=0,eCount=3,runHandle,$slmsg;

var cNo={
	"2010116908":false//湿地
	,"2010116906":false//湿地
	,"2010116905":false//湿地
};

function SelCor(){
	if(eCount==sCount){
		alert("全部都选了！");
		return;
	}
	for(var i in cNo){
		if(cNo[i])continue;
		$.ajax({
			"async":false,
			"url":"http://202.198.128.29:8000/webxk/XK_SELECTCOURSE.XKAPPPROCESS?Time="+Math.random()+"&XKTaskID="+i,
			"success":function(data){
				var code=data.replace(/\s/mg,"").replace(/^.*iRetFlag=(\d+?);.*$/mg,"$1");
				if(code=="1022"){//1022已经选择此课程
					sCount++;
					cNo[i]=true;
					$slmsg.append(new Date()+"!!选课失败，你能选，但是你错过了，因为已经选择此课程，课程："+i+"<br>");
				}else if(code=="1026"){//1026超出学分限制
					sCount++;
					cNo[i]=true;
					$slmsg.append(new Date()+"!!选课失败，你能选，但是你错过了，因为学分限制，课程："+i+"<br>");
				}else if(code=="1021"||code=="1022"){//1022重复选课，1031删除成功，
					sCount++;
					cNo[i]=true;
					$slmsg.append(new Date()+"##选课成功："+i+"<br>");
				}else{
					console.log(new Date()+"\t选课失败："+i+"，Code: "+code);
				}
			},
			"type":"GET",
			"error":function (XMLHttpRequest, textStatus, errorThrown) {
				console.log("网络错误，code："+textStatus);
			}
		});
	}
	runHandle=setTimeout("SelCor();",1000);//时间
}

function start(){
	if(typeof(jQuery)=='undefined'){
		console.log(new Date()+"\tjQuery 未加载。");
		return;
	}
	clearInterval(initInterval);
	jQuery("html").append("<div id='slmsg' style='position:absolute;bottom:0px;left:0px;width:100%;height:100px;background-color:#dd0;color:#d00;overflow:scroll;z-index:999;font-size:12px;'></div>");
	$slmsg=jQuery("#slmsg");
	SelCor();
}

function stop(){
	clearTimeout(runHandle);
}

var initInterval=setInterval(start,100);

