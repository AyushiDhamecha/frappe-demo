import frappe
import random
import time

@frappe.whitelist()
def publish_realtime_chart():
    """Publishes data to the frontend in real-time"""
    for i in range(10):  # Sends 10 updates
        data = {
            "label": i,
            "points": [random.randint(10, 100)]
        }
        frappe.publish_realtime("test_event", data)
        time.sleep(2)  # Simulate real-time updates