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
		
	'logout': function(data, callback){
		$.ajax({
			url: "/users/logout",
			method: "POST",
			data: data
		}).done(callback)	
	},


	'runSingleGame': function(data, callback){
		$.ajax({
			url:"/users/singlegame",
			method: "GET",
			data: data
		}).done(callback)
	},

	'setTeams': function(data, callback){
		$.ajax({
			url:"/users/setteams",
			method: "POST",
			data: data
		}).done(callback)
	},


	// 'runSeason': function(data, callback){
	// 	$.ajax({
	// 		url:"/users/runseason",
	// 		method: "GET",
	// 		data: data
	// 	}).done(callback)
	// },

};





