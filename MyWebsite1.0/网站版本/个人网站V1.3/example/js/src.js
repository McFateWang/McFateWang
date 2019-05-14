/*
* JS  - src.js
*/

/* 正文 */
function on_cal_click(){
	var v_cal = document.getElementById("id-input-text").value; //获取输入框的值
	var v_result = eval(v_cal);  //使用eval语句计算结果
	document.getElementById("id-div-result").innerText = "  结果：  "+ v_result;  //在div处输出结果
}

function deal_event(event){
	var v_value = event.target.value;  //该事件的值
		console.log(v_value);  //记录在log中
		if(v_value == 'c'){  //c则输入框清零 = 或者 cal 计算结果 其他则输入框依次增加
			document.getElementById("id-input-text").value = "";
			document,getElementById("id-div-result").innerText = "";
		}
		else if(v_value == '=' || v_value == 'cal'){
			on_cal_click();
		}
		else {
			document.getElementById("id-input-text").value += v_value;
		}
}

function on_btn_click(thisid){
	var btn = document.getElementById(thisid);  //获取这个标签的id
	btn.addEventListener('click',deal_event(event),false);  //事件，点击鼠标后得到v_value
}

//找到元素id，插入HTML语言
//document.getElementById("id-div-body-1").innerHTML += "<h3>using JS...</h3>" 

