var amount = 4;

$(document).ready(function() {


	$('#addField').click(function() {
		if(amount < 10){
			$("#addAnswer").append(" <input type=\"text\" class=\"mcinputbox\" name=\"answers[]\" placeholder=\"Type your answer in here\">");
			amount++;			
		}
	});
	$('#removeField').click(function() {
		if(amount > 4){
			console.log("fsdfdsf");
			$("#addAnswer input:last").remove();
			amount--;
		}


	});





$("#check").click(function () {

		var answer = document.querySelector('input[name="answers"]:checked').value;
		var correct = document.getElementById("correct").value;
		var id_checkbox = $('input[type=radio][name="answers"]:checked').attr('id');
		var id = id_checkbox.split("-"); 
		var id_text = id[1];

		$('#choices').children('input').each(function () {
			if(this.value!=answer){
				this.disabled=true;
			}
		});


		if(correct==answer){
			var field = document.getElementById(id_text);
			$(field).addClass('right');
		}
		else{
			var field = document.getElementById(id_text);
			$(field).addClass('wrong');
		}

});


// $('#post-form').on('submit', function(){


//   console.log("#answers[1]".val());

//   // var txt = $('#correct');
//   // var txt2 = $('#correct');
//   // txt.val(["updated ", txt.val()]);

//   // var data = $('post-form').serialize();
//   // $.post('/mca/submit/', data);
//   //   setTimeout(function() { correct.value = txt.val(); }, 0);
//     // event.preventDefault();
//     // console.log($('answers').val())  // sanity check
//     // create_post();
// });

 function create_post() {

var a1=$("#correct").val();
var a2=$("#answers").val();
var a3=$("#a3").val();
var a4=$("#a4").val();
var title=$("#title").val();
var list=[a2];
var myJson = JSON.stringify(list); 

console.log(a1);
console.log(a2);
$.ajax({
    url : './submit/',
    type: 'POST',
    data:{
        'title':title,
        'answers': myJson,
        'correct': a1
            },
    contentType:'application/json',
    success: function(data){
            alert("woo!");
        window.open("http://localhost:8000/mcq2/")
       // window.location.assign('http://localhost:8000/mcq2/');
        //$().redirect('http://localhost:8000/mcq2/', {'a1': 'value1', 'a2': 'value2'});
    },
    error: function(){
        alert('nope');
    }
});
};


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});



// function create_post() {
//     console.log("create post is working!") // sanity check
//     $.ajax({
//         url : "/mc/submit/", // the endpoint
//         type : "POST", // http method
//         data : { $('post-form').val() }, // data sent with the post request

//         // handle a successful response
//         success : function() {
//             console.log("success"); // another sanity check
//         },

//         // handle a non-successful response
//         error : function() {
//             console.log("error"; // provide a bit more info about the error to the console
//         }
//     });
// };


// $("#saveQuestion").click(function () {

// var a1=$("#a1").val();
// var a2=$("#a2").val();
// var a3=$("#a3").val();
// var a4=$("#a4").val();
// var title=$("#title").val();
// var list=[a2,a3,a4];
// var myJson = JSON.stringify(list); 

// console.log(a1);
// console.log(a2);
// $.ajax({
//     url : './ajax/validate/',
//     type: 'GET',
//     data:{
//         'a1': a1,
//         'list': myJson,
//         'title':title
//             },
//     contentType:'application/json',
//     success: function(data){
//         if(data.is_taken){
//             alert("woo!");
//         }
//         console.log(data.is_taken);
//         window.open("http://localhost:8000/mcq2/")
//        // window.location.assign('http://localhost:8000/mcq2/');
//         //$().redirect('http://localhost:8000/mcq2/', {'a1': 'value1', 'a2': 'value2'});
//     },
//     error: function(){
//         alert('nope');
//     }
// });
// });


// $("#cancelQuestion").click(function () {

// var a1=$("#a1").val();
// var a2=$("#a2").val();
// console.log(a1);
// console.log(a2);
// $.ajax({
//     url : './ajax/validatee/',
//     type: 'GET',
//     data:{
//         'a1': a1,
//         'a2': a2
//             },
//     contentType:'application/json',
//     success: function(data){
        
//         alert(data.is_taken);
        
//         console.log(data.is_taken);
//     },
//     error: function(){
//         alert('nope');
//     }
// });
// });







/*

 $("#saveQuestion").click(function () {
     var a1=$("#a1").val();
    console.log(a1)  // sanity check
      $.ajax({
        url: '/ajax/validate/',
        data: {
          'a1': a1
        },
        dataType: 'json',
        success: function (data) {
            console.log("here")  // sanity check
          if (data.is_taken) {
            alert("A user with this username already exists.");
          }
        },
        error: function(err){ console.log('my message'+err); }
      });

    });


*/
/*

        $('#saveQuestion').click(function(){
      var a1=$("#a1").val();
      var a2=$("#a2").val();
      console.log("saved with the stupid button!")  // sanity check
     // var userid = //get your user id in some way you can
      //var total = parseInt(localStorage['total']);
      $.ajax({
        url: "../../../coolbeans/app/views/question.py/MCQCreateView/savethis",
        type:"POST",
        data: {a1:a1,a2:a1},
          success: function(json){
            console.log(a1);
          }
      });

    });


        $('#saveQuestion').click(function(){
      var a1=$("#a1").val();
      console.log("saved with the stupid button!")  // sanity check
     // var userid = //get your user id in some way you can
      //var total = parseInt(localStorage['total']);
      $.ajax({
        url: "/MCQ-Creation-update.html",
        type:"POST",
        data: {a1:a1,a2:a1}
      }).done(function(data){
          console.log("dsddd");
           console.log(a1);
         alert(data);//do what you want to do with response
      });

    }); */

        /*

	$('#saveQuestion').click(function(event){
	    event.preventDefault();
	    console.log("saved with the stupid button!")  // sanity check
	    save_question();
	});
	


	    // AJAX for posting
    function save_question() {
        console.log("save q is working") // sanity check
        var a1 = $("#a1").val();
        console.log(a1);
        $.ajax({
            url : "save_question/", // the endpoint
            type : "POST", // http method
            data : { a1 : $('#mcq-text').val() }, // data sent with the post request
            // handle a successful response
            success : function(json) {
                $('#a1').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                $("#mcq-text").prepend("<li><strong>"+json.correct+"</strong> - <em> "+json.answers+"</em> - <span> "+json.created+
                    "</span> - <a id='delete-post-"+json.postpk+"'>delete me</a></li>");
                console.log("success"); // another sanity check
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText + "ddd"); // provide a bit more info about the error to the console
            }
        });
    };
*/


});
