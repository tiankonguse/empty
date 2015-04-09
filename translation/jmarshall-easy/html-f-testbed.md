# HTML 测试基地(iframe版本)

输入一些 HTML 代码， 点击运行。你将会在下面的 frame 中看到运行效果。  

<form>
<textarea id="htmlcode" rows="20" cols="51">&lt;html&gt;
&lt;head&gt;
&lt;title&gt;&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;!-- Put the body of your page below this line --&gt;
hello, tiankonguse!
&lt;!-- Put the body of your page above this line --&gt;
&lt;/body&gt;
&lt;/html&gt;
</textarea> <br/>
<input type="button" id="htmlrun" value="运行">
<input type="reset" value="重新开始">
</form>
<div id="wrapIframe">
</div>
<script src="http://github.tiankonguse.com/javascripts/jquery-1.7.1.min.min.js" type="text/javascript"></script>
<script>
$(document).ready(function() {
    var strFrame = '<iframe src="javascript:parent.onloadIframe;" height="50%" width="100%"></iframe>';
    $("#htmlrun").bind("click", function(){
        window.onloadIframe = $("#htmlcode").val(); 
        $("#wrapIframe").html(strFrame);
    }).click();
});
</script>

