class ExcelReader:
    def __init__(self, excel_file_path):
        self.excel_file_path = excel_file_path

    def is_password_protected(self):
        try:
            # Attempt to read the Excel file
            pd.read_excel(self.excel_file_path)
            return False  # Excel file opened successfully, not password-protected
        except Exception as e:
            error_message = str(e)
            if "password" in error_message.lower():
                return True  # Excel file is password-protected
            else:
                return False  # Other error occurred, not password-protected

    def read_excel(self):
        if self.is_password_protected():
            return None  # Return None if the Excel file is password-protected

        try:
            df = pd.read_excel(self.excel_file_path)
            return df
        except Exception as e:
            return str(e)  # Handle any exceptions during Excel file reading
