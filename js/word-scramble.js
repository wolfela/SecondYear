var cols = document.querySelectorAll('#boxes .box');
[].forEach.call(cols, function(col) {
    col.addEventListener('dragstart', handleDragStart, false);
    col.addEventListener('dragenter', handleDragEnter, false);
    col.addEventListener('dragover', handleDragOver, false);
    col.addEventListener('dragleave', handleDragLeave, false);
    col.addEventListener('drop', handleDrop, false);
    col.addEventListener('dragend', handleDragEnd, false);
});

var dragSrcEl = null;

function handleDragOver(e) {
    if (e.preventDefault) {
        e.preventDefault(); // Necessary. Allows us to drop.
    }
    e.dataTransfer.dropEffect = 'move';  // See the section on the DataTransfer object.

    return false;
}

function handleDragEnter(e) {
    // this / e.target is the current hover target.
    this.classList.add('over');
}

function handleDragLeave(e) {
    this.classList.remove('over');  // this / e.target is previous target element.
}

function handleDragEnd(e) {
    // this/e.target is the source node.

    [].forEach.call(cols, function (col) {
        col.classList.remove('over');
    });
}

function handleDragStart(e) {
    // Target (this) element is the source node.
    dragSrcEl = this;

    e.dataTransfer.effectAllowed = 'move';
    e.dataTransfer.setData('text/html', this.innerHTML);
}

function handleDrop(e) {
    // this/e.target is current target element.

    if (e.stopPropagation) {
        e.stopPropagation(); // Stops some browsers from redirecting.
    }

    // Don't do anything if dropping the same column we're dragging.
    if (dragSrcEl != this) {
        // Set the source column's HTML to the HTML of the column we dropped on.
        dragSrcEl.innerHTML = this.innerHTML;
        this.innerHTML = e.dataTransfer.getData('text/html');
        changeanswer();
    }
    return false;
}

function changeanswer() {
    var answer = [];
    for (var ans of cols) {
        answer.push($(ans).text());
    }
    document.getElementById('answer').value = answer;
};

function proceed() {
    var form = document.createElement('form');
    form.setAttribute('method', 'post');
    form.setAttribute('action', '');
    form.style.display = 'hidden';
    document.body.appendChild(form);
    form.submit();
}

$("#check").click(function () {
        var correct_string = document.getElementById("correct").value;
        var correct = correct_string.split(" ");
        var i = 0;
            for (var col of cols) {
                col.removeEventListener('dragstart', handleDragStart, false);
                col.removeEventListener('dragenter', handleDragEnter, false);
                col.removeEventListener('dragover', handleDragOver, false);
                col.removeEventListener('dragleave', handleDragLeave, false);
                col.removeEventListener('drop', handleDrop, false);
                col.removeEventListener('dragend', handleDragEnd, false);

                if($(col).text()==correct[i]){
                 $(col).addClass('right');
                }
                else{
                    $(col).addClass('wrong');
                }
                i++;
             }

});


  $('#post-form').on('submit', function(event) {

    var $btn = $(document.activeElement);
    if($btn.attr('name') == 'save_form') {
      var allFilled = true;
      $('.req').each(function() {
        if($(this).val() == '') {
          allFilled = false;
        }
      });

      if(!allFilled) {
        alert('You have missed out one of more fields :( Please fill all of them in');
        event.preventDefault();
      }
    }

  });



$("#preview").click(function () {

 window.open("http://localhost:8000/ws/preview");

});
