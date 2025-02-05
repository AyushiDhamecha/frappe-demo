// Copyright (c) 2025, asd and contributors
// For license information, please see license.txt

frappe.ui.form.on("Client Side Scripting", {
	// refresh: function(frm) {
    //     frappe.msgprint("Hello, how are you ?");
    // },
        // frappe.throw("This is Error");

        ////////////////////////////// EVENTS /////////////////////////////////////////////
        
    // refresh: function(frm){
    //     frappe.msgprint("hello asd from 'refresh' event");
    // }

    // onload: function(frm){
    //     frappe.msgprint("hello asd from 'refresh' event");
    // }

    // validate: function(frm){
    //     frappe.msgprint("hello asd from 'validate' event");
    // }

    // before_save: function(frm){
    //     frappe.msgprint("hello asd from 'refresh' event");
    // }

    // after_save: function(frm){
    //     frappe.msgprint("hello asd from 'refresh' event");
    // }

    // enable: function(frm){
    //     frappe.msgprint("hello asd from 'enable' event");
    // }

    // age: function(frm){
    //     frappe.msgprint("hello asd from 'refresh' event");
    // }

    // family_member_on_form_rendered: function(frm){
    //     frappe.msgprint("hello asd from 'refresh' event");
    // }

    // before_submit: function(frm){
    //     frappe.msgprint("hello asd from 'refresh' event");
    // }

    // on_submit: function(frm){
    //     frappe.msgprint("hello asd from 'refresh' event");
    // }

    // before_cancle: function(frm){
    //     frappe.msgprint("hello asd from 'refresh' event");
    // }

    // after_cancle: function(frm){
    //     frappe.msgprint("hello asd from 'refresh' event");
    // }

   

    /////////////////////////////////////  VALUE FATCHING //////////////////////////////////////

    // after_save:function(frm){
    //     frappe.msgprint(__( "The full name is '{0}'",
    //         [frm.doc.first_name +" "+frm.doc.middle_name+" "+frm.doc.last_name]
    //     ))

    //     for(let row of frm.doc.family_members){
    //         frappe.msgprint(__("{0}. The family member name is '{1}' and relation is '{2}' ",
    //             [row.idx,row.name1,row.relation]
    //         ))
    //     }
    // }
    // ----------------------------------------------------------------------------------------------------
    
    //////////////////////////////////////Set intro ////////////////////////////////////////////////
    // refresh:function(frm){
    //     // --------this massge shows every time-------------
    //     frm.set_intro("This is intro")

    //     // -----------this massege shows only first time-----------
    //     if(frm.is_new()){
    //         frm.set_intro("This is new intro")
    //     }
    // }

    // validate:function(frm){
    //     frm.set_value('full_name',frm.doc.first_name+" "+frm.doc.middle_name+" "+frm.doc.last_name)

    //     let row = frm.add_child('family_members',{
    //         name1:'john',
    //         relation:'father',
    //         age:44,
    //     })
    // }
    

    /////////////////////////////////   Custom  Button   /////////////////////////////////////////////
    // refresh:function(frm){
    //     // frm.add_custom_button('custom button',()=>{
    //     //     frappe.msgprint(__('you clicked me....!!'))
    //     // })

    //     frm.add_custom_button('button 1',()=>{
    //         frappe.msgprint(__('button 1 is clicked ....!!'))
    //     },'custom button')
        
    //     frm.add_custom_button('button 2',()=>{
    //         frappe.msgprint(__('button 2 is clicked ....!!'))
    //     },'custom button')

    //     frm.add_custom_button('button 3',()=>{
    //         frappe.msgprint(__('button 3  is clicked ....!!'))
    //     },'custom button')
    // }
});

////////////////////////////////////// CHILD TABLE EVENTS /////////////////////////////////////////

frappe.ui.form.on('Family Members',{
        // cdn is child Doctype 

        // name1: function(frm){
        //     frappe.msgprint("hello asd from child doctype 'name1' event")
        // }

        // Age(frm, cdt, cdn){
        //     frappe.msgprint("hello asd from child doctype 'age' event")
        // }

       
})


