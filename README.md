#### Video Demo: https://youtube.com/shorts/ZSwngnbrq-c
#### Description:
This is my CS50 Final Project by idivet (Antony Ancil). Its a simple Flask app for Venad Global Consultancy to track students going abroad.

I am from Kollam, Kerala. VGC gives honest career guidance. This app helps me track student name, country, course, status (Applied/Offer/Visa/Flown).

It uses same concepts as Finance PSET: login, register, SQLite, sessions.

#### How to run:
1. pip install Flask Flask-Session cs50
2. sqlite3 vgc.db -> CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, hash TEXT); CREATE TABLE students (id INTEGER PRIMARY KEY, user_id INTEGER, name TEXT, country TEXT, course TEXT, status TEXT);
3. flask run

#### About:
Made for CS50x 2026 - Final Project
