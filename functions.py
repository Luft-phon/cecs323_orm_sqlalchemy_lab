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
    new_part: Part = None
    while violation:
        part_number = input("Enter part_number: ")
        part_name = input("Enter part_name: ")
        new_part = Part(part_number, part_name)
        # pass the active session instance `sess`, not the Session class
        violated_constraints = check_unique(sess, new_part)
        if len(violated_constraints) > 0:
            print('The following uniqueness constraints were violated:')
            print(violated_constraints)
            print('please try again.')
        else:
            violation = False
    sess.add(new_part)

# --- Delete Functions ---
def delete_part(sess: Session):
    part_number: str = input("Enter part_number of the part to delete: ")
    part = sess.query(Part).filter(Part.part_number == part_number).first()
    if part:
        sess.delete(part)
        print(f"Part {part_number} deleted.")
    else:
        print(f"Part {part_number} not found.")
    
def delete_assembly(sess: Session):
    assembly_part_number: str = input("Enter assembly_part_number of the assembly to delete: ")
    assembly = sess.query(Assembly).filter(Assembly.assembly_part_number == assembly_part_number).first()
    if assembly:
        sess.delete(assembly)
        print(f"Assembly {assembly_part_number} deleted.")
    else:
        print(f"Assembly {assembly_part_number} not found.")
        
def delete_usage(sess: Session):
    usage_id: int = int(input("Enter usage_id of the usage to delete: "))
    usage = sess.query(Usage).filter(Usage.usage_id == usage_id).first()
    if usage:
        sess.delete(usage)
        print(f"Usage {usage_id} deleted.")
    else:
        print(f"Usage {usage_id} not found.")

def delete_piece_parts(sess: Session):
    part_number: str = input("Enter part_number of the piece part to delete: ")
    piece_part = sess.query(PiecePart).filter(PiecePart.part_number == part_number).first()
    if piece_part:
        sess.delete(piece_part)
        print(f"Piece Part {part_number} deleted.")
    else:
        print(f"Piece Part {part_number} not found.")
def delete_vendors(sess: Session):
    vendor_id: int = int(input("Enter vendor_id of the vendor to delete: "))
    vendor = sess.query(Vendor).filter(Vendor.vendor_id == vendor_id).first()
    if vendor:
        sess.delete(vendor)
        print(f"Vendor {vendor_id} deleted.")
    else:
        print(f"Vendor {vendor_id} not found.")
# --- Update Functions ---

def update_part(sess: Session):
    part_number: str = input("Enter part_number of the part to update: ")
    part = sess.query(Part).filter(Part.part_number == part_number).first()
    if part:
        print(f"Current part_name: {part.part_name}")
        new_name: str = input("Enter new part_name: ")
        part.part_name = new_name
        print(f"Part {part_number} updated.")
    else:
        print(f"Part {part_number} not found.")
def update_vendor(sess: Session):
    vendor_id: int = int(input("Enter vendor_id of the vendor to update: "))
    vendor = sess.query(Vendor).filter(Vendor.vendor_id == vendor_id).first()
    if vendor:
        print(f"Current vendor_name: {vendor.supplier_name}")
        new_name: str = input("Enter new vendor_name: ")
        vendor.supplier_name = new_name
        print(f"Vendor {vendor_id} updated.")
    else:
        print(f"Vendor {vendor_id} not found.")

def exit_menu():
    print("Exiting add menu...")

# --- List Functions ---
def list_part(session: Session):
    parts = list(session.query(Part).order_by(Part.part_number))
    print("\n--- LIST OF PARTS ---")
    if not parts:
        print("No parts found.")
    else:
        for part in parts:
            print(part)


def list_assembly(session: Session):
    assemblies = list(session.query(Assembly).order_by(Assembly.assembly_part_number))
    print("\n--- List of Assemblies ---")
    if not assemblies:
        print("No assembly found.")
    else:
        for assembly in assemblies:
            print(assembly)

def list_usage(session: Session):
    usages = list(session.query(Usage).order_by(Usage.usage_quantity))
    print("\n--- List of Usages ---")
    if not usages:
        print("No Usages found.")
    else:
        for usage in usages:
            print(usage)

def list_piece_parts(session: Session):
    pieceParts = list(session.query(PiecePart).order_by(PiecePart.part_number))
    print("\n--- List of Piece Parts ---")
    if not pieceParts:
        print("No Piece Part found.")
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