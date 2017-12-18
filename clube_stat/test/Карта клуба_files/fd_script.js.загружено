
$(document).ready(function(){
	$(".date").datepicker({ dateFormat: 'yy-mm-dd' });    	
	//ДОБАВИТЬ ЛИНИЮ
	$(".moreline").live("click",function(){
		el=$(this).closest(".add_field");
		num=$(el).attr("alt");
		el2=$(el).clone();
		$(el).after($(el2));
		num++;
		$(el2).css({display: "none"});
		$(el2).attr("alt",num);
		$(el2).find("input, select").each(function(){
			$(this).val($(this).attr("alt"));
			nm=$(this).attr("title");
			$(this).attr("name",nm+num);
		});
		$(el2).slideDown("fast");
		$(this).fadeOut(100,function(){
			$(this).after("<button type='button' class='minline'></button>");
			$(this).remove();	
		});
	})
	$(".minline").live("click",function(){
		el=$(this).closest(".add_field");
		$(el).slideUp("fast",function(){$(this).remove();});
	})
    
	if($("#fd_school_list_page").length == 1){
		$(".fd_user_nchecked").live("click", function(){
			var el = $(this);
			var user_id = el.attr('alt');
			$.ajax({
				url: base_url+"users/setSchool",
				data: "user_id="+user_id,
				type: "POST",
				success: function(r){
					el.attr("disabled", "disabled");	
				}
			})
		})
	}
	
	//ПРИВЯЗКА КЛЮЧА К ЮЗЕРУ
	$("#user_nick").live("keyup",function(){
		var word=$(this).val();
		if($.trim(word)!="" && word!="Ник или E-mail"){
			if(word.length>1){
			
				$.post(base_url+"content/get_users", {searchword: word}, function(data){
					if($("#user_hint").html()!=data){
						$("#user_hint").html(data);	
						$("#user_hint").fadeIn('fast');
					}else {
				$("#user_hint").html("").fadeOut('fast');	
			}
				});
			}else {
				$("#user_hint").html("").fadeOut('fast');	
			}
		}
		else {$("#user_hint").html("").fadeOut('fast');}
	})
	
	$(".addusertolist").live('click', function(){
		var text=$(this).text();
		var id=$(this).attr('alt');
		$("#user_id").val(id);
		$("#user_nick").val(text);
		$("#user_hint").html("").fadeOut('fast');	
	})
	
})

jQuery(function($){
	
	$("#fd_search_btn").live("click",function(){
		var val=$.trim($("#fd_srch_word").val());
		if(val != ''){
			$.ajax({
				url: base_url+"rights/search_user",
				data: "n="+val,
				async: false,
				type: "POST",
				success: function(r){
					$("#fd_result").html(r+'<button class="but_1" id="add_to_group" type="submit" name="sbmt">добавить</button>');
				}
			})	
		}
	})
	
	$("#add_to_group").live("click", function(){
		var user_id=$("[name='fd_user']").val();
		if(user_id!=0){
			var group_id=$("#fd_id_group").val();
			$.ajax({
				url: base_url+"rights/add_user_to_group",
				data: "gr_id="+group_id+"&user_id="+user_id,
				async: false,
				type: "POST",
				success:function(r){
					if(r!=0){
						window.location.href=window.location.href;	
					}else alert("error, user exists");
				}
			})	
		}else alert("Выберите пользователя со списка!");
	})
	
	$(".restore_but").live("click", function(e){
		e.preventDefault();
		var el = $(this);
		var id = el.attr("rel");
		$.ajax({
			url: base_url+"restore/restore_pass",
			data: "user_id="+id,
			type: "POST",
			async: false,
			success: function(r){
				if(r==1){
					alert("Пароль успешно обновлен!");	
				}
			}	
		})	
	})
	
	$("[rel='no_reload']").live("click", function(e){
		e.preventDefault();
		var el= $(this);
		var link_ = $(this).attr("href");
		alert(link_);
		return false;
	})
	
	$("#add_genre").live("click", function(){
		var str="<tr class='string string_genre'>";
		var el = $(".string_genre:first").html();
		str+=el;
		str+="</tr>";
		str+="<tr><td height='10'></td></tr>";
		$("#last_row").before(str);
		$(".string_genre:last").find("select").val(0);
	})
	
	$("#add_tag").live("click", function(){
		var str="<tr class='string tag_string'>";
		var el = $(".tag_string:first").html();
		str+=el;
		str+="</tr>";
		str+="<tr><td height='10'></td></tr>";
		$("#last_row_tag").before(str);
		$(".tag_string:last").find("select").val(0);
	})
	
	$(".del_row_genre").live("click",function(){
		if( $(this).closest("tr").hasClass("string_genre"))var cl = "string_genre";
		else var cl = "tag_string";
		var tot = $("."+cl).length;
		if(tot>1){
			$(this).closest("tr").remove();
		}
	})
	
	$(".fd_permission").live("click",function(){
		var el=$(this);
		var perm_id=el.attr("alt");
		if(!$(this).attr("checked") ){
			act="delete_role_privilege"
			el.removeClass('fd_active');
		}else{
			act = "add_role_privilege";
			el.addClass('fd_active');
		}
		$.ajax({
			url: base_url+"rights/"+act,
			data:"priv_id="+perm_id+"&role_id="+$("#fd_role_id").val(),
			async: false,
			type: "POST",
			success: function(data){
				
			}	
		})
	})
	
	
	
	
	$(".fd_add_group_role").live("click",function(){
		var el=$(this);
		var perm_id=el.attr("alt");
		if(el.hasClass("active")){
			act="delete_group_role"
			el.removeClass('active');
		}else{
			act = "add_group_role";
			el.addClass('active');
		}
		$.ajax({
			url: base_url+"rights/"+act,
			data:"role_id="+perm_id+"&group_id="+$("#fd_id_group").val(),
			async: false,
			type: "POST",
			success: function(data){
				
			}	
		})
	})
	
	$("#change_role_name").live('click',function(){
		var el=$(this);
		var data=el.text();
		el.replaceWith("<input id='fd_new_role_name' title='Введите новое название' type='text' name='fd_new_name' value='"+data+"' style='border: 2px solid #666;' />"); 
		$("#fd_new_role_name").focus();
	})
	
	$("#fd_new_role_name").live("blur", function(){
		var el = $(this);
		var value=el.val();
		if($.trim(value)=="")return false;
		var role_id=$("#fd_role_id").val();
		$.ajax({
			url: base_url+"rights/change_role_nm",
			data: "role_id="+role_id+"&new_name="+value,
			async: false,
			type: "POST",
			success: function(r){
				$("#fd_new_role_name").replaceWith('<a id="change_role_name">'+value+'</a>');
			}
		})	
	})
	
	$("#change_group_name").live('click',function(){
		var el=$(this);
		var data=el.text();
		el.replaceWith("<input id='fd_new_group_name' title='Введите новое название' type='text' name='fd_new_name' value='"+data+"' style='border: 2px solid #666;' />"); 
		$("#fd_new_group_name").focus();
	})
	
	$("#fd_new_group_name").live("blur", function(){
		var el = $(this);
		var value=el.val();
		if($.trim(value)=="")return false;
		var group_id=$("#fd_id_group").val();
		$.ajax({
			url: base_url+"rights/change_gr_nm",
			data: "group_id="+group_id+"&new_name="+value,
			async: false,
			type: "POST",
			success: function(r){
				$("#fd_new_group_name").replaceWith('<a id="change_group_name">'+value+'</a>');
			}
		})	
	})
	
	$("#fd_adduser").live("click",function(e){
		var error=0;
		
		if(jQuery.trim($("#fd_userpass").val())==jQuery.trim($("#fd_userpassconf").val())){
			error=0;	
		}else error = 2;
		
		$("[alt='req']").each(function(index, element) {
			if(jQuery.trim($(this).val())==""){
				error=1;
				$(this).css({"border":"solid 1px #ff6600"});
			}else{
				$(this).css({"border":"none"});	
			}
		});	
		if(error==1){
			e.preventDefault();	
			alert("Не все обязательные поля заполнены");
		}
		if(error==2){
			e.preventDefault();	
			alert("Пароли не совпадают");
		}
	})
	
	$("#fd_add_content").live("click",function(e){
		var error=0;
		var error_str = "";
		$("[alt='req']").each(function(index, element) {
			var val = $(this).val();
			
			if($(this).is("textarea") && val==""){
				val = tinyMCE.get($(this).attr("id")).getContent();	
			}
			if(jQuery.trim(val)==""){
				error=1;
				error_str+=$(this).attr("name")+",";
				$(this).css({"border":"solid 1px #ff6600"});
			}else{
				$(this).css({"border":"none"});	
			}
		});	
		if(error==1){
			alert("Не все поля заполнены ("+error_str+")");
			e.preventDefault();	
		}
	})
	
	$("#fd_enter").live("click",function(e){
		e.preventDefault();	
		var el=$(this);
		var login_data = new Object({
			"login":$("#enter_login").val(),
			"password":$("#enter_password").val()
		})
		$.ajax({
			url: base_url+"main/auth_v2",
			data: login_data,
			async: false,
			type: "POST",
			success: function(data){
				if(data!=0){
					window.location.href=base_url+"map";
				}else{
					make_error("Неверная пара логин/пароль",$(".input_m").last(),0);
				}
			}	
		})
	});

	$('.redirect_new_admin').live('click', redirect_new_admin);
	
	//ЧИСЛЕННЫЕ ПОЛЯ
	$(".numeric").live("keypress", function (e) {
	
	  if((e.which > 57 || e.which < 48 && e.which != 8 && e.which != 0 || e.keyCode == 45) && e.which!=44)
	  return false; 
	});
	
	//ВСПЛЫВАЮЩИЕ ПОДСКАЗКИ
	$('a, button, .fd_tool').tooltip({ 
   		 track: true, 
   		 delay: 0, 
   		 showURL: false, 
   		 showBody: " - ", 
  		 fade: 250 
		});
	
	//УДАЛЕНИЕ ЗАПИСЕЙ
	$(".del_but").live('click',function(e){
		var art=$(this).text();
		id=$(this).val();
		var name=$("#str_"+id).find("a").text();
		if($("#tempform").attr("id")!=null)$("#tempform").remove();
		$("body").append("<form method='post' id='tempform'><input type='hidden' id='fd_idtodel' value='"+id+"'/><input type='hidden' id='fd_strtodel' name='strtodel' value='"+base_url+art+id+"'/></form>");
		form=$("#tempform");
		str="Вы уверены, что хотите удалить из списка запись <br/><span style='color: #f00;'>"+name+"</span>";
		make_notification(form,str);
		e.preventDefault();
	})
	
	$("#tempform").live("submit",function(){
		
		str=$("#fd_strtodel").val();
		$.post(str,{"true": 1},function(data){

			if(data=="1"){
			id=$("#fd_idtodel").val();
			$("#str_"+id).fadeOut(200,function(){
				$(this).remove();	
			})
			}
			else {
				if(data==5)window.location.href = window.location.href;
				if(data==2)alert("Действие не может быть выполнено, так как запись используется");
				if(data !=1 && data != 5)("Возникла ошибка в работе сайта. Обратитесь в тех. отдел студии!");
				if(data!=5)alert(data);	
			}
			notification_close();
			
		})
		return false;
		
	})
	
	
	//Общее - автоматическая очистка INPUT если VALUE==ALT И НАОБОРОТ
	$("input").live("focus",function(){
		if($(this).attr("alt") != "req"){
			if($(this).val()==$(this).attr("alt"))$(this).val('');
		}
	})
	$("input").live("blur",function(){
		if($(this).attr("alt") != "req"){
			if($(this).val()=="")$(this).val($(this).attr("alt"));
		}
	})
	
	//БОКОВОЕ МЕНЮ - СКРЫВАЮЩИЕСЯ СПИСКИ
	$(".m_item").click(function(){
		$(this).next().next().slideToggle(300, 'easeInCubic');
	})
	
	//СКРОЛ В ШАПКУ
	window.onscroll = function () {
		offy=$(window).scrollTop();
		hgt=$(window).height();
		if(offy>parseInt(hgt/2)){
			$("#to_the_top").fadeIn('fast');	
		}
		else {
			$("#to_the_top").fadeOut('fast');
		}
	}
	$("#to_the_top").click(function(){
		$.scrollTo("[name='pagetop']",1000);
	})
	
	$(".close_notify").live("click",function(){
	$(".big_dark").stop().fadeOut('fast',function(){
		$(this).remove();	
	});
	
	
})
	
})

//ЗНАЧЁК ЗАГРУЗКИ
function globload(){
	if(!($(".globloader").lenght)){
		$("body").append("<div class='globloader'><span></span></div>");	
		$(".globloader").fadeIn(300);
	}
}
function stopload(callback){
	if($(".globloader").length){
		$(".globloader").fadeOut(300,function(){
			$(this).remove();	
			if(typeof callback == 'function'){
				callback.call(this);
			  }

		});
	}
}

//УВЕДОМЛЕНИЕ
function notify(str){
	if(!($("#curnotify").length)){
		$("body").append("<div class='big_dark' id='curnotify'><div class='notify'><p>"+str+"</p><button class='close_notify but_m'><span style='width: 120px;'>Ок</span></button></div></div>");
		$("#curnotify").fadeIn('fast').delay(2000).fadeOut('fast',function(){$(this).remove();});
	}
}

function make_error(str,el,tp){
	var d = new Date();
	var curid=d.getTime();
	if(tp==0)var cls="warning";
	if(tp==1)var cls="success";
	$(el).append("<div style='width:644px;' class='"+cls+"' id='warn_"+curid+"'>"+str+"</div>");
	$("#warn_"+curid).slideDown('fast').delay(2000).slideUp('fast',function(){$(this).remove();});
}

function make_notification(form,str){
	if(document.getElementById("notification")!=null){
		el=$("#notification");
		el.remove();	
	}
	$('body').append("<dib class='big_dark'></div><div id='notification'><h1>Внимание!</h1><p>"+str+"</p><div class='buttons'><button type='button' id='sub_but' class='but_m'><span>Да</span></button><button type='button' class='close_notify but_m'><span>Нет</span></button></div>");
	el=$("#notification");
	$(el).fadeIn();
	el2=("#sub_but");
	$(el2).bind("click",function(){
		$(form).submit();
	})
}


function notification_close(){
		if(document.getElementById("notification")!=null){
			el=$("#notification");
			$(el).fadeOut("fast");
			$(".big_dark").fadeOut("fast",function(){
				$(this).remove();
			})
		}
}

function redirect_new_admin(e) {
	e.preventDefault();
	$.ajax({
		url: base_url+"main/get_new_admin_url",
		async: false,
		type: "POST",
		success: function(data) {
			if(data !=0 ) {
				window.location.href = data;
			}
		}
	})
}

