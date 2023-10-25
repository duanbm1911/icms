jQuery(document).ready(function($){
    $('li.dropdown-submenu-inventory a[data-toggle="dropdown"]').on('click', function(event) {
      event.preventDefault();
      event.stopPropagation();
      $('li.dropdown-submenu').not($(this).parent()).removeClass('open');
      $(this).parent().toggleClass('open');
    });
    $('li.dropdown-submenu-ipplan a[data-toggle="dropdown"]').on('click', function(event) {
      event.preventDefault();
      event.stopPropagation();
      $('li.dropdown-submenu').not($(this).parent()).removeClass('open');
      $(this).parent().toggleClass('open');
    });
  });
