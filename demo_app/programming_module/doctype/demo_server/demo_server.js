// Copyright (c) 2025, asd and contributors
// For license information, please see license.txt

frappe.ui.form.on("Demo_Server", {
	refresh: function (frm) {
        let chart = new frappe.ui.RealtimeChart("#chart", "test_event", 8,{  
            data: {
                labels: ["Jan", "Feb", "Mar", "Apr"],
                datasets: [
                    {
                        name: "Sales",
                        values: [100, 200, 150, 300]
                    }
                ]
            },
            type: 'bar', // Types: bar, line, pie, donut, percentage, heatmap
            colors: ['#7cd6fd']
        });
    }
}); 
