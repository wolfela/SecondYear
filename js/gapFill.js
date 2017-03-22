var gaps = new Map(),
    selectedRow,
    selectedWord;

CKEDITOR.replace('gapFillInput');

function getText() {
    return CKEDITOR.instances.gapFillInput.getData();
}

function getSelected() {
    return (document.all) ? document.selection.createRange().text : document.getSelection();
}

function loadAltAnswers(altAnswer) {
    var altElement = $('<div class=gapFillAltRow tabindex=1>'+altAnswer+'</div>').appendTo($('.gapFillAltAnswers'));
    $(altElement).click(function () {
        selectedRow = this;
        console.log('yaya')
    })
}

function addOption(content) {
    var option = '<option value='+content+'>'+content+'</option>';
    $('.gapFillAnswerOptions').append(option);
    if($('.gapFillAnswerOptions').children().length==1){
        selectedWord=content;
    }
}

function addGap(){
    var selected = getSelected();
    var text = selected.toString();
    if(text.length!=0) {
        var highlight = document.createElement('SPAN');
        var range = selected.getRangeAt(0);
        highlight.textContent = text;
        highlight.style.cssText = 'color:red';
        range.deleteContents();
        range.insertNode(highlight);
        var altAnswer = [];
        gaps.set(text,altAnswer);
        addOption(text);
    }
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
        $(selected).replaceWith(getSelected().toString())
    }else{
        alert('Be more careful selecting pls(ie dont select spaces')
    }
}

function getChange(select) {
    selectedWord = select.value;
    $('.gapFillAltAnswers').empty();
    var altWords = gaps.get(selectedWord);
    for(var i=0;i<altWords.length;i++){
        loadAltAnswers(altWords[i])
    }
    $('.gapFillAltInput').val('');
}

function addAltGap() {
    var altAnswer = $('.gapFillAltInput').val();
    gaps.get(selectedWord).push(altAnswer);
    $('.gapFillAltAnswers').append('<p>'+altAnswer+'</p>')
    $('.gapFillAltInput').val('');
}

function deleteAltGap() {
    // gaps.get(selectedWord).splice(gaps.get(selectedWord).indexOf($(selectedRow).val()),1);
    console.log($(selectedRow).val());
    $(selectedRow).remove();
}

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
