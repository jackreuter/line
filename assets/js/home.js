
$(document).ready(function() {
  $(".summary-button").each(function(){
  $(this).click(function() {
    $(this).next('#summary').slideToggle('slow');
  });
});
  $('.plus').click(function() {
    $(this).click(function() {
  	$('#share-post-0').slideToggle('slow');
  });
  });
   $('#share-post-0').click(function() {
  	$('#share-post-1').slideToggle('slow');
  });
    $('#share-post-1').click(function() {
  	$('#share-post-2').slideToggle('slow');
  });
     $('#share-post-2').click(function() {
  	$('#share-post-3').slideToggle('slow');
  });
      $('#share-post-3').click(function() {
  	$('#share-post-4').slideToggle('slow');
  });
       $('#share-post-4').click(function() {
  	$('#share-post-5').slideToggle('slow');
  });
  $('[data-toggle=tooltip]').tooltip();
});

