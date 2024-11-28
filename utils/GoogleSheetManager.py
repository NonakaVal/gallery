from streamlit_gsheets import GSheetsConnection
import streamlit as st
class GoogleSheetManager:
    def __init__(self, connection_type="gsheets"):
        self.conn = st.connection(connection_type, type=GSheetsConnection)
        self.spreadsheets = {}

    def set_url(self, url):
        if url not in self.spreadsheets:
            self.spreadsheets[url] = []

    def add_worksheet(self, url, worksheet_name):
        if url in self.spreadsheets:
            self.spreadsheets[url].append(worksheet_name)
        else:
            raise ValueError("URL não encontrada. Adicione a URL primeiro.")

    def read_sheet(self, url, worksheet):
        if url in self.spreadsheets and worksheet in self.spreadsheets[url]:
            data = self.conn.read(spreadsheet=url, worksheet=worksheet)
            return data.copy()
        else:
            raise ValueError("Worksheet não encontrada para esta URL.")

    def update_sheet(self, url, worksheet, data):
        if url in self.spreadsheets and worksheet in self.spreadsheets[url]:
            self.conn.update(spreadsheet=url, worksheet=worksheet, data=data)
        else:
            raise ValueError("Worksheet não encontrada para esta URL.")
