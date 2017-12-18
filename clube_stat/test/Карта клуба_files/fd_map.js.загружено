$(document).ready(function(){
	map_update();
})

jQuery(function($){
	

		
	
	
	$(".comp").live('mouseenter',function(){
		if($(this).attr("title")!=""){
			var txt=$(this).attr("title");
			$(this).append("<div class='map_desc'>"+txt+"</div>");
			$(this).attr("title","");	
		}
	})
	
	$(".comp").live('mouseleave',function(){
		if($(this).children(".map_desc").length>0){
			$(this).attr("title",$(this).children(".map_desc").html());
			$(this).children(".map_desc").remove();	
		}
	})
	$(".map_desc").live("mouseenter",function(){
		$(this).parent().attr("title",$(this).html());
		$(this).remove();
	})
	
	$(".select_all").live('click',function(){
		if($(this).find("span").text()=="Выбрать все"){
			$(this).find("span").text("Снять выбор");
			
			$(".comp").each(function(){
				$(this).addClass("selected");
			})
		}else {
			$(this).find("span").text("Выбрать все");
			$(".comp").each(function(){
				$(this).removeClass("selected");
			})
		}	
	})
	$(".comp").live("click",function(e) {
		var el=$(this);
		altPressed  =e.altKey;
		if(altPressed){
			if($(el).hasClass("selected"))$(el).removeClass("selected");
			else $(el).addClass("selected");
		}
		ctrlPressed = e.ctrlKey;
		if(ctrlPressed){
			var k=0;
			var act=1;
			$(el).parent().parent().find(".comp").each(function(){
				k++;
				if(k==1){
					if($(this).hasClass("selected")){
						act=1;
					}else {
						act=0;
					}	
				}
				if(act==1){
					$(this).removeClass("selected");
				}else {
					$(this).addClass("selected");
				}
			})
			
		}	
	})
	
	
	var map_up=setInterval("map_update()",10000);
	
	$(".comp").live("contextmenu",function(e) {
		
		$(".selected_pc").removeClass("selected_pc");
		$("#submenu").remove();
		$(".startuser").fadeOut('fast',function(){
			$(this).remove();
		});
    	e.preventDefault(); //ПРЯЧЕМ ИСХОДНОЕ МЕНЮ
		var x=e.pageX;
		var y=e.pageY;
		var id=$(this).attr("id");
		id=id.replace("pc","");
		$(this).addClass("selected");
		
		$.post(base_url+"map/get_tech", {}, function(data){
			var adt="<em class='subtech'>"+data+"</em>";
			var str = "";
			str = "<div style='width: 250px;' id='submenu' alt='"+id+"'><a class='power_on'>Включить рабочую станцию</a>";
			if($("#allowtechuser").length>0){
				str+="<a class='run_tech_user'>Запустить тех. пользователя"+adt+"</a>";
			}
			str+="<a class='power_off'>Выключить рабочую станцию</a><a class='restart'>Перезагрузить рабочую станцию</a><a class='user_warning'>Послать предупреждение пользователю</a><a class='cancel'>Отменить последние команды</a><a class='run_with_user'>Запустить от имени пользователя</a><input type='text' class='mysub'/></div>";
			$("body").append(str);
			$("#submenu").css({"left": x+10, "top": y+10});
			$("#submenu").fadeIn("50");
			$(".mysub").focus();
		})
	})
	
	
	$(".run_tech_user").live("mouseenter",function(){
		$(".subtech").fadeIn(20);
	})
	$(".subtech").live("mouseleave",function(){
		$(".subtech").fadeOut(20);
	})
	$(".run_with_user").live("mouseenter",function(){
			$(".subtech").fadeOut(20);
	})
	$(".power_off").live("mouseenter",function(){
			$(".subtech").fadeOut(20);
	})
	
	$(".mysub").live("blur",function(){
		$("#submenu").fadeOut('fast',function(){$(".selected").removeClass("selected");$(this).remove();$(".toselect").addClass("selected").removeClass("toselect");});
	})
	
	$(".start_tech").live("click",function(){
		var el=$(this);
		var str='';
		var cl=el.attr("class");
		cl=cl.replace("start_tech ","");
		cl=parseInt(cl);
		var id=$(this).parent().attr("alt");
		$(".selected").each(function(){
			//ВЫБИРАЕМ ВСЕ ОТМЕЧЕННЫЕ РС
			var id=$(this).attr("id");
			id=id.replace("pc","");
			if(str!="")str+=",";
			str+=id;
		})
		$(".selected").each(function(){
			var id=$(this).attr("id");
			id=id.replace("pc","");
			var el = $(this);
			$.ajax({
				url: base_url+"map/start_tech",
				data: "str="+id+"&user="+cl,
				async: false,
				type:"POST",
				success:function(data){
						if(data==1){
							//$(".selected").each(function(){
								//var id=$(this).attr("id");
							//	id=id.replace("pc","");
								el.append("<div class='map_ok' id='map_ok"+id+"'></div>");
								$("#map_ok"+id).fadeIn('fast').delay(1000).fadeOut('fast',function(){$(this).remove();});	
							//});
							
						}
						else {
							//$(".selected").each(function(){
							//	var id=$(this).attr("id");
							//	id=id.replace("pc","");
								el.append("<div class='map_bad' id='map_bad"+id+"'></div>");
								$("#map_bad"+id).fadeIn('fast').delay(1000).fadeOut('fast',function(){$(this).remove();});	
							//})
						}
				}
			})
		})
	})
	
	$("#submenu a").live('click',function(){
		if($(this).hasClass("start_tech"))return false;
		var act=$(this).attr("className");
		var str="";
		var el=$(this);
		$(".selected").each(function(){
			//ВЫБИРАЕМ ВСЕ ОТМЕЧЕННЫЕ РС
			var id=$(this).attr("id");
			id=id.replace("pc","");
			if(str!="")str+=",";
			str+=id;
		})
		
		var id=$(this).parent().attr("alt");
		if(act!="run_with_user"){
			var string = "";
			if(act=="user_warning"){
				string=prompt("Введите текст предупреждения");	
				string=$.trim(string);
				while(string==""){
					string=prompt("Введите текст предупреждения");	
				}
			}
			$(".selected").each(function(){
				var el = $(this);
				var id=$(this).attr("id");
				id=id.replace("pc","");
				$.post(base_url+"map/command", {comp: id, action: act,new_str:string}, function(data){
					if(data==1){

							//var id=$(this).attr("id");
							//id=id.replace("pc","");
							el.append("<div class='map_ok' id='map_ok"+id+"'></div>");
							$("#map_ok"+id).fadeIn('fast').delay(1000).fadeOut('fast',function(){$(this).remove();});	
		
						
					}
					else {
						//$(".selected").each(function(){
							//var id=$(this).attr("id");
							//id=id.replace("pc","");
							el.append("<div class='map_bad' id='map_bad"+id+"'></div>");
							$("#map_bad"+id).fadeIn('fast').delay(1000).fadeOut('fast',function(){$(this).remove();});	
						//})
					}
				})
			})
		}else {
			var id = $(el).parent().attr("alt");
			$("#pc"+id).addClass("selected");

			var x=$(el).parent().position().left;
			var y=$(el).parent().position().top;
			$(el).parent().after("<div class='startuser' style='top: "+y+"px; left: "+x+"px;'><input type='hidden' class='id' value='"+id+"'/><input type='text' class='ulog' value='login' alt='login'/><br/><input type='password' class='upass' value=''/><br/><button type='button' class='make'>Выполнить</button><button class='cancel'>Отмена</button>");
			$("#pc"+id).addClass("toselect");
		}
		$(".select_all").find("span").text("Выбрать все");
	})
	$(".startuser .cancel").live("click",function(){
		$(".startuser").fadeOut("fast",function(){
			$(this).remove();
		})
		$(".selected").removeClass("selected");
	})
	$(".startuser .make").live("click",function(){
		var id=$(".startuser").find(".id").val();
		var login=$(".startuser").find(".ulog").val();
		var pass=$(".startuser").find(".upass").val();
		if(login!="" && pass!=""){
			$.ajax({
				url: base_url+"map/run_user",
				data: "id="+id+"&login="+login+"&pass="+pass,
				async: false,
				type: "POST",
				success: function(data){
					if(data==1){
						$(".selected").each(function(){
							var id=$(this).attr("id");
							id=id.replace("pc","");
							$(this).append("<div class='map_ok' id='map_ok"+id+"'></div>");
							$("#map_ok"+id).fadeIn('fast').delay(1000).fadeOut('fast',function(){$(this).remove();});	
						});
						
					}
					else {
						$(".selected").each(function(){
							var id=$(this).attr("id");
							id=id.replace("pc","");
							$("#pc"+id).append("<div class='map_bad' id='map_bad"+id+"'></div>");
							$("#map_bad"+id).fadeIn('fast').delay(1000).fadeOut('fast',function(){$(this).remove();});	
						})
					}
				}	
			})
		}
		$(".startuser").fadeOut("fast",function(){
			$(this).remove();
		})
		$(".selected").removeClass("selected");
	})
	
	$("#club_id").live("change", function(r){
		var val = $(this).val();
		$.ajax({
			url: base_url+"map/change_club_id",
			data: "value="+val,
			async: false,
			type: "POST",
			success: function(act){
					$("#club_id_input").val(val);
					if(act==1){
						$("#auto_shut").html("<strong style='color: #090;'>Автовыключение включено</strong>");
						$("#auto_shut_button").text("Отключить");
						$("#auto_val").val(0);
						
					}else {
						$("#auto_shut").html("<strong style='color: #900;'>Автовыключение отключено</strong>");	
						$("#auto_shut_button").text("Включить");
						$("#auto_val").val(1);
					}	
					map_update();
			}
		})
	})
	
	$("#map td").live("click",function(){		/*КОНСТРУКТОР КАРТЫ*/
		if(!$(".move_sign").hasClass("active")){
			if(!$(this).find("span").hasClass("selected")){
				$("#map td.active").removeClass("active");
				$(this).addClass("active");
				if($(this).text()==""){
					var t = "";	
				}else var t = parseInt($(this).text());
				var comp_num = t;			//ЕСЛИ УКАЗАНО - НОМЕР ПК
				var comp_ip = $(this).find("span").data("ip");			//ЕСЛИ УКАЗАНО - IP ПК
				var comp_mac = $(this).find("span").data("mac");			//ЕСЛИ УКАЗАНО - IP ПК
				var coord_top = $(this).offset().top + $(this).height();
				var coord_left = $(this).offset().left;
				var unauth = $(this).find("span").data("unauth");
				console.log(comp_num);
				console.log("unauth: " + unauth);
				if(comp_num==""){
					$(".fd_del_pc, .fd_move_pc").css({"display":'none'});
				}else {
					$(".fd_del_pc, .fd_move_pc").css({"display":'inline-block'});
				}

				if (unauth) {
					$(".nstq_authorize").css({"display": "inline-block"});
					$(".nstq_reject").css({"display": "inline-block"});
				}
				else {
					$(".nstq_authorize").css({"display": "none"});
					$(".nstq_reject").css({"display": "none"});
				}
				
				$("#add_pc").fadeOut("fast",function(){
					$(this).css({"left": coord_left, "top": coord_top}).fadeIn("fast");
					$("[name=pc_num]").val(comp_num);
					$("[name=pc_mac]").val(comp_mac);
					$("[name=pc_ip]").val(comp_ip);
				})
			}
		}else {
			if($(this).find("span").length==0){
				var lft = $(this).index();
				var top = $(this).parent().index();
				var id = $(".move_sign").data("id");
				var office_id = $("#club_id").val();
				$.ajax({
					type: "POST",
					url: base_url+"map/move_pc",
					async: true,
					data: {"id": id, "office_id": office_id, "left": lft, "top": top},
					success: function(data){
						if(data==1){
							$(".move_sign").removeClass('active');
							$(".move_sign").fadeOut("fast");
							$("#map td.active").removeClass("active");	
							map_update();
						}else alert(data);
					}
				})		
			}
		}
	})
	
	$(".fd_move_pc").live("click",function(){
		var id=0;
		id = $("#map td.active").find("span").data("id");
		$("#add_pc").fadeOut("fast");
		$('.move_sign').addClass('active');
		$(".move_sign").data({"id":id});
		$(".move_sign").fadeIn('fast');		
	})
	
	$(".fd_cancel_move_pc").live("click",function(){
		$('.move_sign').removeClass('active');
		$(".move_sign").fadeOut('fast');	
		$("#map td.active").removeClass("active");	
	})
	
	$(".fd_cancel_add_pc").live("click",function(){		//ЗАКРЫТИЕ ОКНА ДОБАВЛЕНИЯ ПК
		$("#add_pc").fadeOut("fast");
		$("#map td.active").removeClass("active");
	})
	
	$(".fd_del_pc").live("click",function(){
		var id=0;
		id = $("#map td.active").find("span").data("id");
		var office_id = $("#club_id").val();
		if(id!=0){
			$.ajax({
				type: "POST",
				url: base_url+"map/del_pc",
				async: true,
				data: {"id": id, "office_id": office_id},
				success: function(data){
					if(data==1){
					$("#add_pc").fadeOut("fast");
					$("#map td.active").removeClass("active");	
					map_update();
					}else alert(data);
				}
			})	
		}else {
			$("#add_pc").fadeOut("fast");
			$("#map td.active").removeClass("active");	
			map_update();
		}
	});

	$(".nstq_authorize").live("click", {authorize: true}, authorize);
	$(".nstq_reject").live("click", {authorize: false}, authorize);

	function authorize(event) {
		var mac = $("[name=pc_mac]").val();

		var action = event.data.authorize ? "map/authorize_pc" : "map/reject_pc";

		$.ajax({
			type: "POST",
			url: base_url + action,
			async: true,
			data: {"mac": mac},
			success: function(data){
				if(data==1){
					$("#add_pc").fadeOut("fast");
					$("#map td.active").removeClass("active");
					map_update();
				}else alert(data);
			}
		})
	}


	$(".fd_add_pc").live("click",function(){				//ОТПРАВКА ЗАПРОСА НА ДОБАВЛЕНИЕ ПК
		var lft = $("#map td.active").index();
		var top = $("#map td.active").parent().index();  
		var ip = $("[name=pc_ip]").val();
		var num = $("[name=pc_num]").val();
		var mac = $("[name=pc_mac]").val();
		var office_id = $("#club_id").val();
		var id = 0;
		if($("#map td.active span").length>0){		//РЕДАКТИРОВАНИЕ
			id = $("#map td.active").find("span").data("id");
		}
		
		$.ajax({
			type: "POST",
			url: base_url+"map/add_pc_v2",
			async: true,
			data: {"left": lft, "top": top, "ip": ip, "mac": mac, "num": num, "id": id, "office_id": office_id},
			success: function(data){
				if(data==1){
					$("#add_pc").fadeOut("fast");
					$("#map td.active").removeClass("active");
					map_update();
				}else {
					$("#add_pc").find("div").append("<div class='warning'>"+data+"</div>");
						$(".warning").fadeIn("fast", function(){
							$(this).delay(3000).fadeOut('fast',function(){
							$(this).remove();	
						})
					})
				}
			},
			error: function(data) {
				$("#add_pc").find("div").append("<div class='warning'>" + data.responseText + "</div>");
				$(".warning").fadeIn("fast", function(){
					$(this).delay(3000).fadeOut('fast',function(){
						$(this).remove();
					})
				})
			}
		})
	})
	
})

//СКРИПТ ОБНОВЛЕНИЯ ИНФОРМАЦИИ О КЛУБЕ
function map_update(){
	if($("#map td.active").length==0 && $(".comp.selected").length==0){
		$.ajax({
			url: base_url+"map/render_map",
			async: true,
			data: {"update": 1},
			type: "POST",
			success: function(response){
				$("#map").html(response);
				$.ajax({
					url: base_url+"map/get_stats",
					async: true,
					type: "POST",
					data: {"update": 1},
					success: function(response1){
						$("#stats").html(response1)
						
						/*$.ajax({
							url: base_url+"map/update_price",
							type: "POST",
							data:"",
							success: function(r){
								show(r);
							}
						})*/
						
					}
				})
			}	
		})
	}
}