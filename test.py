from unittest import TestCase
from flask import Flask, request, render_template, session, redirect, flash

from app import app

class FlaskTest(TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_convert(self):
        response = self.client.get('/convert')
        self.assertEqual(session['data']['EUR'], 1)
        self.assertEqual(session['data']['USD'], session['data']['USD'])
        self.assertEqual(session['data']['JPY'], session['data']['JPY'])