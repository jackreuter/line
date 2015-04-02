$(document).ready(function() {
  $(".summary-button").each(function() {
     $(this).click(function() {
    $(this).next().slideToggle('slow');
});
   });
  $(".post").each(function(){
    $(this).hover(function(){
      $(this).css("background-color", "#E4F1FE");
    },function(){
      $(this).css("background-color","white");
    });    
  });
  $('.plus').each(function() {
    $(this).click(function() {
  	$(this).next().slideToggle('slow');
  });
  });
  //  $('.trigger-share-1').each(function() {
  //    $(this).click(function() {
  //   $(this).parent().css("background color", "red");
  //   });
  // });
  //   $('.share-post-1').click(function() {
  // 	 $(this).click(function() {
  //   $(this).next().slideToggle('slow');
  //   });
  // });
  //    $('.share-post-2').click(function() {
  // 	 $(this).click(function() {
  //   $(this).next().slideToggle('slow');
  //   });
  // });
  //     $('.share-post-3').click(function() {
  // 	 $(this).click(function() {
  //   $(this).next().slideToggle('slow');
  //   });
  // });
  //      $('.share-post-4').click(function() {
  // 	$(this).click(function() {
  //   $(this).next().slideToggle('slow');
  // });
  // });
  $('[data-toggle=tooltip]').tooltip();
});