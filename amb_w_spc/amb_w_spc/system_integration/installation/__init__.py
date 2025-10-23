import frappe

def validate_system_requirements():
    """
    Validate system requirements before installing the app
    """
    try:
        # Check if ERPNext is installed
        if not frappe.db.exists("Module Def", "ERPNext"):
            frappe.throw("ERPNext is required but not installed")
        
        # Check Frappe version
        frappe_version = frappe.__version__
        if int(frappe_version.split('.')[0]) < 15:
            frappe.throw(f"Frappe version 15 or higher required. Current version: {frappe_version}")
        
        # Add any other system validation checks here
        frappe.msgprint("System requirements validated successfully")
        
    except Exception as e:
        frappe.log_error(f"System requirements validation failed: {str(e)}")
        raise
