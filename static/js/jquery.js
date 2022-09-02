var maxc = 50,
    crop = '<span class="crop">...</span>';
$('.text').each(function(){
  var text = $(this),
      html = text.html(),
      html_hide = '<span class="hide">' + html.substring(maxc) + '</span>',
      html_show = '<span class="show">' + html.substring(0, maxc) + '</span>';
  text.html(html_show + crop + html_hide);
});
$('.show').click(function(){
  $(this).parent('.text').addClass('more');
});