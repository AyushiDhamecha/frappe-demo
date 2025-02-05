// Copyright (c) 2025, asd and contributors
// For license information, please see license.txt

frappe.ui.form.on("Demo_Client", {
	refresh(frm){
        frm.add_custom_button(__("Button One"),function(){
            frappe.call({
                method:"demo_app.programming_module.doctype.demo_server.demo_server.insert_record",
                callback:function(response){
                    if(response.message){
                        frappe.msgprint(response.message)
                    }
                },
            });
            
        });
},
});
