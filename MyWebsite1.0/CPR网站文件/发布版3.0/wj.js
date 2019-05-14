//V2.0版本 核心JS 文件

jQuery(document).ready(function($){
	//点击菜单外任何区域隐藏菜单
	$("#wj-nav-dropdown").click(function(e){
		//阻止事件冒泡-如果不使用，子元素的click事件冒泡，菜单将永远hide
	  	e.stopPropagation(); 
		$("#my-navbar").toggle();//每次单击-切换navbar的状态
		//当下拉菜单处于打开状态时，任何点击事件都将使其闭合
	  	if($("#my-navbar").is(":visible")){
	       $(document).one("click",function(){
	       	$("#my-navbar").hide();
	       });
		}
	});
	//返回顶部按钮实现  
    $('#wj-backtoTop').click(
    	function(){
    	$('html,body').animate({scrollTop: '0px'}, 800);
    	}
    ); 
    //标签页切换之后事件shown，实现瞬间到页面顶部
	$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
		window.scrollTo('0','0');
	});
});