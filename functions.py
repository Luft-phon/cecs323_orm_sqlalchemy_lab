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