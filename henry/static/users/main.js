
var registerForm = function(event) {
	event.preventDefault();
	var template = $('#_register_form_template').html();
	$("#main-body").html(template);
	// main-body has all the templates
	$("#nav_bar_container").hide();
	//hides main menu elements for cleaner look 
};

var loginForm = function(event) {
	event.preventDefault();
	// console.log("TEST")
	var template = $("#_login_form_template").html();
	$("#main-body").html(template);
	$("#nav_bar_container").hide();
	//hides main menu elements for cleaner look 
};
		
var registerUser = function(event) {
	// console.log('works?')
	event.preventDefault();
	// var $this = $(this);
	var formData = $(this).serialize();
	var callback = function(response){
		//after user is refistered, he/she will get routed to user_menu_page

		// var template = "{{test}}";
		// var rendered = Mustache.render(template, {"test":"some value"});
		
		// console.log($("#_user_menu_template").html);
		var template = $("#_user_menu_template").html();
		// $("#nav_bar_container").html(template);

		var rendered = Mustache.render(template, response);
		$("#main-body").html(rendered);
		// after successful registration, takes new user to the user page
		$("#register_form").hide();
		//hides main menu elements for cleaner look 
	};

	Users.register(formData, callback);
};		

var loginUser = function(event){
	event.preventDefault();
	var formData = $(this).serialize();
	var callback = function(response){
		// console.log(response);
		if(response.logged_in === "true"){	
			var template = $('#_user_menu_template').html();
			$('#nav_bar_container').html(template);
			// $('#nav_bar_container').html("write here whatever I want!!");
			var rendered = Mustache.render(template, response);
			$("#main-body").html(rendered);
			// after successully logging in, takes user to the user page
			$("#login_form").hide();
		} 
		else {
			$("#login_form").append("Invalid Login and/ or Password");
		}
	};

	Users.login(formData, callback);
};

var logoutUser =function(event){
	var formData = $(this).serialize();
	// 		var template = $('#index').html();
	// 		$('#nav_bar_container').html(template);
	// 	}
	// 		var rendered = Mustache.render(template, response);
	// 		$("#main-body").html(rendered);
	// };
	Users.logout(formData);
};

var runSingleGame = function(event){
		// console.log("event listener works")
	event.preventDefault();
	var formData = $(this).serialize();
	console.log("TEST")
	var callback = function(response){
		var template = $("#_single_game_template").html();
		var rendered = Mustache.render(template, response);
		$("#main-body").html(rendered);
	};

	Users.runSingleGame(formData, callback);
};

var setTeams = function(event) {
	//console.log("event listener works")
	event.preventDefault();
	var formData = $(this).serialize();
	var callback = function(response){
		var template = $("#_set_teams_template").html();
		// var template = $("#_single_game_template").html();

		var rendered = Mustache.render(template, response);
		$("#main-body").html(rendered);
	};

	Users.setTeams(formData, callback)
};


// pass through dict the values of teams and seasons
// make api calls get elememt byID pass through json

// var runSeason = function(event){
// 	console.log("event listener works")
// 	event.preventDefault();
// 	var formData = $(this).serialize();
// 	var url = $(this).attr("action");
// 	console.log(url);

// 	var callback =function(response){
// 		var template = $('#_run_season_template').html();
// 		var rendered = Mustache.render(template, response);
// 		$("#main-body").html(rendered);
// 	};

// 	Users.runSeason(formData, callback)

// };

// $("#form").submit(function(event) {

// var runSingleGame =function(event){
// var formData = $(this).serialize();



// 	// var $form = $(this),
// 	$inputs = $form.find("input, select, button, textarea"),
// 	serializedData = $form.serialize();

// 	$.ajax({
// 		url: "/donate/",
// 		type: "post",
// 		data: serializeData,
// 		success: function(response) {
// 		    alert(response)
// 		}
// 	})
// 	event.preventDefault();
// 	});




$(document).ready(function (){

	$('#nav_bar_container').on('click', '#register_user', registerForm);

	$("#main-body").on('submit', '#register_form', registerUser);

	$('#nav_bar_container').on('click', '#login_user', loginForm);

	$("#main-body").on('submit', '#login_form', loginUser);
	
	$('#nav_bar_container').on('click', '#logout', logoutUser);

	$('#main-body').on('click', '#single_game', runSingleGame);

	$(document).on('submit', '#set_teams', setTeams);



});


