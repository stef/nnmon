function empty(node) {
   if(node.text().trim()) return false;
   return true;
}
function check1st4() {
  var country=$('#id_country').val();
  var op=$('#id_operator').val();
  var contract=$('#id_contract').val();
  var media=$('#id_media').val();
  var div=$('#similar_cases');
  if(country && op && contract && media) {
     //http://localhost:8001/lookup/?country=HU&contract=asdf&operator=Voda&media=fixed
     $.getJSON('/lookup/?country='+country+'&contract='+contract+'&operator='+op+'&media='+media, function(data) {
        if (data.length>0) {
           div.parent().removeClass('hidden');
        } else {
           div.parent().addClass('hidden');
        }
        while(data) {
           var val=data.pop();
           div.append('<li><a href="/view/'+val[0]+'">'+(val[1] || "no resource given")+'</a></li>');
        };
     });
     $('#id_comment').parent().parent().show().focus();
     $('#id_comment_ifr').focus();
     $('#id_email').parent().parent().show();
     $('#id_consent').parent().parent().show();
     $('#id_nick').parent().parent().show();
     $('#id_attachments0').parent().parent().show();
     $("#save_button").attr('disabled','true').show();
  } else {
     div.parent().addClass('hidden');
  }
}
function init_form() {
  $('.help_text').hide();
  $(".fieldWrapper").focusin(function(event) {if(!empty($(this).find('.help_text'))) $(this).find('.help_text').show();});
  $(".fieldWrapper").focusout(function(event) {if(!empty($(this).find('.help_text'))) $(this).find('.help_text').hide();});
  $("#show_optionals").hide();
  $("#id_contractual").click(function(event) {
                               $("#id_contract_excerpt_parent").parent().parent().toggle();
                             });
  $("#show_optionals").click(function(event) {
                               $(this).hide();
                               $("#optional .fieldWrapper").show();
                               $("#id_contract_excerpt_parent").parent().parent().hide();
                             });
  $('#id_country').change(function() {
                            var country=$(this).attr('value');
                            if(country.length>0) {
                              $.getJSON('/api/'+country, function(data) {
                                          $("#id_operator").autocomplete(data, { minChars: 0, autoFill: true });
                                          $('#id_operator').focus();
                                        });
                            }
                            check1st4();
                          });
  $('#id_operator').change(function() {
                             var country=$('#id_country').attr('value');
                             var operator=$(this).val();
                             if(operator.length>0) {
                               $.getJSON('/api/'+country+'/'+operator, function(data) {
                                           $("#id_contract").autocomplete(data,{ minChars: 0 });
                                           $('#id_contract').focus();
                                         });
                             }
                            check1st4();
                           });
  $('#id_contract').change(function() {
                            check1st4();
                           });
  $('#id_media').change(function() {
                            check1st4();
                           });
  $('#id_email').change(function() {
                             if($(this).val().length>0) {
                               $('#id_captcha_0').parent().parent().show();
                               $('#save_button').removeAttr('disabled');
                               $("#show_optionals").show();
                             }
                        });
  $("form").bind("keypress", function(e) {
                   if (e.keyCode == 13) {
                     e.preventDefault();
                     $(e.target).change();
                     return false;
                   }
                   return true;
                 });
}
