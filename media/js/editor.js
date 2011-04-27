tinyMCE.init({
               mode : "textareas",
               width : "600",
               height : "200",
               theme : "advanced",
               theme_advanced_toolbar_align : "left",
               theme_advanced_toolbar_location : "top",
               theme_advanced_buttons1 : "bold,italic,underline,bullist,numlist,outdent,indent,blockquote,undo,",
               theme_advanced_buttons2 : "",
               theme_advanced_buttons3 : "",
               plugins : "paste",
               paste_auto_cleanup_on_paste : true,
               paste_strip_class_attributes: 'all',
               paste_remove_styles: true,
               valid_elements : "@[id|title|dir<ltr?rtl|lang|xml::lang],a[rel|rev|"
                                + "charset|hreflang|name|href|title],strong/b,em/i,"
                                + "strike,u,p,-ol,-ul,-li,br,-sub,-sup,-blockquote,"
                                + ",-code,-pre,address,-h1,-h2,-h3,-h4,-h5,"
                                + "-h6,hr[size|noshade],dd,dl,dt,cite,abbr,acronym,"
                                + "del[datetime|cite],ins[datetime|cite]",
             });
