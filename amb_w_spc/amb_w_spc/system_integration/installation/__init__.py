import frappe

def validate_system_requirements():
    """
    Validate system requirements before installing amb_w_spc app
    """
    try:
        # Check if required apps are installed
        installed_apps = frappe.get_installed_apps()
        
        if 'erpnext' not in installed_apps:
            frappe.throw("ERPNext is required but not installed. Please install ERPNext first.")
            
        frappe.msgprint("✅ System requirements validated successfully")
        return True
        
    except Exception as e:
        frappe.log_error(f"System requirements validation failed: {str(e)}")
        raise

def check_erpnext_version():
    """
    Check ERPNext version compatibility
    """
    try:
        # Get ERPNext version
        erpnext_version = None
        try:
            from erpnext import __version__ as erpnext_ver
            erpnext_version = erpnext_ver
        except ImportError:
            frappe.throw("ERPNext is not installed")
        
        if erpnext_version:
            frappe.msgprint(f"✅ ERPNext version {erpnext_version} detected")
        
        return True
        
    except Exception as e:
        frappe.log_error(f"ERPNext version check failed: {str(e)}")
        raise

# Add any other functions that might be referenced
def setup_warehouse_permissions():
    """Setup warehouse permissions - placeholder"""
    pass

def create_default_warehouse_zones():
    """Create default warehouse zones - placeholder""" 
    pass
