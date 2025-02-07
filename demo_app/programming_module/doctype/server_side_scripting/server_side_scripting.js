// // Copyright (c) 2025, asd and contributors
// // For license information, please see license.txt

frappe.ui.form.on("Server Side Scripting", {
	refresh(frm) {
        frappe.msgprint("Hello")
	},


//     // ---------------------------   Server Side Calling -----------------------------------------
    // enable:function(frm){
    //     frm.call({
    //         doc: frm.doc,
    //         method: 'frm_call',
    //         args: {
    //             msg: "Hello"
    //         },
    //         freeze: true,
    //         freeze_message: __('Calling frm_call Methods'),
    //         callback: function(r){
    //             frappe.msgprint(r.message)
    //         }
    //     });

    // }

    

    // enable:function(frm){
    //     frappe.call({
            
    //         method: "demo_app.programming_module.doctype.client_side_scripting.client_side_scripting.frappe_call",
    //         args: {
    //             msg: "Hello"
    //         },
    //         // freeze: true,
    //         // freeze_message: __('Calling frappe_call Methods'),
    //         callback: function(r){
    //             frappe.msgprint(r.message)
    //         }
    //     });


    // }

// ------------------------------------------- frm.call (Client code) -----------------------------------------------
//     refresh: function (frm) {
//         frm.add_custom_button(__('Create Record in Another Doctype'), function () {
//             frappe.call({
//                 method: "demo_app.programming_module.doctype.client_side_scripting.client_side_scripting.new_document",
//                 callback: function(r){
//                     if(r.message){
//                         frappe.msgprint(__('New Record Created: ' + r.message));
//                     }
//                 }
//             });
//         });
//     }

    
});


// --------------------------------------------frappe call -----------------------------------------------------------
// frappe.ui.form.on("Server Side Scripting", {
// 	refresh(frm){
//         frm.add_custom_button(__("Button One"),function(){
//             frappe.call({
//                 method:"demo_app.programming_module.doctype.client_side_scripting.client_side_scripting.insert_record",
//                 callback:function(response){
//                     if(response.message){
//                         frappe.msgprint(response.message)
//                     }
//                 },
//             });
            
//         });
// },
// });
// -------------------------------------------------------------------------------------------------------------------------
