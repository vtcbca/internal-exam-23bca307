{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "80246bfe-3d83-4342-8565-92b5845cce88",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "90b91f4e-8837-44f7-81ce-761151e7c927",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6ab833ae-4589-4374-a157-6c18f5d198bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "conn=sqlite3.connect(\"C:\\\\23bca262\\\\sqlite\\\\mydb.sqlite\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ef47a6fe-e463-4846-9f27-fa14fe79ece7",
   "metadata": {},
   "outputs": [],
   "source": [
    "cur=conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9df5d961-ff7c-4144-91e0-75848c090c2c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x15c9b191d40>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cur.execute('''create table if not exists product(user id int primary key, pid int,pname text,prate number,pqty int)''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "aa071692-7a31-454e-bcf8-7bdd23209336",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x15c9b191d40>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cur.execute(\"insert into product values(1,999,'pen',20,200),(2,444,'note',50,420),(3,555,'book',10,350),(4,666,'pencil',5,130),(5,777,'eraser',10,250)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "237e8c50-a9ec-4bda-a4f0-1fe3372ef8a5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x15c9b191d40>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cur.execute('select*from product')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "add94506-81a2-48a7-bcf8-9a0c1030ca0e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 999, 'pen', 20, 200),\n",
       " (2, 444, 'note', 50, 420),\n",
       " (3, 555, 'book', 10, 350),\n",
       " (4, 666, 'pencil', 5, 130),\n",
       " (5, 777, 'eraser', 10, 250)]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cur.fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "fe5065dd-0070-4d75-88d1-a1d0a7a57ea3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlite3.Cursor at 0x15c9b191d40>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cur.execute('''\n",
    "create trigger if not exists product_rate_qty\n",
    "before insert on product\n",
    "for each row\n",
    "begin\n",
    "select\n",
    "case\n",
    "when new.prate = 0 THEN\n",
    "raise (abort, 'Product rate cannot be zero.')\n",
    "when new.pqty = 0 THEN\n",
    "raise (abort, 'Product quantity cannot be zero.')\n",
    "end;\n",
    "end;\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c77d4cc-c507-42ec-a6e1-bc9474bac25c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
