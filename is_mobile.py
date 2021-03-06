import xlwings as xl
from src.app import isMobile

def write_excel_for_mobile(excel_file_path, lower_bound,upper_bound):
    hcp_excel = xl.Book(excel_file_path)
    sheet = hcp_excel.sheets['Sheet1']
    i = lower_bound
    while i <= upper_bound:
        country = sheet.range('C'+str(i)+":"+'C'+str(i)).value
        contact_no = sheet.range('D'+str(i)+":"+'D'+str(i)).value
        if contact_no is None or country is None:
            i+=1
            continue
        country = country[0:2]
        if(country=='NL'):
            country = 'NL'
        elif(country=='BE'):
            country = 'BE'
        elif(country=='IT'):
            country = 'IT'
        elif(country=='FR'):
            country = 'FR'
        elif(country=='DE'):
            country = 'DE'
        elif(country=='ES'):
            country = 'ES'
        elif country=='GB':
            country = 'GB'
        sheet.range('E'+str(i)).value = isMobile(country,contact_no)
        i+=1
    hcp_excel.save()
    hcp_excel.close()

if __name__=="__main__":
    write_excel_for_mobile('HCP.xlsx',2,5)



