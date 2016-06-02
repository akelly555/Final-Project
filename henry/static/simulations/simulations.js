simulations.js


var Users = {
	'register': function(data, callback){
		$.ajax({
			url: "/users/register",
			method: "POST",
			data: data
		}).done(callback)	
	},
	'login': function(data, callback){
		$.ajax({
			url: "/users/login",
			method: "POST",
			data: data
		}).done(callback)	
	},
		
	// 'logout': function(data, callback){
	// 	$.ajax({
	// 		url: "/users/logout",
	// 		method: "POST",
	// 		data: data
	// 	}).done(callback)	
	// },


};