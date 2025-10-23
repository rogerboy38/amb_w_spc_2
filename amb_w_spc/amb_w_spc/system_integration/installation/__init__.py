import frappe

def validate_system_requirements():
    """
    Validate system requirements before installing amb_w_spc app
    """
    try:
        # Check if required apps are installed - CORRECT WAY
        installed_apps = frappe.get_installed_apps()
        
        if 'erpnext' not in installed_apps:
            frappe.throw("ERPNext is required but not installed. Please install ERPNext first.")
            
        frappe.msgprint("✅ System requirements validated successfully")
        
    except Exception as e:
        frappe.log_error(f"System requirements validation failed: {str(e)}")
        raise
