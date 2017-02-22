CKEDITOR.replace('gapFillInput', {
    allowedContent: true,
    removePlugins: 'elementspath'
});

function getSelected() {
    return CKEDITOR.instances.gapFillInput.getSelection().getSelectedText();
}

function correctFormat(text){
    var data = CKEDITOR.instances.gapFillInput.getData();
    var html = '<span style="color:red">' + text.trim() + '</span>';
    var pos = data.search(html)+html.length;
    if(!/\s/.test(data.charAt(pos))){
        CKEDITOR.instances.gapFillInput.setData([data.slice(0,pos),'&nbsp;',data.slice(pos)].join(''));
    }

}

function addGap(){
    var text = getSelected();
    if(text.length!=0) {
        var editor = CKEDITOR.instances.gapFillInput;
        if (editor.mode == 'wysiwyg') {
            editor.insertHtml('<span style="color:red">' + text + '</span>');
            correctFormat(text)
        } else {
            alert("WYSIWYG!");
        }
    }
}

function deleteGap() {
    var text = getSelected();
    if(text.length!=0) {
        var selection = getSelected().trim();
        var editor = CKEDITOR.instances.gapFillInput;
        editor.insertHtml(selection);
    }
}

function removeHTML(html){
    for(var i =0;i<html.length;i++){
        html[i] = html[i].replace(/<[^>]*>/g,"")
    }
}

function createQuiz() {
    var editor = CKEDITOR.instances.gapFillInput;
    var data = editor.getData();
    //Gets text that has gaps in it
    var spanless = data.split(/<span[^>]*>[^>]*<\/span>/g);
    removeHTML(spanless);
    //Get gaps
    var gaps = [];
    var gap = /<span[^>]*>[^>]*<\/span>/g.exec(data);
    if(gap!=null) {
        gaps.push(gap.toString().replace(/<\/?span[^>]*>/g, ''));
    }
    displayQuiz(gaps,spanless);
}