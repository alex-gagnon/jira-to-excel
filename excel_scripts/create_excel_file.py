import xlwt as excel


class CreateExcel:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.book = excel.Workbook()
        self.filename = kwargs.get('filename')
        self.sheetname = kwargs.get('sheetname')

        self.sheet = self.book.add_sheet(self.sheetname or 'Sheet 1')

        print('Workbook initialized...')

    def __call__(self, *args, **kwargs):
        self.args = args
        self.filename = kwargs.get('filename')
        self.sheetname = kwargs.get('sheetname')
        self.sheet = self.book.add_sheet(self.sheetname or 'Sheet 1')

        print(f'Workbook filename and sheetname redefined as: filename={self.filename}, sheetname={self.sheetname}')

    def create_excel_book(self, data_list):
        print('Generating report...')
        self.write_data(data_list=data_list)
        self.save_and_close()

    def write_data(self, data_list, n=0):
        n += 1
        for dict_item in data_list:
            for n, (k, v) in enumerate(dict_item.items()):
                self.sheet.write(0, n, k)
                self.sheet.write(1, n, v)

    def save_and_close(self):
        self.book.save(self.filename + '.xls')
        print(f'Report finished. Excel file saved as "{self.filename}.xls"')
