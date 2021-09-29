def raf1(subject):
    import xlwt
    import xlrd
    from xlutils.copy import copy

    rb = xlrd.open_workbook('EEG_HMC_FeatureExtraction.xlsx')
    wb2 = copy(rb)
    w_sheet2 = wb2.get_sheet(0)

    next_index = xlrd.open_workbook("/content/EEG_HMC_FeatureExtraction.xlsx").sheet_by_index(0).nrows
    sheet4 = xlrd.open_workbook("/content/content/sleep_scooring_xls/" + subject + "_sleepscoring.xls").sheet_by_index(
        0)

    wb = xlrd.open_workbook("/content/eeg analysis result/" + subject + "_CH1_F4.xls")
    sheet = wb.sheet_by_index(0)
    row = sheet.nrows
    col = sheet.ncols

    # subject, epoc, sleeping score
    i = next_index
    l = 1
    for j in range(8, row):
        if sheet.cell_value(j, 0) == '':
            break
        w_sheet2.write(i, 0, subject)
        w_sheet2.write(i, 1, sheet4.cell_value(l, 0))
        w_sheet2.write(i, 2, sheet.cell_value(j, 0))
        i = i + 1
        l = l + 1

    rfr = 0
    first = 3
    second = 8
    for i in range(1, 16):
        if (i == 6):
            wb = xlrd.open_workbook("/content/eeg analysis result/" + subject + "_CH2_C4.xls")
            sheet = wb.sheet_by_index(0)
            row = sheet.nrows
            col = sheet.ncols
            rfr = 0
        elif (i == 11):
            wb = xlrd.open_workbook("/content/eeg analysis result/" + subject + "_CH3_O2.xls")
            sheet = wb.sheet_by_index(0)
            row = sheet.nrows
            col = sheet.ncols
            rfr = 0

        new_rfr = rfr
        rfc = 1
        for wfc in range(first, second):
            wfr = next_index
            rfr = new_rfr
            for rfr in range(rfr + 8, row):
                if sheet.cell_value(rfr, 0) == '':
                    break
                w_sheet2.write(wfr, wfc, sheet.cell_value(rfr, rfc))
                wfr = wfr + 1
            rfc = rfc + 1
        first = second
        second = second + 5

    wb2.save('EEG_HMC_FeatureExtraction.xlsx')

talika=['2','3','4','5','6','7','8','9','10','12','13','14','15','18','19','20','21','22','23','24','25','26','27','28','29','30','31','33','34','35','36','37','38','39','40','41','43','44','45','46','47','49','50','51','52','53','54','55','57','59','60']
for i in talika:
  raf1("SN0"+i)
  print("SN0"+i+" is complete!!!.........................")

