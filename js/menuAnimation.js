$(document).ready(function() {

    let $menuButton = $(".hamburger"),
        $content = $(".container"),
        $menu = $(".menu-content"),
        $sidebar = $(".sidebar"),
        $title = $(".title-bar-title"),
        isOpen = false;

    $(document).foundation();
    $menuButton.click(function(){
        $menuButton.prop("disabled",true);
        if(isOpen){
            $content.animate({left: "-=110px",opacity:1},350);
            $menu.animate({opacity:0, 'z-index': -1},400);
            $sidebar.animate({width: "-=110px"},350);
            $title.animate({left: "-=110px"},350);
            $menuButton.animate({'margin-left' : "10px"},250, function(){
                $menuButton.toggleClass('cross');
            });
        }else{
            $content.animate({left: "+=110px",opacity:0.5},350);
            $menu.animate({opacity:1, 'z-index': 1},200);
            $sidebar.animate({width: "+=110px"},350);
            $title.animate({left: "+=110px"},350);
            $menuButton.animate({'margin-left': "120px"},350, function(){
                $menuButton.toggleClass('cross');
            });
        }
        isOpen=!isOpen;
        $menuButton.prop("disabled",false);
    });
});
