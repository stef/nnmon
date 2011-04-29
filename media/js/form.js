function init_form() {
  $('.help_text').hide();
  $(".fieldWrapper").hover(function(event) {$(this).find('.help_text').toggle();});
  $("#show_optionals").hide();
  $("#id_contractual").click(function(event) {
                               $("#id_contract_excerpt_parent").parent().toggle();
                             });
  $("#show_optionals").click(function(event) {
                               $(this).hide();
                               $("#optional .fieldWrapper").show();
                               $("#id_contract_excerpt_parent").parent().hide();
                             });
  $('#id_country').change(function() {
                            var country=$(this).attr('value');
                            if(country.length>0) {
                              $('#id_operator').parent().show();
                              $.getJSON('/ajax/'+country, function(data) {
                                          $("#id_operator").autocomplete(data, { minChars: 0, autoFill: true, });
                                        });
                            }
                          });
  $('#id_operator').change(function() {
                             var country=$('#id_country').attr('value');
                             var operator=$(this).val();
                             if(operator.length>0) {
                               $('#id_contract').parent().show();
                               $.getJSON('/ajax/'+country+'/'+operator, function(data) {
                                           $("#id_contract").autocomplete(data,{ minChars: 0, });
                                         });
                             }
                           });
  $('#id_contract').change(function() {
                             if($(this).val().length>0) {
                               $('#id_comment').parent().show();
                               $('#id_email').parent().show();
                               $('#id_attachments0').parent().show();
                             }
                           });
  $('#id_email').change(function() {
                             if($(this).val().length>0) {
                               $('#id_captcha_0').parent().show();
                               $('#save_button').show();
                               $("#show_optionals").show();
                             }
                        });
}
