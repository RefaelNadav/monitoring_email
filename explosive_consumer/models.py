from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from db import Base, engine
import datetime



class Email(Base):
    __tablename__ = 'emails'
    id = Column(String, primary_key=True)
    email_address = Column(String, nullable=False)
    username = Column(String)
    ip_address = Column(String)
    created_at = Column(DateTime)
    location_id = Column(Integer, ForeignKey('locations.id'))
    device_info_id = Column(Integer, ForeignKey('device_info.id'))

    location = relationship("Location", back_populates="emails")
    device_info = relationship("DeviceInfo", back_populates="emails")
    explosive_content = relationship("SuspiciousExplosiveContent", back_populates="email")


class Location(Base):
    __tablename__ = 'locations'
    id = Column(String, primary_key=True)
    latitude = Column(Numeric(2, 8))
    longitude = Column(Numeric(2, 8))
    city = Column(String)
    country = Column(String)

    emails = relationship("Email", back_populates="location")


class DeviceInfo(Base):
    __tablename__ = 'device_info'
    id = Column(String, primary_key=True)
    browser = Column(String)
    os = Column(String)
    device_id = Column(String)

    emails = relationship("Email", back_populates="device_info")


class SuspiciousExplosiveContent(Base):
    __tablename__ = 'suspicious_explosive_content'
    id = Column(Integer, primary_key=True)
    email_id = Column(String, ForeignKey('emails.id'))
    suspicious_sentence = Column(String)
    detected_at = Column(DateTime)

    email = relationship("Email", back_populates="explosive_content")