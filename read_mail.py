#!/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
import signal
import getpass
import imapclient
import pyzmail
import smtplib, time, imaplib,email
from conn_sql import conn_sql

def read_mail():
	try:
		print('###########')
		print('Reading mails from a gmail account')
		print('###########')

		mail = imapclient.IMAPClient('imap.gmail.com', ssl=True)
		email = raw_input("Enter email account [user.desafio01@gmail.com]: ")
		password = raw_input("Enter password account [default]: ")
		if email == "" and password == "":
			email = 'user.desafio01@gmail.com'
			password = 'U$3Rdesafio01'
			mail.login(email, password)
		else:
			mail.login(email, password)
		mail.select_folder('INBOX', readonly=True)
		UIDs = mail.search("ALL")

		for line in UIDs:
			rawMessages = mail.fetch([line], ['BODY[]', 'FLAGS'])
			message = pyzmail.PyzMessage.factory(rawMessages[line]['BODY[]'])
			if 'DevOps' in message.get_subject() or 'DevOps' in message.get_payload():
				origem = message.get_address('from')[1]
				assunto = message.get_subject()
				data = message.get_decoded_header('date')
				insert_info = ("INSERT INTO MailsInfo (data, origem, assunto) \
					VALUES ('{}','{}','{}')").format(origem, assunto, data)
				conn_sql(insert_info)

	except Exception as e:
		print(e)



read_mail()