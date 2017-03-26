var gaps = [];

CKEDITOR.replace('gapFillInput');

function getText() {
    return CKEDITOR.instances.gapFillInput.getData();
}

function getSelected() {
    return (document.all) ? document.selection.createRange().text : document.getSelection();
}

function addGap(){
    var selected = getSelected();
    var text = selected.toString();
    if(text.length!=0) {
        var highlight = document.createElement('SPAN');
        var range = selected.getRangeAt(0);
        highlight.textContent = text.trim();
        highlight.style.cssText = 'color:red';
        range.deleteContents();
        range.insertNode(highlight);
        if(/^\s/.test(text)){
            highlight.parentNode.insertBefore(document.createTextNode(" "),highlight);
            console.log('Added before');
        }
        if(text.endsWith(' ')){
            highlight.parentNode.insertBefore(document.createTextNode(" "),highlight.nextSibling);
            console.log('Added after');
        }
        gaps.push(text);
    }
    getAnswers();
}

function getSelectedElement() {
    var containerElement = null;
    if (typeof window.getSelection != "undefined") {
        var sel = window.getSelection();
        if (sel.rangeCount) {
            var node = sel.getRangeAt(0).commonAncestorContainer;
            containerElement = node.nodeType == 1 ? node : node.parentNode;
        }
    } else if (typeof document.selection != "undefined" &&
        document.selection.type != "Control") {
        var textRange = document.selection.createRange();
        containerElement = textRange.parentElement();
    }
    return containerElement
}

function deleteGap() {
    var selected = getSelectedElement();
    if($(selected).is('span')) {
        $(selected).replaceWith(getSelected().toString());
        var index = gaps.indexOf(getSelected().toString());
        gaps.splice(index, 1);
        getAnswers();
    }else{
        alert('Be more careful selecting pls(ie dont select spaces');
    }
}

//function getChange(select) {
 //   selectedWord = select.value;
  //  $('.gapFillAltAnswers').empty();
 //   var altWords = gaps.get(selectedWord);
 //   for(var i=0;i<altWords.length;i++){
//        loadAltAnswers(altWords[i])
 //   }
 //   $('.gapFillAltInput').val('');
//}

function closeCKEDITOR(){
    $('.gapFillSelectBox').append('<p>'+ getText() + '</p>');
    CKEDITOR.instances.gapFillInput.setReadOnly(true);
    $('#cke_gapFillInput, .gapFillNext').css({'opacity': '0.3','pointer-events':'none'});
    $('.gapFillSelectBox, .gapFillBack').css({'opacity': '1','pointer-events':'auto'});
}

function openCKEDITOR() {
    $('#cke_gapFillInput, .gapFillNext').css({'opacity': '1','pointer-events':'auto'});
    $('.gapFillSelectBox, .gapFillBack').css({'opacity': '0.3','pointer-events':'none'});
    $('.gapFillSelectBox').empty();
    CKEDITOR.instances.gapFillInput.setReadOnly(false);
}

function getAnswers() {
    //document.getElementById('gaps').value = gaps;
    var question = getText();
    question = question.replace(/<p[^>]*>/g, "");
    question = question.replace(/<\/p[^>]*>/g, "");
    document.getElementById('question').value = question;
    document.getElementById('gaps').value = gaps;
}


$(document).ready(function () {
    $('.gapFillBack').click(function() {
        openCKEDITOR();
    });

    $('.gapFillNext').click(function() {
        closeCKEDITOR();
    });

    $('.gapFillSelect').click(function() {
        addGap();
    });

    $('.gapFillDelete').click(function() {
        deleteGap();
    });

    $('.gapFillAltAdd').click(function() {
        addAltGap();
    });

    $('.gapFillAltDelete').click(function() {
        deleteAltGap();
    });



});

    window.getPreviewData = function() {
    //document.getElementById('gaps').value = gaps;
    var question = getText();
    question = question.replace(/<p[^>]*>/g, "");
    question = question.replace(/<\/p[^>]*>/g, "");
    var all = question.split(" ");
    for(var i=0; i<all.length; i++){
    	for(var j=0; j<gaps.length; j++){
    		if(gaps[j]==all[i]){
    			all[i]="$$"
    		}
    	}
    }

    return all;
}

$("#preview").click(function () {
    window.open("http://localhost:8000/gf/preview");
});
