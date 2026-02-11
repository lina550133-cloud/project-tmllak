# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base

# Employees
class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    role = Column(String(100))

    profile = relationship("EmployeeProfile", back_populates="employee")
    teams = relationship("EmployeeTeam", back_populates="employee")


class EmployeeProfile(Base):
    __tablename__ = "employee_profiles"

    profile_id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employees.employee_id"))
    avatar = Column(String(255))
    bio = Column(Text)

    employee = relationship("Employee", back_populates="profile")


class EmployeeTeam(Base):
    __tablename__ = "employee_teams"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employees.employee_id"))
    team_id = Column(Integer, ForeignKey("teams.team_id"))
    role = Column(String(100))
    joined_at = Column(DateTime)

    employee = relationship("Employee", back_populates="teams")
    team = relationship("Team", back_populates="members")


# Teams
class Team(Base):
    __tablename__ = "teams"

    team_id = Column(Integer, primary_key=True)
    name = Column(String(255))

    members = relationship("EmployeeTeam", back_populates="team")


# Properties
class Property(Base):
    __tablename__ = "properties"

    property_id = Column(Integer, primary_key=True)
    address = Column(String(255))
    type = Column(String(100))
    status = Column(String(100))


# Clients
class Client(Base):
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    phone = Column(String(50))
    email = Column(String(255))
    created_at = Column(DateTime)


# Tasks
class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    status = Column(String(100))
    priority = Column(String(50))
    due_date = Column(DateTime)

    assigned_to = Column(Integer, ForeignKey("employees.employee_id"))
    project_id = Column(Integer)
    property_id = Column(Integer)


class TaskComment(Base):
    __tablename__ = "task_comments"

    comment_id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.task_id"))
    employee_id = Column(Integer, ForeignKey("employees.employee_id"))
    comment = Column(Text)
    created_at = Column(DateTime)


# Conversations & Messages
class Conversation(Base):
    __tablename__ = "conversations"

    conversation_id = Column(Integer, primary_key=True)
    type = Column(String(100))
    created_at = Column(DateTime)


class ConversationParticipant(Base):
    __tablename__ = "conversation_participants"

    id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, ForeignKey("conversations.conversation_id"))
    employee_id = Column(Integer, ForeignKey("employees.employee_id"))


class Message(Base):
    __tablename__ = "messages"

    message_id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, ForeignKey("conversations.conversation_id"))
    sender_id = Column(Integer, ForeignKey("employees.employee_id"))
    content = Column(Text)
    created_at = Column(DateTime)


# Files
class File(Base):
    __tablename__ = "files"

    file_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    related_id = Column(Integer)
    file_path = Column(String(255))
    uploaded_by = Column(Integer, ForeignKey("employees.employee_id"))
    uploaded_at = Column(DateTime)


# Notifications
class Notification(Base):
    __tablename__ = "notifications"

    notification_id = Column(Integer, primary_key=True)
    task_id = Column(Integer)
    type = Column(String(100))
    message = Column(Text)
    created_at = Column(DateTime)


# Deals
class Deal(Base):
    __tablename__ = "deals"

    deal_id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey("properties.property_id"))
    doc_number = Column(String(255))
    status = Column(String(100))
    file_url = Column(String(255))
