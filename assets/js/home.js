
$(document).ready(function() {
  $(".summary-button").each(function() {
     $(this).click(function() {
    $(this).next().slideToggle('slow');
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

