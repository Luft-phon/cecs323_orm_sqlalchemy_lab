from sqlalchemy.orm import Session, sessionmaker, configure_mappers

from menu_definition import add_menu, list_menu, menu_main, delete_menu
from SQLAlchemyUtilities import check_unique
from part import Part
from assembly import Assembly
from usage import Usage
from piecePart import PiecePart
from vendor import Vendor

# --- Add Functions ---
       
def add_part(sess: Session):
    part_number: str = ''
    part_name: str = ''
    violation = True
    while violation:
        part_number = input("Enter part_number: ")
        part_name = input("Enter part_name: ")
        new_part = Part(part_number, part_name)
<<<<<<< HEAD
        violated_constraints = check_unique(sess, new_part)
        if len(violated_constraints) > 0:
            print('Error: The following uniqueness constraints were violated:')
            print(violated_constraints)
            print('please try again.')
            print(f"")
        else:
            sess.add(new_part)
            # sess.commit()
        violation = False  
    
      

def add_assembly(sess: Session):
    assembly_part_number: str = ''
    violation = True
    while violation:
        assembly_part_number = input("Enter assembly_part_number: ")
        new_assembly = Assembly(assembly_part_number)
        violated_constraints = check_unique(sess, new_assembly)

        parts = list(sess.query(Part))
        
        if len(violated_constraints) > 0:
            print('Error: The following uniqueness constraints were violated:')
            print(violated_constraints)
            print('please try again.')
            print(f"")
        if not any(part.part_number == assembly_part_number for part in parts):
            print(f"Error: Part with part_number '{assembly_part_number}' does not exist. Please add the part first.") 
            print(f"")
        else: 
            sess.add(new_assembly)
            # sess.commit()
        violation = False   
            
def add_piece_parts(sess: Session):
    part_number: str = ''
    vendor_id: str = ''
    violation = True
    while violation:
        part_number = input("Enter part_number: ")
        vendor_id = input("Enter vendor_id: ")
        new_piece_parts = PiecePart(part_number, vendor_id)
        violated_constraints = check_unique(sess, new_piece_parts)
        
        parts = list(sess.query(Part))
        assemblies = list(sess.query(Assembly))
        vendors = list(sess.query(Vendor))

=======
        # pass the active session instance `sess`, not the Session class
        violated_constraints = check_unique(sess, new_part)
>>>>>>> a64a1b6b7ae13907f1f48f62264492cde0900a48
        if len(violated_constraints) > 0:
            print('The following uniqueness constraints were violated:')
            print(violated_constraints)
            print('please try again.')
            print(f"")
        if not any(part.part_number == part_number for part in parts):
            print(f"Error: Part with part_number '{part_number}' does not exist. Please add the part first.")
            print(f"")
        if any(assembly.assembly_part_number == part_number for assembly in assemblies):
            print(f"Error: Assembly with part_number '{part_number}' already exist.")
            print(f"")
        elif not any(vendor.vendor_id == int(vendor_id) for vendor in vendors):
            print(f"Error: Vendor with vendor_id '{vendor_id}' does not exist. Please add the vendor first.")
            print(f"")
        else: 
            sess.add(new_piece_parts)
            # sess.commit()
        violation = False

def add_usage(sess: Session):
    usage_quantity: int = 0
    parts_part_number: str = ''
    assemblies_assembly_part_number: str = ''
    violation = True
    while violation:
        usage_quantity = input("Enter usage_quantity: ")
        parts_part_number = input("Enter parts_part_number: ")
        assemblies_assembly_part_number = input("Enter assemblies_assembly_part_number: ")
        new_usage = Usage(usage_quantity, parts_part_number, assemblies_assembly_part_number)
        violated_constraints = check_unique(sess, new_usage)
        
        parts = list(sess.query(Part))
        assemblies = list(sess.query(Assembly))

        if len(violated_constraints) > 0:
            print('The following uniqueness constraints were violated:')
            print(violated_constraints)
            print('please try again.')
            print(f"")
        if not any(part.part_number == parts_part_number for part in parts):
            print(f"Error: Part with part_number '{parts_part_number}' does not exist. Please add the Part first.")
            print(f"")
        elif not any(assembly.assembly_part_number == assemblies_assembly_part_number for assembly in assemblies):
            print(f"Error: Assembly with assembly_part_number '{assemblies_assembly_part_number}' does not exist. Please add the Assembly first.")
            print(f"")
        else: 
            sess.add(new_usage)
            # sess.commit()
        violation = False   

def add_vendors(sess: Session):
    supplier_name: str = ''
    vendor_id: str = ''
    violation = True
    while violation:
        vendor_id = input("Enter vendor_id: ")
        supplier_name = input("Enter supplier_name: ")
        new_vendors = Vendor(vendor_id, supplier_name)
        violated_constraints = check_unique(sess, new_vendors)

        if len(violated_constraints) > 0:
            print('The following uniqueness constraints were violated:')
            print(violated_constraints)
            print('please try again.')
            print(f"")
        else: 
            sess.add(new_vendors)
            # sess.commit()
        violation = False  

# --- Delete Functions ---
def delete(sess: Session):
    delete_action: str = ''
    while delete_action != delete_menu.last_action():
        delete_action = delete_menu.menu_prompt()
        exec(delete_action)

def exit_menu():
    print("Exiting add menu...")

# --- List Functions ---
def list_part(session: Session):
    parts = list(session.query(Part).order_by(Part.part_number))
    print("\n--- LIST OF PARTS ---")
    if not parts:
        print("No parts found.")
        print(f"")
    else:
        for part in parts:
            print(part)


def list_assembly(session: Session):
    assemblies = list(session.query(Assembly).order_by(Assembly.assembly_part_number))
    print("\n--- LIST OF ASSEMBLY ---")
    if not assemblies:
        print("No assembly found.")
        print(f"")
    else:
        for assembly in assemblies:
            print(assembly)

def list_usage(session: Session):
    usages = list(session.query(Usage).order_by(Usage.usage_quantity))
    print("\n--- List of Usages ---")
    if not usages:
        print("No Usages found.")
        print(f"")
    else:
        for usage in usages:
            print(usage)

def list_piece_parts(session: Session):
    pieceParts = list(session.query(PiecePart).order_by(PiecePart.part_number))
    print("\n--- List of Piece Parts ---")
    if not pieceParts:
        print("No Piece Part found.")
        print(f"")
    else:
        for piecePart in pieceParts:
            print(piecePart)

def list_vendors(session: Session):
    vendors = list(session.query(Vendor).order_by(Vendor.vendor_id))
    print("\n--- List of Piece Parts ---")
    if not Vendor:
        print("No Vendor found.")
    else:
        for vendor in vendors:
            print(vendor)