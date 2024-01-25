from fpdf import FPDF

def report(rows, file_path):
	pdf = FPDF()
	pdf.add_page()
	pdf.set_xy(0, 0)


	pdf.set_font('arial', 'B',22)
	pdf.cell(50)
	pdf.cell(120, 15, "Armed Forces Personnel Report", 0, 1, 'C')



	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "Name:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(55, 16, rows[3], 0, 1, 'C')



	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "Military ID:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(55, 16, str(rows[1]), 0, 1, 'C')


	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "SSN:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(55, 16, str(rows[2]), 0, 1, 'C')



	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "Rank ID:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(55, 16, rows[4], 0, 1, 'C')


	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "Formation ID:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(55, 16, rows[6], 0, 1, 'C')


	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "Brnach ID:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(55, 16, rows[5], 0, 1, 'C')

	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "Leader ID:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(55, 16, str(rows[7]), 0, 1, 'C')


	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "Address:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(90, 16, rows[11], 0, 1, 'L')


	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "Phone No:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(55, 16, '0' + str(rows[12]), 0, 1, 'C')


	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "Blood Type:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(55, 16, rows[10], 0, 1, 'C')


	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "Birth Date:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(55, 16, rows[13], 0, 1, 'C')

	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "Marital Status:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(55, 16, rows[14], 0, 1, 'C')


	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "Physicality:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(55, 16, rows[9], 0, 1, 'C')

	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "Batch No:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(55, 16, rows[8], 0, 1, 'C')

	pdf.set_font('arial', 'B', 12)
	pdf.cell(30, 16, "Guarantor ID:", 0, 0)

	pdf.set_font('arial', '', 12)
	pdf.cell(55, 16, str(rows[15]), 0, 1, 'C')

	pdf.output(rf'{file_path}', 'F')


def genFormationReport(rows, formation_id, file_path):
	pdf = FPDF()
	pdf.add_page()
	pdf.set_xy(0, 0)


	pdf.set_font('arial', 'B',22)
	pdf.cell(50)
	pdf.cell(120, 15, f"Armed Forces {formation_id} Report", 0, 1, 'C')

	pdf.set_font('arial', 'B', 10)
	pdf.cell(30, 16, "Military ID:", 1, 0, 'C')

	pdf.set_font('arial', 'B', 10)
	pdf.cell(60, 16, "Name", 1, 0, 'C')

	pdf.set_font('arial', 'B', 10)
	pdf.cell(25, 16, "Rank ID:", 1, 0, 'C')

	pdf.set_font('arial', 'B', 10)
	pdf.cell(30, 16, "Branch ID:", 1, 0, 'C')

	pdf.set_font('arial', 'B', 10)
	pdf.cell(25, 16, "Leader ID:", 1, 0, 'C')

	pdf.set_font('arial', 'B', 10)
	pdf.cell(25, 16, "Blood Type:", 1, 1, 'C')

	

	for row in rows:

		if row[0] == 207192:    #FM
			r = 79
			g = 64
			b = 40
		elif row[0] == 987761:	#Defense 
			r = 181
			g = 178
			b = 87
		elif row[0] == 445933:  #airforce
			r = 54
			g = 83
			b = 99
		elif row[0] == 106772:  #navy
			r = 67
			g = 142
			b = 186
		elif row[0] == 475298: #chief of general staff
			r = 117
			g = 186
			b = 67
		elif row[0] == 168067: # air-def
			r = 59
			g = 80
			b = 110
		else:
			r = 255
			g = 255
			b = 255

		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(r,g,b)
		pdf.cell(30, 16, str(row[0]), 1, 0, 'C', 1)

		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(r,g,b)
		pdf.cell(60, 16, row[1], 1, 0, 'C', 1)

		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(r,g,b)
		pdf.cell(25, 16, row[2], 1, 0, 'C', 1)

		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(r,g,b)
		pdf.cell(30, 16, row[3], 1, 0, 'C', 1)

		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(r,g,b)
		pdf.cell(25, 16, str(row[4]), 1, 0, 'C', 1)

		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(r,g,b)
		pdf.cell(25, 16, row[5], 1, 1, 'C', 1)
	if formation_id == 'Leaders':
		pdf.set_font('arial', '', 10)
		pdf.cell(30, 16, "", 0, 1, 'C')


		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(79,64,40)
		pdf.cell(3, 3, '', 1, 0, 'C', 1)

		pdf.cell(7, 0, "", 0, 0, 'C')

		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(255,255,255)
		pdf.cell(33, 3, 'Commander In Chief', 0, 0, 'C', 1)


		pdf.cell(30, 0, "", 0, 0, 'C')


		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(181,178,87)
		pdf.cell(3, 3, '', 0, 0, 'C', 1)

		pdf.cell(7, 0, "", 0, 0, 'C')

		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(255,255,255)
		pdf.cell(33, 3, 'Defense Minister', 0, 0, 'C', 1)



		pdf.cell(30, 0, "", 0, 0, 'C')


		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(117,186,67)
		pdf.cell(3, 3, '', 0, 0, 'C', 1)

		pdf.cell(7, 0, "", 0, 0, 'C')

		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(255,255,255)
		pdf.cell(33, 3, 'Chief of General Staff', 0, 0, 'C', 1)




		pdf.set_font('arial', '', 10)
		pdf.cell(30, 11, "", 0, 1, 'C')

		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(67,142,186)
		pdf.cell(3, 3, '', 0, 0, 'C', 1)

		pdf.cell(7, 0, "", 0, 0, 'C')

		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(255,255,255)
		pdf.cell(33, 3, 'Navy Commander', 0, 0, 'C', 1)


		pdf.cell(30, 0, "", 0, 0, 'C')




		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(54,83,99)
		pdf.cell(3, 3, '', 0, 0, 'C', 1)

		pdf.cell(7, 0, "", 0, 0, 'C')

		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(255,255,255)
		pdf.cell(33, 3, 'Air Force Commander', 0, 0, 'C', 1)



		pdf.cell(30, 0, "", 0, 0, 'C')


		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(59, 80, 110)
		pdf.cell(3, 3, '', 0, 0, 'C', 1)

		pdf.cell(7, 0, "", 0, 0, 'C')

		pdf.set_font('arial', '', 10)
		pdf.set_fill_color(255,255,255)
		pdf.cell(33, 3, 'Air Defense Commander', 0, 1, 'C', 1)


	pdf.output(rf'{file_path}', 'F')	
		