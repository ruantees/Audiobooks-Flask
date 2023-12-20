from app import app, db, bcrypt
from db_tables import Role, User
from encryption import encrypt, decrypt


with app.app_context():
    db.drop_all()
    db.session.commit()
    db.create_all()
    db.session.commit()

with app.app_context():
    role1 = Role()
    role1.role = "Admin"
    role2 = Role()
    role2.role = "User"
    db.session.add(role1)
    db.session.add(role2)
    db.session.commit()

hashed_password = bcrypt.generate_password_hash("Sf7VkBZ6u4H9C/tMP")
with app.app_context():
    admin = User()
    admin.role_id = 1
    admin.email = encrypt("admin@audiobooks.com")
    admin.password = hashed_password
    admin.fullname = encrypt("Admin")
    db.session.add(admin)
    db.session.commit()
