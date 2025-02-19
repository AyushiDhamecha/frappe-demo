frappe.pages['chart_page'].on_page_load = function(wrapper) {
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Realtime Chart',
        single_column: true
    });

    $(wrapper).find('.layout-main-section').append('<div id="chart"></div>');

    const data = {
        datasets: [{
            name: "Live Data",
            values: []
        }]
    };

    // Initialize Realtime Chart
    let chart = new frappe.ui.RealtimeChart("#chart", "test_event", 10, {
        title: "Live Updates",
        data: data,
        type: "line",
        height: 250,
        colors: ["#7cd6fd"]
    });

    // Call Python API to Start Data Publishing
    frappe.call({
        method: "your_app.api.publish_realtime_chart"
    });
};
