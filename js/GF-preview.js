$(document).ready(function() {
    
    var opener = window.opener;
    if(opener) {
        var data = opener.getPreviewData();
    }

    var display = "<label class=\"gapFillQuestions\">"
    for(var i=0; i<data.length; i++){   
        if(data[i]=="$$"){
            display += " <span class=\"gapFillBox\"></span>";
        }else{
            display += " ";
            display += data[i];
        }
    }
    display +=  " </label>"
    $('#gapFillQuestionDiv').append(display);
});
