<h1 align="center"> ORM Python Practice Lab </h1>

```javascript
=== WELCOME TO CATEGORIZATION OF BILL MATERIAL ===

Please select one of the following options:
  1 - Add
  2 - List
  3 - Delete
  4 - Update
  5 - Exit this application

Enter your choice: ...
```

## 🌐 What is this lab project?
A part Bill of Material (BOM) is a network of parts within a product.  Each part could be an assembly,
in which case that part is composed of yet other parts, or the part is a "piece part" meaning that, for the purposes of the manufacturer, that part is a single unit with no constituent parts that we are interested in.

## ⭐ It allows user to:
- Insert new rows into each of the tables.
- Report out the data in a selected row from each of the tables.
- Delete a selected row, or give them an error message if such a deletion would leave orphaned rows.
- Update a selected row
  
## 📌 An abbreviated BOM for an idealized motorcycle
 <img alt="Fav Icon Png" src="https://github.com/Luft-phon/cecs323_orm_sqlalchemy_lab/blob/list/photos/BOM.png"/>

 <details>
   <summary align="center">VIEW MORE PHOTOS HERE</summary>
    <img alt="Fav Icon Png" src="https://github.com/Luft-phon/cecs323_orm_sqlalchemy_lab/blob/list/photos/ERD.png" />
    <img alt="Fav Icon Png" src="https://github.com/Luft-phon/cecs323_orm_sqlalchemy_lab/blob/list/photos/Enterprise%20description.jpg"/>
 </details>
 
## 🛠 Setup
1. Clone this repository
```
https://github.com/Luft-phon/cecs323_orm_sqlalchemy_lab.git
```

2. Open the project folder
   
3. Create config.ini file, we must defind  
```
[credentials]
userid = your-database-userid
password: your-database-password
host = localhost
port = ...
database = your-database-management-system
```
4. The program will ask to enter the database schema
   - This is usually "Public"

## 📁 Project Structure

```
Project/
├── db_connection.py/        # configuration to connect postgres
├── functions.py/            # methods  
├── main.py/       
├── menu_definition.py/      
├── menu.py/
├── option.py/    
├── part.py/                 # Mapped class
├── usage.py/                # Mapped class
├── vendor.py/               # Mapped class
├── piecePart.py/            # Mapped class
├── SQLAlchemyUltilities.py/ # Check constraints
├── orm_base.py/      
```
