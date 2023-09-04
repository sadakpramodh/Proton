import chainlit as cl


# Example usage:
if __name__ == "__main__":
    docx_path = "sample.docx"  # Replace with your document file path
    doc_reader = DocReader(docx_path)

    if doc_reader.is_password_protected():
        print("The document is password-protected.")
    else:
        document_text = doc_reader.read_document()
        if document_text is not None:
            print("Document contents:\n", document_text)
        else:
            print("Failed to read the document (possibly password-protected).")


# Example usage:
if __name__ == "__main__":
    excel_path = "sample.xlsx"  # Replace with your Excel file path
    excel_reader = ExcelReader(excel_path)

    if excel_reader.is_password_protected():
        print("The Excel file is password-protected.")
    else:
        excel_data = excel_reader.read_excel()
        if excel_data is not None:
            print("Excel data:\n", excel_data)
        else:
            print("Failed to read the Excel file (possibly password-protected).")


# Example usage:
if __name__ == "__main__":
    csv_path = "sample.csv"  # Replace with your CSV file path
    csv_reader = CSVReader(csv_path)

    csv_data = csv_reader.read_csv()
    if isinstance(csv_data, pd.DataFrame):
        print("CSV data:\n", csv_data)
    else:
        print("Failed to read the CSV file.")