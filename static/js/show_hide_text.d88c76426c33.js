$(document).ready(function () {
    // Configure/customize these variables.
    var showChar = 70;  // How many characters are shown by default
    var moretext = "more";
    var lesstext = "less";


    $('.more').each(function () {
        var content = $(this).html();

        if (content.length > showChar) {

            var c = content.substr(0, showChar);
            var h = content.substr(showChar, content.length - showChar);

            var html = c + '&nbsp;<span class="moreellipses">' + '...' + '&nbsp;</span><span ' +
                'class="morecontent"><span>' + h + '</span><a href="" class="morelink" style="text-decoration: none">'
                + moretext + '</a></span>';

            $(this).html(html);
        }

    });

    $(".morelink").click(function () {
        if ($(this).hasClass("less")) {
            $(this).removeClass("less");
            $(this).html(moretext);
        } else {
            $(this).addClass("less");
            $(this).html(lesstext);
        }
        $(this).parent().prev().toggle();
        $(this).prev().toggle();
        return false;
    });
});